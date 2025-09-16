import typing

from BaseClasses import Item, ItemClassification
from .utils import Constants
from .mission import all_missions, name_to_mission
from .parts import all_parts, name_to_part

item_id_to_item_name: typing.Dict[int, str] = {}

# Mission unlock item ID's are the mission ID + mission completion offset
for mission in all_missions:
    item_id_to_item_name[mission.id + Constants.MISSION_COMPLETION_OFFSET] = mission.name

# Victory Item
item_id_to_item_name[Constants.VICTORY_ITEM_ID] = Constants.VICTORY_ITEM_NAME

# Progressive Missions
item_id_to_item_name[Constants.PROGRESSIVE_MISSION_ITEM_ID] = Constants.PROGRESSIVE_MISSION_ITEM_NAME

# Credit
item_id_to_item_name[Constants.CREDIT_ITEM_ID] = Constants.CREDIT_ITEM_NAME

# Progressive Human+
item_id_to_item_name[Constants.PROGRESSIVE_HUMANPLUS_ITEM_ID] = Constants.PROGRESSIVE_HUMANPLUS_ITEM_NAME

# Parts
for part in all_parts:
    if part.name != "DUMMY" and part.name != "NO WEAPON":
        item_id_to_item_name[part.id + Constants.PARTS_INVENTORY_OFFSET] = part.name #f"{part}"

# Reverse item_id_to_item_name
item_name_to_item_id: typing.Dict[str, int] = {value: key for key, value in item_id_to_item_name.items()}

class ACItem(Item):
    game: str = Constants.GAME_NAME

def create_item(name: str, player_id: int) -> ACItem:
    return ACItem(name, ItemClassification.progression if (name in name_to_mission or
                                                           name is Constants.PROGRESSIVE_MISSION_ITEM_NAME)
                      else ItemClassification.filler, item_name_to_item_id[name], player_id)

def create_victory_event(player_id: int) -> ACItem:
    return ACItem(Constants.VICTORY_ITEM_NAME, ItemClassification.progression, Constants.VICTORY_ITEM_ID, player_id)

def convert_item_id_to_mission_id(item_id: int) -> int:
    return item_id - Constants.MISSION_COMPLETION_OFFSET