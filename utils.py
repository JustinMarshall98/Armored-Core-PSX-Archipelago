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
    SHOPSANITY_TRACKING_OFFSET: int = 0x48663 # We are comandeering the VS Stage option memory for this!
    PLAYER_CREDITS_OFFSET: int = 0x39CA4 # Data is 4 byte size, signed integer. Min max should be +/- 99,999,999.
    HUMANPLUS_LEVEL_OFFSET: int = 0x039D20 # Data is 1 byte size. The three levels are 01/04/06
    PROGRESSIVE_HUMANPLUS_ITEM_NAME: str = "Progressive Human+"
    PROGRESSIVE_HUMANPLUS_ITEM_ID: int = 0x4
    MAIL_RECEPTION_OFFSET: int = 0x17F6D0 # Data is 1 Byte
    STORY_PROGRESS_OFFSET: int = 0x1F3752 # Data is 1 Byte
    SUCCESSFUL_SORTIES_COUNT_OFFSET: int = 0x1F3780 # Data is 1 Byte
    SHOP_INVENTORY_OFFSET: int = 0x031B34 # Data is 1 Byte
    PARTS_INVENTORY_OFFSET: int = 0x031A94 # Data is 1 Byte


    FREESPACE_CODE_OFFSET: int = 0x17f860 # Used for Mission List modification, it's actually where Mail names are stored lol (but we guarded write to prevent Mail from getting messed up)
    MISSION_MENU_HOOK_OFFSET: int = 0x87218 # Used to hack into mission list display routine
    MENU_CURRENT_SELECTION1_OFFSET: int = 0x1A2836 # 1A2837. IE Mail is 0x04, 1A2766,1A2767. 20 or E0 in second values must be checked? WHY is this location moving around ugh
    MENU_CURRENT_SELECTION1_VERIFY_OFFSET: int = 0x1A2837 # 20 or E0 to verify we can use the above offset
    MENU_CURRENT_SELECTION2_OFFSET: int = 0x1A2766 # This data moves around, this is the second possible location for it (plus its verifier)
    MENU_CURRENT_SELECTION2_VERIFY_OFFSET: int = 0x1A2767
    MENU_LOADED_VERIFY_OFFSET1: int = 0x1A2728
    MENU_LOADED_VERIFY_OFFSET2: int = 0x1A27F8
    SHOP_SELL_INTERCEPT_OFFSETS: typing.Tuple[int, ...] = (
        0x0952B4,
        0x0952CC,
        0x095220,
        0x095230,
    ) # For removing the Sell option
    SHOP_SELL_TEXT__OFFSET: int = 0x04CC25
    PARTS_DESCRIPTIONS_OFFSET: int = 0x19C360 # Each entry is 0x4E apart
    PARTS_TEXT_CHANGE_VERIFY_OFFSET: int = 0x19F02B # Expected value is 0x40
    PARTS_NAMES_OFFSETS: typing.Tuple[int, ...] = ( # This is so awful lol. all_parts changed to match this order
        0x0B91F4, # Head
        0x0B9230,
        0x0B926C,
        0x0B92A8,
        0x0B92E4,
        0x0B9320,
        0x0B935C,
        0x0B9398,
        0x0B93D4,
        0x0B9410,
        0x0B944C, # Core
        0x0B9484,
        0x0B94BC,
        0x0B94F4, # Leg
        0x0B953C,
        0x0B9584,
        0x0B95CC,
        0x0B9614,
        0x0B965C,
        0x0B96A4,
        0x0B96EC,
        0x0B9734,
        0x0B977C,
        0x0B97C4,
        0x0B980C,
        0x0B9854,
        0x0B989C,
        0x0B98E4,
        0x0B992C,
        0x0B9974,
        0x0B99BC,
        0x0B9A04,
        0x0B9A4C,
        0x0B9A94,
        0x0B9ADC,
        0x0B9B24,
        0x0B9B6C,
        0x0B9BB4,
        0x0B9BFC,
        0x0B9C44,
        0x0B9C8C,
        0x0B9CD4,
        0x0B9D1C,
        0x0B9D64,
        0x0B9DAC,
        0x0B9DF4, # Arms
        0x0B9E28,
        0x0B9E5C,
        0x0B9E90,
        0x0B9EC4,
        0x0B9EF8,
        0x0B9F2C,
        0x0B9F60,
        0x0B9F94,
        0x0B9FC8,
        0x0B9FFC,
        0x0BA030,
        0x0BA064,
        0x0BA098,
        0x0BA0CC,
        0x0BA100,
        0x0BA134, #Arm Weapon R
        0x0BA160,
        0x0BA18C,
        0x0BA1B8,
        0x0BA1E4,
        0x0BA210,
        0x0BA23C,
        0x0BA268,
        0x0BA294,
        0x0BA2C0,
        0x0BA2EC,
        0x0BA318,
        0x0BA344,
        0x0BA370,
        0x0BA39C,
        0x0BA3C8,
        0x0BA3F4, # Back Weapon
        0x0BA428,
        0x0BA45C,
        0x0BA490,
        0x0BA4C4,
        0x0BA4F8,
        0x0BA52C,
        0x0BA560,
        0x0BA594,
        0x0BA5C8,
        0x0BA5FC,
        0x0BA630,
        0x0BA664,
        0x0BA698,
        0x0BA6CC,
        0x0BA700,
        0x0BA734,
        0x0BA768,
        0x0BA79C,
        0x0BA7D0,
        0x0BA804,
        0x0BA838,
        0x0BA86C,
        0x0BA8A0,
        0x0BA8D4,
        0x0BA908,
        0x0BA93C,
        0x0BA970,
        0x0BA9A4,
        0x0BA9D8,
        0x0BAA0C,
        0x0BAA40,
        0x0BAA74,
        0x0BAAA8,
        0x0BAADC, #Arm Weapon L's
        0x0BAB10,
        0x0BAB44,
        0x0BAB78,
        0x0BABAC,
        0x0BABDC, #Boosters
        0x0BAC0C,
        0x0BAC3C,
        0x0BAC6C,
        0x0BAC9C,
        0x0BACCC, #fcs
        0x0BAD2C,
        0x0BAD8C,
        0x0BADEC,
        0x0BAE4C,
        0x0BAEAC,
        0x0BAF0C,
        0x0BAF6C,
        0x0BAFCC, #Generator
        0x0BAFFC,
        0x0BB02C,
        0x0BB05C,
        0x0BB08C,
        0x0BB0BC,
        0x0BB0EC,
        0x0BB11C, #option parts
        0x0BB148,
        0x0BB174,
        0x0BB1A0,
        0x0BB1CC,
        0x0BB1F8,
        0x0BB224,
        0x0BB250,
        0x0BB27C,
        0x0BB2A8,
        0x0BB2D4
    )
    

    GAME_OPTIONS_KEY: str = "g"