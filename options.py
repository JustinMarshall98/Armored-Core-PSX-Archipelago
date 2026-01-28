import typing
import dataclasses

from Options import Range, Choice, PerGameCommonOptions, DefaultOnToggle, Toggle as DefaultOffToggle
from dataclasses import dataclass

class Goal(Choice):
    """
    Choose what you want your goal to be.
    In missionsanity all missions are individually added to the pool of checks,
    you set the number of missions that you must complete in order to complete your goal.
    In progressive missions you receive 'progressive mission' items that unlock groups of
    5 missions at a time. Your goal is completing Destroy Floating Mines after collecting
    all 'progressive mission' items.
    """
    display_name = "Goal"
    option_missionsanity = 0
    option_progressive_missions = 1
    default = 1

class MissionsanityGoalRequirement(Range):
    """
    This option only matters if your Goal is Missionsanity.
    Select how many missions it takes to complete your goal.
    Does not include the tutorial mission.
    """
    display_name = "Missionsanity Goal Requirement"
    range_start = 1
    range_end = 46
    default = 46

class IncludeHumanPlusFiller(DefaultOnToggle):
    """
    If this option is on, three "Progressive Human+"
    Enhancement levels will be added as filler to the item pool.
    """
    display_name = "Include Human+ Filler"

class Shopsanity(DefaultOffToggle):
    """
    Shopsanity turns all parts listings in the shop into locations,
    and all parts that you don't start with are shuffled into the multiworld.
    """
    display_name = "Shopsanity"

class ShopsanityListingsPerMission(Range):
    """
    Define how many shop listings open up per mission completion.
    Higher numbers may require more grinding. Includes Raven Test.
    """
    display_name = "Shopsanity Listings Per Mission"
    range_start = 4
    range_end = 146
    default = 4

class RandomizeStartingParts(DefaultOffToggle):
    """
    Your starting AC Parts will be randomized but still
    adhere to weight and energy limits.
    """
    display_name = "Randomize Starting Mech"

class CreditCheckAmount(Range):
    """
    Define how much you earn from Credit Filler checks you receieve.
    """
    display_name = "Credit Check Amount"
    range_start = 100
    range_end = 100000
    default = 10000

@dataclass
class ACOptions(PerGameCommonOptions):
    goal: Goal
    missionsanity_goal_requirement: MissionsanityGoalRequirement
    include_humanplus: IncludeHumanPlusFiller
    shopsanity: Shopsanity
    shopsanity_listings_per_mission: ShopsanityListingsPerMission
    rando_start_parts: RandomizeStartingParts
    credit_check_amount: CreditCheckAmount

    def serialize(self) -> typing.Dict[str, int]:
        return {field.name: getattr(self, field.name).value for field in dataclasses.fields(self)}