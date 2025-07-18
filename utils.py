import typing

from dataclasses import dataclass

@dataclass
class Constants:
    # Armored Core constants
    GAME_NAME: str = "Armored Core"
    MISSION_LIST_MODE: int = 0x1F3754 # Data is 1 Byte
    MISSION_COMPLETION_OFFSET: int = 0x1F3788 # Data is 1 Byte each
    VICTORY_ITEM_NAME: str = "Destroy Floating Mines Completed"
    VICTORY_ITEM_ID: int = 0x1F37B8 # Data is 1 Byte