import typing
import dataclasses

from Options import Range, Choice, PerGameCommonOptions, Toggle
from dataclasses import dataclass

class GoalRequirement(Range):
    """
    In this version the goal is always completing Destroy Floating Mines.
    Choose the number of missions that must be completed to unlock it.
    The tutorial mission is counted.
    """
    display_name = "Goal Requirement"
    range_start = 1
    range_end = 46
    default = 46

@dataclass
class ACOptions(PerGameCommonOptions):
    goal_requirement: GoalRequirement

    def serialize(self) -> typing.Dict[str, int]:
        return {field.name: getattr(self, field.name).value for field in dataclasses.fields(self)}