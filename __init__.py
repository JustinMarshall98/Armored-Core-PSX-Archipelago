import typing
import warnings

from worlds.AutoWorld import World, WebWorld
from BaseClasses import CollectionState, Region, Tutorial, LocationProgressType
from worlds.generic.Rules import set_rule

from .utils import Constants

class ACWeb(WebWorld):
    theme = "dirt"

    setup_en = Tutorial(
        "Multiworld Setup Guide",
        f"A guide to playing {Constants.GAME_NAME} with Archipelago.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Jumza"]
    )

    tutorials = [setup_en]

class ACWorld(World):
    """Armored Core is a 1997 third-person shooter mecha PSX game developed by FromSoftware."""
    game: str = Constants.GAME_NAME
    options_dataclass = ACOptions
    options: ACOptions
    required_client_version = (0, 5, 0)
    web = ACWeb()