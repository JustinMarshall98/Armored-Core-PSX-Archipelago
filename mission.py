import typing

class Mission:
    id: int
    name: str

    def __init__(self, _id: int, name: str):
        self.id = _id
        self.name = name

    def __str__(self) -> str:
        return (
            f"{self.name} "
        )
    
# Unused missions (outside of Dummy00) are omitted from this list
all_missions: typing.Tuple[Mission, ...] = (
    Mission(0, "Dummy00"),
    Mission(1, "Stop Terrorist Threat"),
    Mission(2, "Remove Gun Emplacement"),
    Mission(3, "Rescue Survey Team"),
    Mission(4, "Terrorist Pursuit"),
    Mission(5, "Worker Robot Removal"),
    Mission(6, "Secret Factory Recon"),
    Mission(7, "Exterminate Organisms(1)"),
    Mission(8, "Guard Freight Train"),
    Mission(9, "Destroy Fuel Depot"),
    Mission(10, "Prototype MT Test(1)"),
    Mission(11, "Guard Airplane"),
    Mission(12, "Stop Gas Exposure"),
    Mission(13, "Prototype MT Test(2)"),
    Mission(14, "Repulse Enemy Attack"),
    Mission(15, "Exterminate Organisms(2)"),
#   Mission(16, "16 Omitted"),
    Mission(17, "Guard Wharf Warehouse"),
    Mission(18, "Remove Base Occupants"),
    Mission(19, "Destroy Space Catapult"),
    Mission(20, "Destroy Base Generator"),
    Mission(21, "Mop Up Chrom Remnants"),
    Mission(22, "Destroy \"Justice\""),
    Mission(23, "Chrome Uprising"),
    Mission(24, "Destroy Plus Escapee"),
    Mission(25, "Destroy Intruders"),
    Mission(26, "Destroy Plane Computer"),
    Mission(27, "AC Battle(1)"),
    Mission(28, "Attack Urban Center"),
#   Mission(29, "29 Omitted"),
    Mission(30, "Eliminate Squatters(1)"),
    Mission(31, "Eliminate Squatters(2)"),
    Mission(32, "Destroy Uknown MTs"),
    Mission(33, "Rescue Transport Truck"),
    Mission(34, "Eliminate Strikers"),
    Mission(35, "Stop Security MTs"),
    Mission(36, "Stop Gang, \"Dark Soul\""),
    Mission(37, "Reclaim Oil Facility"),
    Mission(38, "Recover Capsules"),
#   Mission(39, "39 Omitted"),
    Mission(40, "Guard Factory Entrance"),
    Mission(41, "Capture Space Station"),
    Mission(42, "Release Organisms"),
    Mission(43, "Retake Air Cleaner"),
    Mission(44, "Kill \"Struggle\" Leader"),
    Mission(45, "Stop Security MT"),
    Mission(46, "Destroy Base Computer"),
    Mission(47, "Mop Up Chrome Remnants"),
    Mission(48, "Destroy Floating Mines"),
#   Mission(49, "Destruction of Ravens"),
    Mission(50, "AC Battle")
#   Mission(51, "~~~~~~~~~") etc
)

id_to_mission = {mission.id: mission for mission in all_missions}
name_to_mission = {mission.name: mission for mission in all_missions}