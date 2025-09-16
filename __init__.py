import typing
import warnings
import random

from worlds.AutoWorld import World, WebWorld
from BaseClasses import CollectionState, Region, Tutorial, LocationProgressType
from worlds.generic.Rules import set_rule

from .client import ACClient
from .utils import Constants
from .mission import Mission, all_missions, STARTING_MISSION, DESTROY_FLOATING_MINES, id_to_mission as mission_id_to_mission, missions_that_award_credits
from .mail import Mail, all_mail
from .items import ACItem, create_item as fabricate_item, item_name_to_item_id, create_victory_event
from .locations import ACLocation, MissionLocation, get_location_name_for_mission, location_name_to_id as location_map, MailLocation, ShopLocation
from .options import ACOptions
from .parts import Part, all_parts, base_starting_parts, all_dummy_parts

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
    shop_listing_unlock_order: typing.List[Part]
    randomized_valid_parts_rewards: typing.List[Part] # Won't include Dummy or Starting Parts
    missions_awarding_credits: typing.List[Mission]

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
    """ Unused
    def get_available_shop_listings(self, state: CollectionState) -> typing.List[Part]:
        available_listings: typing.List[Part]
        for count, mission in enumerate(self.mission_unlock_order): # mission unlock order vs all_missions?
            start_index: int = count * self.options.shopsanity_listings_per_mission
            end_index: int = (((count + 1) * self.options.shopsanity_listings_per_mission) if ((count + 1) * self.options.shopsanity_listings_per_mission) < len(self.shop_listing_unlock_order) 
                                                                                            else len(self.shop_listing_unlock_order) - 1)
            if state.has(mission.name, self.player):
                for part in self.shop_listing_unlock_order[start_index : end_index]:
                    available_listings.append(part)
        return available_listings
    """ 
    def generate_early(self) -> None:
        self.mission_unlock_order = list(all_missions)
        if self.options.goal == 1: # Progressive Missions
            self.mission_unlock_order.sort(key = lambda m: m.progression_level)
        self.shop_listing_unlock_order = list(all_parts)
        random.shuffle(self.shop_listing_unlock_order)
        self.randomized_valid_parts_rewards = list((set(all_parts) - set(all_dummy_parts)) - set(base_starting_parts))
        random.shuffle(self.randomized_valid_parts_rewards)
        self.missions_awarding_credits = list(missions_that_award_credits)
    
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

        # Define mail locations
        for mail in all_mail:
            if mail.mission_unlock_id != -1: # It unlocks by doing a specific mission
                mail_location: MailLocation = MailLocation(mission_list_region, self.player, mail)
                set_rule(mail_location, (lambda state, m=mail_location:
                                         mission_id_to_mission[m.mail.mission_unlock_id] in self.get_available_missions(state)))
                mission_list_region.locations.append(mail_location)
            else: # It has a different unlock requirement. As of right now these can all be done Out Of Logic, but it leads to a better play pattern
                if mail.name == "New Parts Added (1)": # Unlocks after 10 missions are completed, so the rule is you must have at least 10 missions (should it be 9? Raven Test?)
                    mail_location: MailLocation = MailLocation(mission_list_region, self.player, mail)
                    set_rule(mail_location, lambda state: state.has_from_list([m.name for m in self.mission_unlock_order], self.player, 10))
                    mission_list_region.locations.append(mail_location)
                elif mail.name == "New Parts Added (2)": # Unlocks after 20 missions are completed, so the rule is you must have at least 20 missions (should it be 19? Raven Test?)
                    mail_location: MailLocation = MailLocation(mission_list_region, self.player, mail)
                    set_rule(mail_location, lambda state: state.has_from_list([m.name for m in self.mission_unlock_order], self.player, 20))
                    mission_list_region.locations.append(mail_location)
                else: #mail.name == "Human Plus": # Unlocks after 13 missions are completed, so the rule is you must have at least 13 missions (should it be 12? Raven Test?)
                    mail_location: MailLocation = MailLocation(mission_list_region, self.player, mail)
                    set_rule(mail_location, lambda state: state.has_from_list([m.name for m in self.mission_unlock_order], self.player, 13))
                    mission_list_region.locations.append(mail_location)

        # Define Shop Listings locations
        print([m.name for m in missions_that_award_credits])
        for count, mission in enumerate(self.mission_unlock_order):
            start_index: int = count * self.options.shopsanity_listings_per_mission
            end_index: int = (((count + 1) * self.options.shopsanity_listings_per_mission) if ((count + 1) * self.options.shopsanity_listings_per_mission) < len(self.shop_listing_unlock_order) 
                                                                                            else len(self.shop_listing_unlock_order) - 1)
            for part in self.shop_listing_unlock_order[start_index : end_index]:
                shop_location: ShopLocation = ShopLocation(mission_list_region, self.player, part)
                # Shop rules are such that the player has the missions needed to unlock them AND at least one mission that awards credits available
                set_rule(shop_location, lambda state, c = count: state.has_from_list([m.name for m in self.mission_unlock_order], self.player, c) and 
                                                        state.has_from_list([m.name for m in self.missions_awarding_credits], self.player, 1))
                #print(f"{count} {part.name} {mission.name}")
                #set_rule(shop_location, lambda state, c = count: state.has_from_list([m.name for m in self.mission_unlock_order], self.player, c))
                mission_list_region.locations.append(shop_location)

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

        # Human+ generates first if the option is on
        if self.options.include_humanplus:
            humanplus_slots: int = 3 if filler_slots > 3 else filler_slots
            itempool += [self.create_item(Constants.PROGRESSIVE_HUMANPLUS_ITEM_NAME) for h in range(humanplus_slots)][:humanplus_slots]
        filler_slots = filler_slots - humanplus_slots

        # Then parts if shopsanity is on
        if self.options.shopsanity:
            valid_parts_rewards_count: int = len(self.randomized_valid_parts_rewards)
            shopsanity_slots: int = valid_parts_rewards_count if filler_slots > valid_parts_rewards_count else filler_slots
            itempool += [self.create_item(p.name) for p in self.randomized_valid_parts_rewards[:shopsanity_slots]][:shopsanity_slots] 
            # Note to self, list slice should be redundant, but ensures the added amount of items doesn't exceed the length of shopsanity_slots
        filler_slots = filler_slots - shopsanity_slots
        
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