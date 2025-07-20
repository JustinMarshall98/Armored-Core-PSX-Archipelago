import typing
import warnings

from worlds.AutoWorld import World, WebWorld
from BaseClasses import CollectionState, Region, Tutorial, LocationProgressType
from worlds.generic.Rules import set_rule

from .client import ACClient
from .utils import Constants
from .mission import Mission, all_missions, STARTING_MISSION, VICTORY_MISSION
from .items import ACItem, create_item as fabricate_item, item_name_to_item_id, create_victory_event
from .locations import MissionLocation, get_location_name_for_mission, location_name_to_id as location_map
from .options import ACOptions, GoalRequirement

class ACWeb(WebWorld):
    theme = "dirt"

    setup_en = Tutorial(
        "Multiworld Setup Guide",
        f"A guide to playing {Constants.GAME_NAME} with Archipelago.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Jumza"]
    )

    tutorials = [setup_en]

class ACWorld(World):
    """Armored Core is a 1997 third-person shooter mecha PSX game developed by FromSoftware."""
    game: str = Constants.GAME_NAME
    options_dataclass = ACOptions
    options: ACOptions
    required_client_version = (0, 5, 0)
    web = ACWeb()

    location_name_to_id = location_map
    item_name_to_id = item_name_to_item_id

    mission_unlock_order: typing.List[Mission]

    def get_available_missions(self, state: CollectionState) -> typing.List[Mission]:
        available_missions: typing.List[Mission] = [STARTING_MISSION] # Dummy00 is always available
        for m in self.mission_unlock_order:
            if m is not STARTING_MISSION:
                if state.has(m.name, self.player):
                    available_missions.append(m)
        return available_missions
    
    def generate_early(self) -> None:
        self.mission_unlock_order = all_missions
    
    def create_item(self, name: str) -> ACItem:
        return fabricate_item(name, self.player)
    
    def create_regions(self) -> None:
        menu_region = Region("Menu", self.player, self.multiworld)

        mission_list_region = Region("Mission List", self.player, self.multiworld)

        for mission in self.mission_unlock_order:
            if mission.name != Constants.VICTORY_MISSION_NAME:
                mission_location: MissionLocation = MissionLocation(mission_list_region, self.player, mission)
                set_rule(mission_location, (lambda state, m=mission_location:
                                            m.mission in self.get_available_missions(state)))
                mission_list_region.locations.append(mission_location)

        self.multiworld.completion_condition[self.player] = lambda state: state.has(
            Constants.VICTORY_ITEM_NAME, self.player
        )

        itempool: typing.List[ACItem] = []
        for mission in self.mission_unlock_order:
            if mission is not STARTING_MISSION and mission.name != Constants.VICTORY_MISSION_NAME:
                itempool.append(self.create_item(mission.name))

        # Generate filler
        # Basically dummied out 'credit' while testing world gen

        filler_slots: int = len(mission_list_region.locations) - len(itempool)
        itempool += [self.create_item("Credit") for c in range(filler_slots)][:filler_slots]

        # Set Destroy Floating Mines Completed as goal item

        destroy_floating_mines_location: MissionLocation = MissionLocation(mission_list_region, self.player, VICTORY_MISSION)
        mission_completion_names: typing.List[str] = []
        for m in self.mission_unlock_order:
            if m is not VICTORY_MISSION:
                mission_completion_names.append(get_location_name_for_mission(m))
        # Destroy Floating Mines will appear after the number of missions specified have been completed
        set_rule(destroy_floating_mines_location, lambda state: state.has_from_list([m.name for m in self.mission_unlock_order], self.player, self.options.goal_requirement))
        destroy_floating_mines_location.place_locked_item(create_victory_event(self.player))
        mission_list_region.locations.append(destroy_floating_mines_location)

        self.multiworld.itempool.extend(itempool)

        menu_region.connect(mission_list_region)
        self.multiworld.regions.append(mission_list_region)
        self.multiworld.regions.append(menu_region)

    def fill_slot_data(self) -> typing.Dict[str, typing.Any]:
        return {
            #Whatever options we need the client to know
        }