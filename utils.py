import typing

from dataclasses import dataclass

@dataclass
class Constants:
    # Armored Core constants
    GAME_NAME: str = "Armored Core"
    MISSION_LIST_MODE_OFFSET: int = 0x1F3754 # Data is 1 Byte
    MISSION_COMPLETION_OFFSET: int = 0x1F3788 # Data is 1 Byte each
    VICTORY_ITEM_NAME: str = "Destroy Floating Mines Completed"
    VICTORY_MISSION_NAME: str = "Destroy Floating Mines"
    VICTORY_ITEM_ID: int = 0x1F37B8 # Data is 1 Byte

    FREESPACE_CODE_OFFSET: int = 0x17f860 # Used for Mission List modification, it's actually where Mail names are stored lol (but we guarded write to prevent Mail from getting messed up)
    MISSION_MENU_HOOK_OFFSET: int = 0x87218 # Used to hack into mission list display routine
    MENU_CURRENT_SELECTION_OFFSET: int = 0x1A2836 # IE Mail is 0x04

    GAME_OPTIONS_KEY: str = "g"