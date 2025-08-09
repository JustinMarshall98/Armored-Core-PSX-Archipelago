import typing

class Mail:
    id: int
    name: str
    mission_unlock_id: int # Value is -1 if it is a special case (not tied to mission ID)

    def __init__(self, _id: int, name: str, unlock_id: int):
        self.id = _id
        self.name = name
        self.mission_unlock_id = unlock_id


    def __str__(self) -> str:
        return (
            f"{self.name} "
        )
    
all_mail: typing.Tuple[Mail, ...] = (
    Mail(0x0, "New Parts Added (1)", -1), # After doing 10 Missions
    Mail(0x1, "New Parts Added (2)", -1), # After doing 20 Missions
    Mail(0x2, "Human Plus", -1), # After doing 13(?) Missions
    Mail(0x3, "To All New Ravens", 0x0), # Raven Test
    Mail(0x4, "Reclaiming the Facility", 0x25), # Reclaim Oil Facility
    Mail(0x5, "Struggle", 0x25), # Reclaim Oil Facility
    Mail(0x6, "Terrorists in the Shadows", 0x1f), # Eliminate Squatters (2)
    Mail(0x7, "Chrome and Murakumo", 0x1f), # Eliminate Squatters (2)
    Mail(0x8, "Thanks", 0x2), # Remove Gun Emplacement
    Mail(0x9, "Ranking Raven", 0x1c), # Attack Urban Center
    Mail(0xa, "EERC", 0x3), # Rescue Survey Team
    Mail(0xb, "Chemical-Dyne Co", 0x9), # Destroy Fuel Depot
    Mail(0xc, "The Red AC", 0x8), # Guard Freight Train
    Mail(0xd, "Factory Assault Report", 0x6), # Secret Factory Recon
    Mail(0xe, "Factory Affair Report", 0x28), # Guard Factory Entrance
    Mail(0xf, "Giant Organisms", 0x7), # Exterminate Organisms (1)
    Mail(0x10, "Plus", 0x18), # Destroy Plus Escapee
    Mail(0x11, "Relics of the Past", 0x26), # Recover Capsules
    # Mail(0x12, "Above Ground", ???), # Unknown requirement? Seems to appear after Guard Airplane on Chrome route? Might be tied to path progression
    Mail(0x13, "Struggle's Demise", 0x2c), # Kill "Struggle" Leader
    Mail(0x14, "???", 0x12), # Remove Base Occupants
    Mail(0x15, "Biological Weapons", 0x2a), # Release Organisms
    Mail(0x16, "Imminent Storm's Demise", 0x2b) # Retake Air Cleaner
)

id_to_mail = {mail.id: mail for mail in all_mail}
name_to_mail = {mail.name: mail for mail in all_mail}