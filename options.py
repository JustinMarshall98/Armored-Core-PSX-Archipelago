import typing
import dataclasses

from Options import Range, Choice, PerGameCommonOptions, Toggle
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
    Includes the tutorial mission.
    (So if you set it to 1 and become a Raven, you will complete your goal)
    """
    display_name = "Missionsanity Goal Requirement"
    range_start = 1
    range_end = 47
    default = 47

@dataclass
class ACOptions(PerGameCommonOptions):
    goal: Goal
    missionsanity_goal_requirement: MissionsanityGoalRequirement

    def serialize(self) -> typing.Dict[str, int]:
        return {field.name: getattr(self, field.name).value for field in dataclasses.fields(self)}