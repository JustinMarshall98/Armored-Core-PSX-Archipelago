import typing

from dataclasses import dataclass

@dataclass
class Constants:
    # Armored Core constants
    GAME_NAME: str = "Armored Core"
    MISSION_LIST_MODE_OFFSET: int = 0x1F3754 # Data is 1 Byte
    MISSION_COMPLETION_OFFSET: int = 0x1F3788 # Data is 1 Byte each
    VICTORY_ITEM_NAME: str = "Armored Core Goal"
    VICTORY_LOCATION_NAME: str = "Armored Core Completed"
    VICTORY_ITEM_ID: int = 0x1
    VICTORY_LOCATION_ID: int = 0x1
    PROGRESSIVE_MISSION_ITEM_NAME: str = "Progressive Mission"
    PROGRESSIVE_MISSION_ITEM_ID: int = 0x2
    CREDIT_ITEM_NAME: str = "5000 Credits" # Hardcoded currently
    CREDIT_ITEM_ID: int = 0x3
    CREDIT_ITEMS_RECEIVED_OFFSET: int = 0x48664 # We are commandeering the VS Time Limit option memory for this! Sticks in save file
    PLAYER_CREDITS_OFFSET: int = 0x39CA4 # Data is 4 byte size, signed integer. Min max should be +/- 99,999,999.
    HUMANPLUS_LEVEL_OFFSET: int = 0x039D20 # Data is 1 byte size. The three levels are 01/04/06
    PROGRESSIVE_HUMANPLUS_ITEM_NAME: str = "Progressive Human+"
    PROGRESSIVE_HUMANPLUS_ITEM_ID: int = 0x4
    MAIL_RECEPTION_OFFSET: int = 0x17F6D0 # Data is 1 Byte


    FREESPACE_CODE_OFFSET: int = 0x17f860 # Used for Mission List modification, it's actually where Mail names are stored lol (but we guarded write to prevent Mail from getting messed up)
    MISSION_MENU_HOOK_OFFSET: int = 0x87218 # Used to hack into mission list display routine
    MENU_CURRENT_SELECTION1_OFFSET: int = 0x1A2836 # 1A2837. IE Mail is 0x04, 1A2766,1A2767. 20 or E0 in second values must be checked? WHY is this location moving around ugh
    MENU_CURRENT_SELECTION1_VERIFY_OFFSET: int = 0x1A2837 # 20 or E0 to verify we can use the above offset
    MENU_CURRENT_SELECTION2_OFFSET: int = 0x1A2766 # This data moves around, this is the second possible location for it (plus its verifier)
    MENU_CURRENT_SELECTION2_VERIFY_OFFSET: int = 0x1A2767
    

    GAME_OPTIONS_KEY: str = "g"