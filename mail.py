import typing

class Mail:
    id: int
    name: str
    #mission_unlock: mission

    def __init__(self, _id: int, name: str):
        self.id = _id
        self.name = name

    def __str__(self) -> str:
        return (
            f"{self.name} "
        )
    
all_mail: typing.Tuple[Mail, ...] = (
    Mail(0x0, "To All New Ravens"), # Raven Test
    Mail(0x1, "Thanks"), # Remove Gun Emplacement
    Mail(0x2, "EERC"), # Rescue Survey Team
    Mail(0x3, "Factory Assault Report"), # Secret Factory Recon
    Mail(0x4, "Giant Organisms"), # Exterminate Organisms (1)
    Mail(0x5, "The Red AC"), # Guard Freight Train
    Mail(0x6, "Chemical-Dyne Co"), # Destroy Fuel Depot
    Mail(0x7, "???"), # Remove Base Occupants
    Mail(0x8, "Plus"), # Destroy Plus Escapee
    Mail(0x9, "Ranking Raven"), # Attack Urban Center
    Mail(0xa, "Terrorists in the Shadows"), # Eliminate Squatters (2)
    Mail(0xb, "Chrome and Murakumo"), # Eliminate Squatters (2)
    Mail(0xc, "Reclaiming the Facility"), # Reclaim Oil Facility
    Mail(0xd, "Struggle"), # Reclaim Oil Facility
    Mail(0xe, "Relics of the Past"), # Recover Capsules
    Mail(0xf, "Factory Affair Report"), # Guard Factory Entrance
    Mail(0x10, "Biological Weapons"), # Release Organisms
    Mail(0x11, "Imminent Storm's Demise"), # Retake Air Cleaner
    Mail(0x12, "Struggle's Demise"), # Kill "Struggle" Leader
    #Mail(0x1, ""), # 
    #Mail(0x1, ""), #
    # Extra parts mail not appearing in initial testing, linked to something other than mission complete flags?
    # One guide mentions 10 missions, maybe 10/20
)

id_to_mail = {mail.id: mail for mail in all_mail}
name_to_mail = {mail.name: mail for mail in all_mail}