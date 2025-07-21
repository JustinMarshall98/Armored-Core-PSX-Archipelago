import typing

from typing import TYPE_CHECKING
from NetUtils import ClientStatus
from collections import Counter
import random
import worlds._bizhawk as bizhawk
from worlds._bizhawk.client import BizHawkClient

from .version import __version__
from .utils import Constants
from .locations import get_location_id_for_mission, is_mission_location_id, mission_from_location_id
from .mission import Mission, all_missions

if TYPE_CHECKING:
    from worlds._bizhawk.context import BizHawkClientContext
    from NetUtils import JSONMessagePart

MAIN_RAM: typing.Final[str] = "MainRAM"

class ACClient(BizHawkClient):
    game: str = Constants.GAME_NAME
    system: str = "PSX"
    patch_suffix: str = ".apac"
    local_checked_locations: typing.Set[int]
    checked_version_string: bool

    def __init__(self) -> None:
        super().__init__()
        self.local_checked_locations = set()

    async def validate_rom(self, ctx: "BizHawkClientContext") -> bool:

        try:
            # this import down here to prevent circular import issue
            from CommonClient import logger
            # Check ROM name/patch version
            # Unable to locate rom name, verifying based on memory card id instead
            # If you know what the rom memory domain for PSX is on Bizhawk please let me know!
            mem_card_id_bytes = ((await bizhawk.read(ctx.bizhawk_ctx, [(0x4B6BD, 12, MAIN_RAM)]))[0])
            mem_card_id = bytes([byte for byte in mem_card_id_bytes if byte != 0]).decode("ascii")
            logger.info(mem_card_id + " mem_card_id")
            if not mem_card_id.startswith("BASCUS-94182"):
                return False
        except UnicodeDecodeError:
            return False
        except bizhawk.RequestFailedError:
            return False  # Should verify on the next pass

        ctx.game = self.game
        ctx.items_handling = 0b111 # Has this been set correctly? A little confusion
        ctx.want_slot_data = True
        ctx.watcher_timeout = 0.125
        logger.info(f"Armored Core 1 Client v{__version__}.")
        # Add updates section to logger info
        return True
    
    async def read_mission_completion(self, ctx: "BizHawkClientContext") -> typing.List[bool]:
        byte_list_missions: typing.List[bytes] = []
        for mission_number in range(len(all_missions)):
            # Don't read mission completion for omitted missions
            byte_list_missions.append((await bizhawk.read(
            ctx.bizhawk_ctx, [(Constants.MISSION_COMPLETION_OFFSET + all_missions[mission_number].id, 1, MAIN_RAM)]
            ))[0])
        mission_completed_flags: typing.List[bool] = []
        for byte in byte_list_missions:
            if int.from_bytes(byte) > 0:
                mission_completed_flags.append(True)
            else:
                mission_completed_flags.append(False)
        return mission_completed_flags
    
    async def update_mission_list_code(self, ctx: "BizHawkClientContext") -> None:
        # Mission list code needs to be updated on the fly by the client
        # Guarded Write confirms we are in ravens nest menu at the time of writing

        await self.set_mission_list_display_all(ctx)

        # Hooks into mission list write routine
        await bizhawk.guarded_write(ctx.bizhawk_ctx, [(
                    Constants.MISSION_MENU_HOOK_OFFSET,
                    [0xB4, 0x44, 0x00, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
                    MAIN_RAM
                )],[(
                    Constants.MISSION_MENU_HOOK_OFFSET,
                    [0x1F, 0x80, 0x01, 0x3C, 0x21, 0x08, 0x30, 0x00, 0xD4, 0x37, 0x23, 0xA0],
                    MAIN_RAM
                )])

        # Freespace we write to to update mission list as new mission checks are received
        code_as_hex: typing.List[int] = []
        #lui r1,0x801f
        #addu r1,r1,r16
        code_as_string: str = "1F80013C21083000"
        mission_counter: int = 0
        number_of_missions: int = 0
        for item in ctx.items_received:
                if is_mission_location_id(item.item):
                    number_of_missions += 1
        for item in ctx.items_received:
                if is_mission_location_id(item.item):
                    mission: Mission = mission_from_location_id(item.item)
                    code_as_string += self.construct_new_mission_code_entry(mission.id, mission_counter, number_of_missions)
                    mission_counter += 1
        code_as_string += "0000000000000324D43723A0891C020800000000"
        for i in range(0, len(code_as_string), 2):
            code_as_hex.append(int(code_as_string[i:i+2], 16))
        await bizhawk.write(ctx.bizhawk_ctx, [(
                    Constants.FREESPACE_CODE_OFFSET,
                    code_as_hex,
                    MAIN_RAM
                )])
        

    def construct_new_mission_code_entry(self, mission_id: int, mission_counter: int, number_of_missions: int) -> str:
        new_code_entry: str = ""
        # The immediate value being written
        if (mission_counter < 16):
            new_code_entry += "0" + hex(mission_counter)[2:]
        else:
            new_code_entry += hex(mission_counter)[2:]
        new_code_entry += "000224"
        # Branch by an additional 0xC(12) bytes for every mission entry
        branch_amount = (number_of_missions - mission_counter) * 3
        if (branch_amount < 16):
            new_code_entry += "0" + hex(branch_amount)[2:]
        else:
            new_code_entry += hex(branch_amount)[2:]
        new_code_entry += "005010"
        if (mission_id < 16):
            new_code_entry += "0" + hex(mission_id)[2:]
        else:
            new_code_entry += hex(mission_id)[2:]
        new_code_entry += "000324"
        return new_code_entry
    
    async def set_mission_list_display_all(self, ctx: "BizHawkClientContext") -> None:
        # Guarded write ensures we do this only when the menu is open
        #from CommonClient import logger

        await bizhawk.guarded_write(ctx.bizhawk_ctx, [(
                    Constants.MISSION_LIST_MODE_OFFSET,
                    [0x00],
                    MAIN_RAM
                )],[(
                    Constants.MISSION_MENU_HOOK_OFFSET,
                    [0x1F, 0x80, 0x01, 0x3C, 0x21, 0x08, 0x30, 0x00, 0xD4, 0x37, 0x23, 0xA0],
                    MAIN_RAM
                )])

        


    
    async def game_watcher(self, ctx: "BizHawkClientContext") -> None:
        if ctx.slot_data is not None:

            if not ctx.finished_game and any((item.item == Constants.VICTORY_ITEM_ID) for item in ctx.items_received):
                await ctx.send_msgs([{
                    "cmd": "StatusUpdate",
                    "status": ClientStatus.CLIENT_GOAL
                }])
                ctx.finished_game = True

            # Items received handling

            # Unlock missions based on what has been received

            await self.update_mission_list_code(ctx)



            # Local checked checks handling

            new_local_check_locations: typing.Set[int]

            # Read mission completion locations
            completed_missions_flags: typing.List[bool] = await self.read_mission_completion(ctx)

            missions_to_completed: typing.Dict[Mission, bool] = {
                m: c for m, c in zip(all_missions, completed_missions_flags)
            }

            new_local_check_locations = set([
                get_location_id_for_mission(key) for key, value in missions_to_completed.items() if value
            ])

            if new_local_check_locations != self.local_checked_locations:
                self.local_checked_locations = new_local_check_locations
                if new_local_check_locations is not None:
                    await ctx.send_msgs([{
                        "cmd": "LocationChecks",
                        "locations": list(new_local_check_locations)
                    }])