import typing

class Mission:
    id: int
    name: str
    progression_level: int
    awards_credits: bool

    def __init__(self, _id: int, name: str, progression_level: int, awards_credits: bool):
        self.id = _id
        self.name = name
        self.progression_level = progression_level
        self.awards_credits = awards_credits

    def __str__(self) -> str:
        return (
            f"{self.name} "
        )
    
# Unused missions (outside of Dummy00) are omitted from this list
all_missions: typing.Tuple[Mission, ...] = (
    Mission(0x0, "Raven Test", 0, False), # Named Dummy00 in game, name changed for player clarity
    Mission(0x1, "Stop Terrorist Threat", 2, True),
    Mission(0x2, "Remove Gun Emplacement", 2, False),
    Mission(0x3, "Rescue Survey Team", 3, True),
    Mission(0x4, "Terrorist Pursuit", 3, True),
    Mission(0x5, "Worker Robot Removal", 2, True),
    Mission(0x6, "Secret Factory Recon", 4, True),
    Mission(0x7, "Exterminate Organisms(1)", 5, True),
    Mission(0x8, "Guard Freight Train", 3, True),
    Mission(0x9, "Destroy Fuel Depot", 3, True),
    Mission(0xa, "Prototype MT Test(1)", 4, True),
    Mission(0xb, "Guard Airplane", 6, True),
    Mission(0xc, "Stop Gas Exposure", 7, True),
    Mission(0xd, "Prototype MT Test(2)", 6, False),
    Mission(0xe, "Repulse Enemy Attack", 5, True),
    Mission(0xf, "Exterminate Organisms(2)", 7, True),
#   Mission(0x10, "16 Omitted", 0),
    Mission(0x11, "Guard Wharf Warehouse", 4, True),
    Mission(0x12, "Remove Base Occupants", 7, True),
    Mission(0x13, "Destroy Space Catapult", 8, True),
    Mission(0x14, "Destroy Base Generator", 8, True),
    Mission(0x15, "Mop Up Chrome Remnants(1)", 9, True),
    Mission(0x16, "Destroy \"Justice\"", 9, True),
    Mission(0x17, "Chrome Uprising", 9, True),
    Mission(0x18, "Destroy Plus Escapee", 5, True),
    Mission(0x19, "Destroy Intruders", 8, True),
    Mission(0x1a, "Destroy Plane Computer", 6, True),
    Mission(0x1b, "AC Battle(1)", 6, True),
    Mission(0x1c, "Attack Urban Center", 3, True),
#   Mission(0x1d, "29 Omitted", 0),
    Mission(0x1e, "Eliminate Squatters(1)", 1, True),
    Mission(0x1f, "Eliminate Squatters(2)", 2, True),
    Mission(0x20, "Destroy Unknown MTs", 1, True),
    Mission(0x21, "Rescue Transport Truck", 2, True),
    Mission(0x22, "Eliminate Strikers", 1, True),
    Mission(0x23, "Stop Security MTs", 1, True),
    Mission(0x24, "Stop Gang, \"Dark Soul\"", 4, False),
    Mission(0x25, "Reclaim Oil Facility", 1, True),
    Mission(0x26, "Recover Capsules", 5, True),
#   Mission(0x27, "39 Omitted", 0),
    Mission(0x28, "Guard Factory Entrance", 4, True),
    Mission(0x29, "Capture Space Station", 8, True),
    Mission(0x2a, "Release Organisms", 7, True),
    Mission(0x2b, "Retake Air Cleaner", 8, True),
    Mission(0x2c, "Kill \"Struggle\" Leader", 7, True),
    Mission(0x2d, "Stop Security MT", 5, True),
    Mission(0x2e, "Destroy Base Computer", 6, True),
    Mission(0x2f, "Mop Up Chrome Remnants(2)", 9, True),
    Mission(0x30, "Destroy Floating Mines", 10, True),
#   Mission(0x31, "Destruction of Ravens", 10),
    Mission(0x32, "AC Battle(2)", 9, True)
#   Mission(0x33, "~~~~~~~~~", 0) etc
)

STARTING_MISSION = all_missions[0]
DESTROY_FLOATING_MINES = all_missions[-2]

missions_that_award_credits: typing.Tuple[Mission, ...] = {mission for mission in all_missions if mission.awards_credits}

id_to_mission = {mission.id: mission for mission in all_missions}
name_to_mission = {mission.name: mission for mission in all_missions}