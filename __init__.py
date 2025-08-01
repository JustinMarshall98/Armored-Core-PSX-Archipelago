import typing
import warnings

from worlds.AutoWorld import World, WebWorld
from BaseClasses import CollectionState, Region, Tutorial, LocationProgressType
from worlds.generic.Rules import set_rule

from .client import ACClient
from .utils import Constants
from .mission import Mission, all_missions, STARTING_MISSION, DESTROY_FLOATING_MINES
from .items import ACItem, create_item as fabricate_item, item_name_to_item_id, create_victory_event
from .locations import ACLocation, MissionLocation, get_location_name_for_mission, location_name_to_id as location_map
from .options import ACOptions

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
        if self.options.goal == 0: # Missionsanity
            for m in self.mission_unlock_order:
                if m is not STARTING_MISSION:
                    if state.has(m.name, self.player):
                        available_missions.append(m)
        else: # Progressive Missions
            for m in self.mission_unlock_order:
                if m is not STARTING_MISSION:
                    # Progression level - 1 because in this mode we always start with the first 5 missions
                    if state.count(Constants.PROGRESSIVE_MISSION_ITEM_NAME, self.player) >= (m.progression_level - 1):
                        available_missions.append(m)
        return available_missions
    
    def generate_early(self) -> None:
        self.mission_unlock_order = list(all_missions)
        if self.options.goal == 1: # Progressive Missions
            self.mission_unlock_order.sort(key = lambda m: m.progression_level)
    
    def create_item(self, name: str) -> ACItem:
        return fabricate_item(name, self.player)
    
    def create_regions(self) -> None:
        menu_region = Region("Menu", self.player, self.multiworld)

        mission_list_region = Region("Mission List", self.player, self.multiworld)

        # Define mission locations. Changes slightly based on goal

        # Missionsanity Goal
        if self.options.goal == 0:
            for mission in self.mission_unlock_order:
                mission_location: MissionLocation = MissionLocation(mission_list_region, self.player, mission)
                set_rule(mission_location, (lambda state, m=mission_location:
                                            m.mission in self.get_available_missions(state)))
                mission_list_region.locations.append(mission_location)
        else: # Progressive Missions Goal
            for mission in self.mission_unlock_order:
                if mission is not DESTROY_FLOATING_MINES:
                    mission_location: MissionLocation = MissionLocation(mission_list_region, self.player, mission)
                    set_rule(mission_location, (lambda state, m=mission_location:
                                                    m.mission in self.get_available_missions(state)))
                    mission_list_region.locations.append(mission_location)

        self.multiworld.completion_condition[self.player] = lambda state: state.has(
            Constants.VICTORY_ITEM_NAME, self.player
        )

        itempool: typing.List[ACItem] = []
        if self.options.goal == 0: # Missionsanity
            for mission in self.mission_unlock_order:
                if mission is not STARTING_MISSION:
                    itempool.append(self.create_item(mission.name))
        else: # Progressive Missions
            for i in range(9): # Hardcoded number of Progressive Mission items currently
                itempool.append(self.create_item(Constants.PROGRESSIVE_MISSION_ITEM_NAME))

        # Generate filler

        filler_slots: int = len(mission_list_region.locations) - len(itempool)

        # Human+ generates before credit filler if the option is on
        if self.options.include_humanplus:
            humanplus_slots: int = 3 if filler_slots > 3 else filler_slots
            itempool += [self.create_item(Constants.PROGRESSIVE_HUMANPLUS_ITEM_NAME) for h in range(humanplus_slots)][:humanplus_slots]
        
        filler_slots = filler_slots - humanplus_slots
        # Credit checks (5000)
        itempool += [self.create_item(Constants.CREDIT_ITEM_NAME) for c in range(filler_slots)][:filler_slots]

        # Set Goal item location

        if self.options.goal == 0: # Missionsanity
            mission_threshold_location: ACLocation = ACLocation(mission_list_region, self.player, Constants.VICTORY_LOCATION_NAME, Constants.VICTORY_LOCATION_ID)
            # The player wins after beating a number of mission determined in yaml (missionsanity_goal_requirement)
            set_rule(mission_threshold_location, lambda state: state.has_from_list([m.name for m in self.mission_unlock_order], self.player, self.options.missionsanity_goal_requirement))
            mission_threshold_location.place_locked_item(create_victory_event(self.player))
            mission_list_region.locations.append(mission_threshold_location)
        else: # Progressive Missions
            destroy_floating_mines_location: MissionLocation = MissionLocation(mission_list_region, self.player, DESTROY_FLOATING_MINES)
            # Destroy Floating Mines will appear after receiving 9 progressive mission items
            set_rule(destroy_floating_mines_location, lambda state: state.count(Constants.PROGRESSIVE_MISSION_ITEM_NAME, self.player) == 9)
            destroy_floating_mines_location.place_locked_item(create_victory_event(self.player))
            mission_list_region.locations.append(destroy_floating_mines_location)

        self.multiworld.itempool.extend(itempool)

        menu_region.connect(mission_list_region)
        self.multiworld.regions.append(mission_list_region)
        self.multiworld.regions.append(menu_region)

    def fill_slot_data(self) -> typing.Dict[str, typing.Any]:
        return {
            Constants.GAME_OPTIONS_KEY: self.options.serialize()
        }