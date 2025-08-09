import typing

from BaseClasses import Location, Region, LocationProgressType, Item
from .mission import Mission, all_missions, id_to_mission
from .utils import Constants
from .mail import Mail, all_mail, id_to_mail

def get_location_name_for_mission(mission: Mission) -> str:
    return f"{mission.name} Completed"

def get_location_id_for_mission_id(mission_id: int) -> int:
    return Constants.MISSION_COMPLETION_OFFSET + mission_id

def get_location_id_for_mission(mission: Mission) -> int:
    return get_location_id_for_mission_id(mission.id)

def is_mission_location_id(location_id: int) -> bool:
    return (location_id - Constants.MISSION_COMPLETION_OFFSET) in id_to_mission

def mission_from_location_id(location_id: int) -> Mission:
    return id_to_mission[location_id - Constants.MISSION_COMPLETION_OFFSET]


def get_location_name_for_mail(mail: Mail) -> str:
    return f"Mail - {mail.name}"

def get_location_id_for_mail_id(mail_id: int) -> int:
    return Constants.MAIL_RECEPTION_OFFSET + mail_id

def get_location_id_for_mail(mail: Mail) -> int:
    return get_location_id_for_mail_id(mail.id)


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

class MailLocation(ACLocation):
    # Location for having read Mail
    mail: Mail
    def __init__(self, region: Region, player: int, mail: Mail):
        super().__init__(region, player, get_location_name_for_mail(mail), get_location_id_for_mail(mail))
        self.mail = mail

mail_location_name_to_id: typing.Dict[str, int] = {}
for mail in all_mail:
    mail_location_name_to_id[get_location_name_for_mail(mail)] = get_location_id_for_mail(mail)

location_name_to_id: typing.Dict[str, int] = {**mission_location_name_to_id, **mail_location_name_to_id}