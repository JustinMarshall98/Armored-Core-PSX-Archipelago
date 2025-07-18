import typing

from BaseClasses import Location, Region, LocationProgressType, Item
from .mission import Mission, all_missions
from .utils import Constants

def get_location_name_for_mission(mission: Mission) -> str:
    return f"{mission.name} Completed"

def get_location_id_for_mission_id(mission_id: int) -> int:
    return Constants.MISSION_COMPLETION_OFFSET + mission_id

def get_location_id_for_mission(mission: Mission) -> int:
    return get_location_id_for_mission_id(mission.id)

class ACLocation(Location):
    game: str

    def __init__(self, region: Region, player: int, name: str, id: int):
        super().__init__(player, name, parent=region)
        self.game = Constants.GAME_NAME
        self.address = id

    def exclude(self) -> None:
        self.progress_type = LocationProgressType.EXCLUDED

    def place(self, item: Item) -> None:
        self.item = item
        item.location = self

class MissionLocation(ACLocation):
    # Location for mission completion
    mission: Mission

    def __init__(self, region: Region, player: int, mission: Mission):
        super().__init__(region, player, get_location_name_for_mission(mission), get_location_id_for_mission(mission))
        self.mission = mission

mission_location_name_to_id: typing.Dict[str, int] = {}
for mission in all_missions:
    mission_location_name_to_id[get_location_name_for_mission(mission)] = get_location_id_for_mission(mission)

location_name_to_id: typing.Dict[str, int] = {**mission_location_name_to_id}