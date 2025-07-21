import typing

class Mission:
    id: int
    name: str
    story_level: int

    def __init__(self, _id: int, name: str, story_level: int):
        self.id = _id
        self.name = name
        self.story_level = story_level

    def __str__(self) -> str:
        return (
            f"{self.name} "
        )
    
# Unused missions (outside of Dummy00) are omitted from this list
all_missions: typing.Tuple[Mission, ...] = (
    Mission(0x0, "Raven Test", 0), # Named Dummy00 in game, name changed for player clarity
    Mission(0x1, "Stop Terrorist Threat", 6),
    Mission(0x2, "Remove Gun Emplacement", 5),
    Mission(0x3, "Rescue Survey Team", 7),
    Mission(0x4, "Terrorist Pursuit", 8),
    Mission(0x5, "Worker Robot Removal", 6),
    Mission(0x6, "Secret Factory Recon", 12),
    Mission(0x7, "Exterminate Organisms(1)", 14),
    Mission(0x8, "Guard Freight Train", 10),
    Mission(0x9, "Destroy Fuel Depot", 9),
    Mission(0xa, "Prototype MT Test(1)", 11),
    Mission(0xb, "Guard Airplane", 17),
    Mission(0xc, "Stop Gas Exposure", 20),
    Mission(0xd, "Prototype MT Test(2)", 16),
    Mission(0xe, "Repulse Enemy Attack", 14),
    Mission(0xf, "Exterminate Organisms(2)", 21),
#   Mission(0x10, "16 Omitted", 0),
    Mission(0x11, "Guard Wharf Warehouse", 13),
    Mission(0x12, "Remove Base Occupants", 19),
    Mission(0x13, "Destroy Space Catapult", 21),
    Mission(0x14, "Destroy Base Generator", 23),
    Mission(0x15, "Mop Up Chrome Remnants(1)", 24),
    Mission(0x16, "Destroy \"Justice\"", 23),
    Mission(0x17, "Chrome Uprising", 23),
    Mission(0x18, "Destroy Plus Escapee", 14),
    Mission(0x19, "Destroy Intruders", 21),
    Mission(0x1a, "Destroy Plane Computer", 16),
    Mission(0x1b, "AC Battle(1)", 18),
    Mission(0x1c, "Attack Urban Center", 9),
#   Mission(0x1d, "29 Omitted", 0),
    Mission(0x1e, "Eliminate Squatters(1)", 1),
    Mission(0x1f, "Eliminate Squatters(2)", 5),
    Mission(0x20, "Destroy Unknown MTs", 2),
    Mission(0x21, "Rescue Transport Truck", 4),
    Mission(0x22, "Eliminate Strikers", 1),
    Mission(0x23, "Stop Security MTs", 3),
    Mission(0x24, "Stop Gang, \"Dark Soul\"", 13),
    Mission(0x25, "Reclaim Oil Facility", 2),
    Mission(0x26, "Recover Capsules", 15),
#   Mission(0x27, "39 Omitted", 0),
    Mission(0x28, "Guard Factory Entrance", 12),
    Mission(0x29, "Capture Space Station", 22),
    Mission(0x2a, "Release Organisms", 18),
    Mission(0x2b, "Retake Air Cleaner", 22),
    Mission(0x2c, "Kill \"Struggle\" Leader", 18),
    Mission(0x2d, "Stop Security MT", 13),
    Mission(0x2e, "Destroy Base Computer", 17),
    Mission(0x2f, "Mop Up Chrome Remnants(2)", 24),
    Mission(0x30, "Destroy Floating Mines", 26),
#   Mission(0x31, "Destruction of Ravens", 27),
    Mission(0x32, "AC Battle(2)", 25)
#   Mission(0x33, "~~~~~~~~~", 0) etc
)

STARTING_MISSION = all_missions[0]
VICTORY_MISSION = all_missions[-2] # Destroy Floating Mines

id_to_mission = {mission.id: mission for mission in all_missions}
name_to_mission = {mission.name: mission for mission in all_missions}