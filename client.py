import typing

from typing import TYPE_CHECKING
from NetUtils import ClientStatus
from BaseClasses import ItemClassification
from collections import Counter
import random
import worlds._bizhawk as bizhawk
from worlds._bizhawk.client import BizHawkClient

from .version import __version__
from .utils import Constants
from .locations import get_location_id_for_mission, is_mission_location_id, mission_from_location_id, get_location_id_for_mail, get_location_id_for_shop_listing
from .mission import Mission, all_missions
from .mail import Mail, all_mail
from .parts import Part, all_parts, id_to_part, all_parts_data_order, base_starting_parts

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
            logger.info(f"{mem_card_id} mem_card_id")
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
    
    async def shopsanity_initialization(self, ctx: "BizHawkClientContext", in_menu) -> None:
        if not in_menu or ctx.slot_data[Constants.GAME_OPTIONS_KEY]["shopsanity"] == False:
            return []
        # Disable the Sell option in game
        await bizhawk.guarded_write(ctx.bizhawk_ctx, [(
                    Constants.SHOP_SELL_INTERCEPT_OFFSETS[0],
                    [0x00, 0x00, 0x60, 0xA0],
                    MAIN_RAM
                )],[(
                    Constants.SHOP_SELL_INTERCEPT_OFFSETS[0],
                    [0x00, 0x00, 0x62, 0xA0],
                    MAIN_RAM
                )])
        await bizhawk.guarded_write(ctx.bizhawk_ctx, [(
                    Constants.SHOP_SELL_INTERCEPT_OFFSETS[1],
                    [0x00, 0x00, 0x60, 0xA0],
                    MAIN_RAM
                )],[(
                    Constants.SHOP_SELL_INTERCEPT_OFFSETS[1],
                    [0x00, 0x00, 0x62, 0xA0],
                    MAIN_RAM
                )])
        await bizhawk.guarded_write(ctx.bizhawk_ctx, [(
                    Constants.SHOP_SELL_INTERCEPT_OFFSETS[2],
                    [0x00, 0x00, 0x60, 0xA0],
                    MAIN_RAM
                )],[(
                    Constants.SHOP_SELL_INTERCEPT_OFFSETS[2],
                    [0x00, 0x00, 0x62, 0xA0],
                    MAIN_RAM
                )])
        await bizhawk.guarded_write(ctx.bizhawk_ctx, [(
                    Constants.SHOP_SELL_INTERCEPT_OFFSETS[3],
                    [0x00, 0x00, 0x60, 0xA0],
                    MAIN_RAM
                )],[(
                    Constants.SHOP_SELL_INTERCEPT_OFFSETS[3],
                    [0x00, 0x00, 0x62, 0xA0],
                    MAIN_RAM
                )])

        # Change Sell text to BUY2
        await bizhawk.guarded_write(ctx.bizhawk_ctx, [(
                    Constants.SHOP_SELL_TEXT__OFFSET,
                    [0x42, 0x55, 0x59, 0x32],
                    MAIN_RAM
                )],[(
                    Constants.SHOP_SELL_TEXT__OFFSET,
                    [0x53, 0x45, 0x4C, 0x4C],
                    MAIN_RAM
                )])

        shop_listings: int = int.from_bytes((await bizhawk.read(
            ctx.bizhawk_ctx, [(Constants.SHOPSANITY_TRACKING_OFFSET, 1, MAIN_RAM)]
            ))[0])
        if shop_listings == 0: # The run has just begun, set listings to 1 and remove everything from the shop
            shop_listings = 1
            new_shop_contents: str = "00" * 146
            shop_contents_hex: typing.List[int] = []
            for i in range(0, len(new_shop_contents), 2):
                shop_contents_hex.append(int(new_shop_contents[i:i+2], 16))
            # Write instead of guarded write based on ravens nest menu check
            await bizhawk.write(ctx.bizhawk_ctx, [(
                        Constants.SHOP_INVENTORY_OFFSET,
                        shop_contents_hex,
                        MAIN_RAM
                    )])
            # Write shop listings so this won't happen again
            await bizhawk.write(ctx.bizhawk_ctx, [(
                        Constants.SHOPSANITY_TRACKING_OFFSET,
                        shop_listings,
                        MAIN_RAM
                    )])


        
    
    async def read_mission_completion(self, ctx: "BizHawkClientContext", in_menu) -> typing.List[bool]:
        if not in_menu:
            return []
        byte_list_missions: typing.List[bytes] = []
        for mission_number in range(len(all_missions)):
            # Don't read mission completion for omitted missions
            byte_list_missions.append((await bizhawk.read(
            ctx.bizhawk_ctx, [(Constants.MISSION_COMPLETION_OFFSET + all_missions[mission_number].id, 1, MAIN_RAM)]
            ))[0])
        mission_completed_flags: typing.List[bool] = []
        for byte in byte_list_missions:
            if int.from_bytes(byte) & 0x2 == 0x2:
                mission_completed_flags.append(True)
            else:
                mission_completed_flags.append(False)
        return mission_completed_flags
    
    async def read_mail_read_flags(self, ctx: "BizHawkClientContext", in_menu) -> typing.List[bool]:
        if not in_menu:
            return []
        
        byte_list_mail: typing.List[bytes] = []
        for mail_number in range(len(all_mail)):
            # Don't read mail read flag for omitted mail
            byte_list_mail.append((await bizhawk.read(
            ctx.bizhawk_ctx, [(Constants.MAIL_RECEPTION_OFFSET + all_mail[mail_number].id, 1, MAIN_RAM)]
            ))[0])
        mail_read_flags: typing.List[bool] = []
        # There must be a better way! Too tired to think of a better one atm
        accepted_bytes: typing.List[bytes] = [0x3, 0x7, 0xb, 0xf,
                                              0x13, 0x17, 0x1b, 0x1f, 
                                              0x23, 0x27, 0x2b, 0x2f, 
                                              0x33, 0x37, 0x3b, 0x3f,
                                              0x43, 0x47, 0x4b, 0x4f,
                                              0x53, 0x57, 0x5b]
        for byte in byte_list_mail:
            if int.from_bytes(byte) in accepted_bytes:
                mail_read_flags.append(True)
            else:
                mail_read_flags.append(False)
        return mail_read_flags
    
    # return: True/False if it detects we are in the Ravens Nest Menu
    async def ravens_nest_menu_check(self, ctx: "BizHawkClientContext") -> bool:
        MENU_LOADED_BYTES: bytes = bytes([0xC0, 0xDC, 0x04, 0x80])
        menu_verification: bytes = (await bizhawk.read(
            ctx.bizhawk_ctx, [(Constants.MENU_LOADED_VERIFY_OFFSET1, 4, MAIN_RAM)]
            ))[0]
        if menu_verification == MENU_LOADED_BYTES:
            return True
        else:
            menu_verification = int.from_bytes((await bizhawk.read(
                ctx.bizhawk_ctx, [(Constants.MENU_LOADED_VERIFY_OFFSET2, 4, MAIN_RAM)]
                ))[0])
            if menu_verification == MENU_LOADED_BYTES:
                return True
            return False

    # return: 0-5 indicates what part of the ravens nest menu we are hovering / in. -1 means we are not in the ravens nest menu.
    async def ravens_nest_menu_section_check(self, ctx: "BizHawkClientContext") -> int:
        menu_verification: int = int.from_bytes((await bizhawk.read(
            ctx.bizhawk_ctx, [(Constants.MENU_CURRENT_SELECTION1_VERIFY_OFFSET, 1, MAIN_RAM)]
            ))[0])
        if menu_verification == 0x20 or menu_verification == 0xE0:
            return int.from_bytes((await bizhawk.read(
            ctx.bizhawk_ctx, [(Constants.MENU_CURRENT_SELECTION1_OFFSET, 1, MAIN_RAM)]
            ))[0])
        else:
            menu_verification = int.from_bytes((await bizhawk.read(
            ctx.bizhawk_ctx, [(Constants.MENU_CURRENT_SELECTION2_VERIFY_OFFSET, 1, MAIN_RAM)]
            ))[0])
            if menu_verification == 0x20 or menu_verification == 0xE0:
                return int.from_bytes((await bizhawk.read(
                ctx.bizhawk_ctx, [(Constants.MENU_CURRENT_SELECTION2_OFFSET, 1, MAIN_RAM)]
                ))[0])
            else:
                return -1
    
    async def update_mission_list_code(self, ctx: "BizHawkClientContext", menu_section) -> None:
        # Mission list code needs to be updated on the fly by the client

        if menu_section != 2:
            return
        
        # Lock / Unlock if the mission menu is about to be loaded and the Mail data hasn't been overwritten with mission data
        # I hate fighting race conditions (need to find other free space)

        code_written_check: int = int.from_bytes((await bizhawk.read(
            ctx.bizhawk_ctx, [(Constants.FREESPACE_CODE_OFFSET, 1, MAIN_RAM)]
            ))[0])
        locked: bool = False
        
        if code_written_check != 0x1F:
            await bizhawk.lock(ctx.bizhawk_ctx)
            locked = True

        await self.set_mission_list_display_all(ctx)

        # Hooks into mission list write routine
        # OOF hardcoded this jump. If freespace changes this too must change unless you code better
        await bizhawk.guarded_write(ctx.bizhawk_ctx, [(
                    Constants.MISSION_MENU_HOOK_OFFSET,
                    [0x18, 0xFE, 0x05, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
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
        if ctx.slot_data[Constants.GAME_OPTIONS_KEY]["goal"] == 0: # Missionsanity
            for item in ctx.items_received:
                    if is_mission_location_id(item.item):
                        number_of_missions += 1
            for item in ctx.items_received:
                    if is_mission_location_id(item.item):
                        mission: Mission = mission_from_location_id(item.item)
                        code_as_string += self.construct_new_mission_code_entry(mission.id, mission_counter, number_of_missions)
                        mission_counter += 1
        else: # Progressive Missions
            progressive_missions_received: int = 0
            for item in ctx.items_received:
                if item.item == Constants.PROGRESSIVE_MISSION_ITEM_ID:
                    progressive_missions_received += 1
            # number_of_missions is 5 * progressive mission items up to 8 times, then the 9th is 1. 46 total in the end.
            if progressive_missions_received < 9:
                number_of_missions = 5 * (progressive_missions_received + 1)
            else:
                number_of_missions = 46
            for i in range(1, progressive_missions_received + 2):
                for mission in all_missions:
                    if mission.progression_level == i:
                        code_as_string += self.construct_new_mission_code_entry(mission.id, mission_counter, number_of_missions)
                        mission_counter += 1
        code_as_string += "0000000000000324D43723A0891C020800000000"
        for i in range(0, len(code_as_string), 2):
            code_as_hex.append(int(code_as_string[i:i+2], 16))
        # Write instead of guarded write based on ravens nest menu check
        await bizhawk.write(ctx.bizhawk_ctx, [(
                    Constants.FREESPACE_CODE_OFFSET,
                    code_as_hex,
                    MAIN_RAM
                )])
        
        if locked:
            await bizhawk.unlock(ctx.bizhawk_ctx)
        

    def construct_new_mission_code_entry(self, mission_id: int, mission_counter: int, number_of_missions: int) -> str:
        new_code_entry: str = ""
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

        await bizhawk.guarded_write(ctx.bizhawk_ctx, [(
                    Constants.MISSION_LIST_MODE_OFFSET,
                    [0x00],
                    MAIN_RAM
                )],[(
                    Constants.MISSION_MENU_HOOK_OFFSET,
                    [0x18, 0xFE, 0x05, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
                    MAIN_RAM
                )])
        
    async def award_credits(self, ctx: "BizHawkClientContext", in_menu) -> None:
        # We fail to award credits if we are not in the ravens nest menu at all
        if not in_menu:
            return
        
        # Read how many credit items have been received
        stored_credit_drops: int = int.from_bytes((await bizhawk.read(
            ctx.bizhawk_ctx, [(Constants.CREDIT_ITEMS_RECEIVED_OFFSET, 1, MAIN_RAM)]
            ))[0])
        
        received_credit_drops: int = 0
        for item in ctx.items_received:
                if item.item == Constants.CREDIT_ITEM_ID:
                    received_credit_drops += 1

        from CommonClient import logger
        
        if received_credit_drops > stored_credit_drops:
            # Award the difference to the player
            player_credit_bytes = (await bizhawk.read(
                ctx.bizhawk_ctx, [(Constants.PLAYER_CREDITS_OFFSET, 4, MAIN_RAM)]
                ))
            player_credit: int = int.from_bytes(player_credit_bytes[0], "little", signed = True)
            logger.info(f"Player credits read as {player_credit}")
            p1, p2, p3, p4 = (player_credit & 0xFFFFFFFF).to_bytes(4, "little")
            player_credit = player_credit + ((received_credit_drops - stored_credit_drops) * ctx.slot_data[Constants.GAME_OPTIONS_KEY]["credit_check_amount"])
            c1, c2, c3, c4 = (player_credit & 0xFFFFFFFF).to_bytes(4, "little")
            logger.info(f"Attempting to award {(received_credit_drops - stored_credit_drops) * ctx.slot_data[Constants.GAME_OPTIONS_KEY]["shopsanity"]}, new total should be {player_credit}")
            logger.info(f"bytes {player_credit.to_bytes(4, "little", signed = True)} and {player_credit_bytes} and {player_credit_bytes[0]} and {c1} {c2} {c3} {c4}")
            # Guarded write based on read in credit amount. Stops things from messing up when the game is updating credit value
            award_success: bool = await bizhawk.guarded_write(ctx.bizhawk_ctx, [(
                    Constants.PLAYER_CREDITS_OFFSET,
                    [c1, c2, c3, c4],
                    MAIN_RAM
                )],[(
                    Constants.PLAYER_CREDITS_OFFSET,
                    [p1, p2, p3, p4],
                    MAIN_RAM
                )])
            if award_success:
                await bizhawk.write(ctx.bizhawk_ctx, [(
                    Constants.CREDIT_ITEMS_RECEIVED_OFFSET,
                    [received_credit_drops],
                    MAIN_RAM
                )])
    
    async def award_humanplus(self, ctx: "BizHawkClientContext", in_menu) -> None:
        # We fail to award humanplus levels if we are not in the ravens nest menu at all
        # Although it should be safe to do during missions as well...
        if not in_menu:
            return
        
        # Read what human+ level we are at
        # Progressive Human+ checks will overwrite Human+ progress from regular gameplay.
        # This is probably fine
        stored_humanplus_level: int = int.from_bytes((await bizhawk.read(
            ctx.bizhawk_ctx, [(Constants.HUMANPLUS_LEVEL_OFFSET, 1, MAIN_RAM)]
            ))[0])
        
        received_humanplus_drops: int = 0
        for item in ctx.items_received:
                if item.item == Constants.PROGRESSIVE_HUMANPLUS_ITEM_ID:
                    received_humanplus_drops += 1
        
        new_humanplus_level: int
        if received_humanplus_drops == 1:
            new_humanplus_level = 0x1
        elif received_humanplus_drops == 2:
            new_humanplus_level = 0x4
        elif received_humanplus_drops == 3:
            new_humanplus_level = 0x6
        else:
            new_humanplus_level = 0x0
        
        if stored_humanplus_level < new_humanplus_level:
            # Award new human+ level
            await bizhawk.guarded_write(ctx.bizhawk_ctx, [(
                    Constants.HUMANPLUS_LEVEL_OFFSET,
                    [new_humanplus_level],
                    MAIN_RAM
                )],[(
                    Constants.HUMANPLUS_LEVEL_OFFSET,
                    [stored_humanplus_level],
                    MAIN_RAM
                )])
            
    async def award_shop_listings(self, ctx: "BizHawkClientContext", mission_completion_count, in_menu) -> None:
        # Don't bother if Shopsanity is not on
        # shop listings are based on the number of completed missions
        # shop listings are immediately scouted when the player earns them

        if not in_menu or ctx.slot_data[Constants.GAME_OPTIONS_KEY]["shopsanity"] == False:
            return []
        
        shop_listings: int = int.from_bytes((await bizhawk.read(
            ctx.bizhawk_ctx, [(Constants.SHOPSANITY_TRACKING_OFFSET, 1, MAIN_RAM)]
            ))[0])
        
        # Because shop_listings starts at 1 and not 0, offset this by -1
        shop_listings -= 1

        shop_listings_unlock_order: list[Part] = list(all_parts_data_order)

        if mission_completion_count > shop_listings: # We have listings to award the player
            for i in range(shop_listings, mission_completion_count):
                start_index: int = i * ctx.slot_data[Constants.GAME_OPTIONS_KEY]["shopsanity_listings_per_mission"]
                end_index: int = (((i + 1) * ctx.slot_data[Constants.GAME_OPTIONS_KEY]["shopsanity_listings_per_mission"]) if ((i + 1) * ctx.slot_data[Constants.GAME_OPTIONS_KEY]["shopsanity_listings_per_mission"]) < len(shop_listings_unlock_order) 
                                                                                            else len(shop_listings_unlock_order) - 1)
                for part in shop_listings_unlock_order[start_index : end_index]:
                    # Put one in the store inventory
                    await bizhawk.write(ctx.bizhawk_ctx, [(
                        Constants.SHOP_INVENTORY_OFFSET + part.id,
                        [0x01],
                        MAIN_RAM
                    )])
                    # Scout the location (a free hint for the player so they can easily tell what is in the shop)
                    await ctx.send_msgs([{
                        "cmd": "LocationScouts",
                        "locations": [
                            get_location_id_for_shop_listing(part)
                        ],
                        "create_as_hint": 2
                    }])
            # Now write mission_completion_count + 1 to shop listings
            await bizhawk.write(ctx.bizhawk_ctx, [(
                Constants.SHOPSANITY_TRACKING_OFFSET,
                [mission_completion_count + 1],
                MAIN_RAM
            )])

    async def award_parts(self, ctx: "BizHawkClientContext") -> None:
        # No menu check required, it's always loaded in memory

        # Shopsanity check
        if ctx.slot_data[Constants.GAME_OPTIONS_KEY]["shopsanity"] == False:
            return []

        inventory_bytes = list((await bizhawk.read(
                ctx.bizhawk_ctx, [(Constants.PARTS_INVENTORY_OFFSET, 146, MAIN_RAM)]
                ))[0])
        inventory_copy = list(inventory_bytes)
        for item in ctx.items_received:
            partID: int = item.item - Constants.PARTS_INVENTORY_OFFSET # Converts from ap itemID back to part id when subtracting
            if partID in id_to_part: 
                if inventory_bytes[partID] == 0x00:
                    inventory_bytes[partID] = 0x02 # Give 2 of those parts

        # If no new parts have been given, don't perform the gaurded write
        if inventory_bytes == inventory_copy:
            return []

        await bizhawk.guarded_write(ctx.bizhawk_ctx, [(
                    Constants.PARTS_INVENTORY_OFFSET,
                    inventory_bytes,
                    MAIN_RAM
                )],[(
                    Constants.PARTS_INVENTORY_OFFSET,
                    inventory_copy,
                    MAIN_RAM
                )])
            
    # Checks shop listings received vs that listing still being available for purchase
    # Also removes the part that was just purchased from the players inventory
    async def check_purchased_items(self, ctx: "BizHawkClientContext", mission_completion_count, in_menu) -> typing.Dict[Part, bool]:
        if not in_menu or ctx.slot_data[Constants.GAME_OPTIONS_KEY]["shopsanity"] == False:
            return {}
        
        shop_listings_unlock_order: list[Part] = list(all_parts_data_order)
        purchased_items: typing.Dict[Part, bool] = {}
        # There are 146 entries
        purchased_bytes = (await bizhawk.read(
                ctx.bizhawk_ctx, [(Constants.SHOP_INVENTORY_OFFSET, 146, MAIN_RAM)]
                ))[0]
        inventory_bytes = list((await bizhawk.read(
                ctx.bizhawk_ctx, [(Constants.PARTS_INVENTORY_OFFSET, 146, MAIN_RAM)]
                ))[0])
        inventory_copy = list(inventory_bytes)

        
        if mission_completion_count > 0:
            start_index: int = 0
            end_index: int = (((mission_completion_count) * ctx.slot_data[Constants.GAME_OPTIONS_KEY]["shopsanity_listings_per_mission"]) if ((mission_completion_count) * ctx.slot_data[Constants.GAME_OPTIONS_KEY]["shopsanity_listings_per_mission"]) < len(purchased_bytes) 
                                                                                                                    else len(purchased_bytes))
            for count, byte in enumerate(purchased_bytes[start_index : end_index]):
                #print(int.from_bytes(byte, "little", signed = True))
                true_part_index: int = shop_listings_unlock_order[count].id
                if byte == 0x00:
                    # The player has had a shop listing given and then purchased that item if they also have one or three
                    if inventory_bytes[true_part_index] == 0x01 or inventory_bytes[true_part_index] == 0x03 or (inventory_bytes[true_part_index] == 0x02 and shop_listings_unlock_order[count] in base_starting_parts):
                        purchased_items[shop_listings_unlock_order[true_part_index]] = True
                    # It will be 01 if they have just made the purchase but don't have that part in their inventory
                    if inventory_bytes[true_part_index] == 0x01:
                        inventory_bytes[true_part_index] = 0x00
                    # If they've purchased the item but they've already received that part, it doesn't matter if more are given to them

        # Inequality signifies that the inventory needs updating
        if inventory_bytes != inventory_copy:
            await bizhawk.guarded_write(ctx.bizhawk_ctx, [(
                    Constants.PARTS_INVENTORY_OFFSET,
                    inventory_bytes,
                    MAIN_RAM
                )],[(
                    Constants.PARTS_INVENTORY_OFFSET,
                    inventory_copy,
                    MAIN_RAM
                )])
        
        return purchased_items

    # Update shop item and description text when shopsanity is active
    async def shopsanity_update_shop_text(self, ctx: "BizHawkClientContext", menu_section) -> None:
        if menu_section != 1 or ctx.slot_data[Constants.GAME_OPTIONS_KEY]["shopsanity"] == False: # Shop
            return
        
        locations_data = ctx.locations_info

        if len(locations_data) != len(all_parts):
            from CommonClient import logger
            # Scout location data for shop text updating purposes!
            parts_locations_to_scout: typing.List[int] = [get_location_id_for_shop_listing(part) for part in all_parts]
            await ctx.send_msgs([{
                "cmd": "LocationScouts",
                "locations": parts_locations_to_scout,
                "create_as_hint": 0
            }])
            logger.info("Parts location data scouted.\nIf shop names are incorrect, exit and enter shop again.")
            return
        
        # Check if the data needs to be overwritten (Write in a junk value for checking)
        first_part_char_check: int = int.from_bytes((await bizhawk.read(
            ctx.bizhawk_ctx, [(Constants.PARTS_TEXT_CHANGE_VERIFY_OFFSET, 1, MAIN_RAM)]
            ))[0])
        
        if first_part_char_check != 0x40:
            return
        
        first_part_char_check = 0x4A

        await bizhawk.write(ctx.bizhawk_ctx, [(
                Constants.PARTS_TEXT_CHANGE_VERIFY_OFFSET,
                [first_part_char_check],
                MAIN_RAM
            )])

        # 12 Character max for new item names
        # Descriptions can have 36 characters per line and have two lines with '8' point font. ; is newline marker
        # Description starts with ~^num before text which defines font size. We'll use ~^8 for now (7E 5E 38)
        # playernames's itemname;itemtype (red colour for progression)

        # Take item name and truncate if necessary
        for counter, part in enumerate(all_parts_data_order):
            location_info = locations_data[get_location_id_for_shop_listing(part)]
            player_name: str = ctx.player_names[location_info.player]
            item_name: str = ctx.item_names.lookup_in_slot(location_info.item, location_info.player)
            item_type_flags: int = location_info.flags
            item_type: str
            if item_type_flags & ItemClassification.progression == ItemClassification.progression:
                item_type = "@1(Progression)"
            elif item_type_flags & ItemClassification.filler == ItemClassification.filler:
                item_type = "@0(Filler)"
            elif item_type_flags & ItemClassification.trap == ItemClassification.trap:
                item_type = "@0(Trap)"
            else:
                item_type = "@0(Useful)"

            # Description

            # Maximum length for a slot name in AP is 16 characters (I'm going to truncate to 16 as well)
            # Then item name needs to be truncated to 36 - (nameLength+3) length
            player_name = player_name[:16]
            item_name_length: int = 36 - len(player_name) + 3
            desc_item_name = item_name[:item_name_length]

            description_top: str = f"~^8{player_name}'s {desc_item_name}"
            description_bottom: str = f";{item_type}"
            if len(description_bottom) < 36:
                repeat: int = 36 - len(description_bottom)
                name_filler: str = "\0" * repeat
                description_bottom += name_filler
            description: str = description_top + description_bottom
            description_as_hex: typing.List[int] = []
            for i in range(0, len(description)):
                description_as_hex.append(description[i].encode('utf-8')[0])

            await bizhawk.guarded_write(ctx.bizhawk_ctx, [(
                    Constants.PARTS_DESCRIPTIONS_OFFSET + (0x4E * counter),
                    description_as_hex,
                    MAIN_RAM
                )],[(
                    Constants.PARTS_TEXT_CHANGE_VERIFY_OFFSET,
                    [first_part_char_check],
                    MAIN_RAM
                )])

        # Take item name and truncate if necessary
        for counter, part in enumerate(all_parts):
            location_info = locations_data[get_location_id_for_shop_listing(part)]
            item_name: str = ctx.item_names.lookup_in_slot(location_info.item, location_info.player)

            # Shop Listing Name
            listing_name: str = item_name[:12]
            if len(listing_name) < 12:
                repeat: int = 12 - len(listing_name)
                name_filler: str = "\0" * repeat
                listing_name += name_filler
            listing_as_hex: typing.List[int] = []
            for i in range(0, len(listing_name)):
                listing_as_hex.append(listing_name[i].encode('utf-8')[0])

            await bizhawk.guarded_write(ctx.bizhawk_ctx, [(
                    Constants.PARTS_NAMES_OFFSETS[counter],
                    listing_as_hex,
                    MAIN_RAM
                )],[(
                    Constants.PARTS_TEXT_CHANGE_VERIFY_OFFSET,
                    [first_part_char_check],
                    MAIN_RAM
                )])

    # Update shop item and description text when shopsanity is active
    async def shopsanity_update_garage_text(self, ctx: "BizHawkClientContext", menu_section) -> None:
        if menu_section != 0 or ctx.slot_data[Constants.GAME_OPTIONS_KEY]["shopsanity"] == False: # Shop
            return
        
        # Check if the data needs to be overwritten (Write in a junk value for checking)
        first_part_char_check: int = int.from_bytes((await bizhawk.read(
            ctx.bizhawk_ctx, [(Constants.PARTS_TEXT_CHANGE_VERIFY_OFFSET, 1, MAIN_RAM)]
            ))[0])
        
        if first_part_char_check != 0x4A:
            return
        
        first_part_char_check = 0x40

        await bizhawk.write(ctx.bizhawk_ctx, [(
                Constants.PARTS_TEXT_CHANGE_VERIFY_OFFSET,
                [first_part_char_check],
                MAIN_RAM
            )])

        # 12 Character max for new item names

        # Take item name and truncate if necessary
        for counter, part in enumerate(all_parts):
            item_name: str = part.name

            # Shop Listing Name
            listing_name: str = item_name[:12]
            if len(listing_name) < 12:
                repeat: int = 12 - len(listing_name)
                name_filler: str = "\0" * repeat
                listing_name += name_filler
            listing_as_hex: typing.List[int] = []
            for i in range(0, len(listing_name)):
                listing_as_hex.append(listing_name[i].encode('utf-8')[0])

            await bizhawk.guarded_write(ctx.bizhawk_ctx, [(
                    Constants.PARTS_NAMES_OFFSETS[counter],
                    listing_as_hex,
                    MAIN_RAM
                )],[(
                    Constants.PARTS_TEXT_CHANGE_VERIFY_OFFSET,
                    [first_part_char_check],
                    MAIN_RAM
                )])

    # Store the number of successfully completed missions into story progress (For certain Mail's to appear)
    async def force_update_mission_count(self, ctx: "BizHawkClientContext", in_menu) -> None:
        if not in_menu:
            return []
        completed_sorties_byte: typing.int = (await bizhawk.read(
            ctx.bizhawk_ctx, [(Constants.SUCCESSFUL_SORTIES_COUNT_OFFSET, 1, MAIN_RAM)]
            ))[0]
        await bizhawk.write(ctx.bizhawk_ctx, [(
                    Constants.STORY_PROGRESS_OFFSET,
                    [int.from_bytes(completed_sorties_byte)],
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

            # Find out if we are in the Ravens Nest Menu
            # Timing matters less on this than it does for the menu_section_check 
            # (which is right before the function that needs it)
            in_menu: bool = await self.ravens_nest_menu_check(ctx)

            # Blanks the entire shop at the start of the run so it can be properly updated (if shopsanity is on)
            await self.shopsanity_initialization(ctx, in_menu)

            # Force update a value to properly count completed missions
            await self.force_update_mission_count(ctx, in_menu)

            # Read mission completion locations
            completed_missions_flags: typing.List[bool] = await self.read_mission_completion(ctx, in_menu)

            # Read mail read locations
            read_mail_flags: typing.List[bool] = await self.read_mail_read_flags(ctx, in_menu)

            # Items received handling

            # Find out what ravens nest menu section we're in
            menu_section: int = await self.ravens_nest_menu_section_check(ctx)
            # Unlock missions based on what has been received
            await self.update_mission_list_code(ctx, menu_section)
            # Update shop listings text if we're in the shop
            await self.shopsanity_update_shop_text(ctx, menu_section)
            # Update part names in the Garage (fix them from opening shop)
            await self.shopsanity_update_garage_text(ctx, menu_section)

            # Credits handling
            await self.award_credits(ctx, in_menu)

            # Human+ handling
            await self.award_humanplus(ctx, in_menu)

            # Shopsanity handling
            await self.award_shop_listings(ctx, completed_missions_flags.count(True), in_menu)

            # Parts handling
            await self.award_parts(ctx)

            # Local checked checks handling

            new_local_check_locations: typing.Set[int]

            missions_to_completed: typing.Dict[Mission, bool] = {
                m: c for m, c in zip(all_missions, completed_missions_flags)
            }

            mail_been_read: typing.Dict[Mail, bool] = {
                m: c for m, c in zip(all_mail, read_mail_flags)
            }

            items_purchased: typing.Dict[Part, bool] = await self.check_purchased_items(ctx, completed_missions_flags.count(True), in_menu)

            new_local_check_locations = set([
                get_location_id_for_mission(key) for key, value in missions_to_completed.items() if value
            ])

            new_local_check_locations = new_local_check_locations.union(set([
                get_location_id_for_mail(key) for key, value in mail_been_read.items() if value
            ]))

            new_local_check_locations = new_local_check_locations.union(set([
                get_location_id_for_shop_listing(key) for key, value in items_purchased.items()
            ]))

            # Award game completion if in missionsanity mode and you've reached the mission goal threshold
            if ctx.slot_data[Constants.GAME_OPTIONS_KEY]["goal"] == 0: # Missionsanity
                if completed_missions_flags.count(True) == ctx.slot_data[Constants.GAME_OPTIONS_KEY]["missionsanity_goal_requirement"] + 1:
                    new_local_check_locations.add(Constants.VICTORY_LOCATION_ID)

            if new_local_check_locations != self.local_checked_locations:
                self.local_checked_locations = new_local_check_locations
                if new_local_check_locations is not None:
                    await ctx.send_msgs([{
                        "cmd": "LocationChecks",
                        "locations": list(new_local_check_locations)
                    }])