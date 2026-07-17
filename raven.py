import typing

class Raven:
    id: int
    name: str
    mission_access_id: int # Value is -1 if it is a special case (not tied to mission ID)

    def __init__(self, _id: int, name: str, unlock_id: int):
        self.id = _id
        self.name = name
        self.mission_access_id = unlock_id


    def __str__(self) -> str:
        return (
            f"{self.name} "
        )
    
# All ravens that you can fight in missions, not technically all ravens
all_ravens: typing.Tuple[Raven, ...] = (
    Raven(0x0, "Valkyrie", 0x1c), # Attack Urban Center
    Raven(0x1, "Nine-Ball", 0x30), # Destroy Floating Mines
    Raven(0x2, "Fefnir", 0x1b), # AC Battle (1)
    Raven(0x3, "Kamui Mk. 17", 0x1a), # Destroy Plane Computer
    Raven(0x4, "Sledgehammer", 0x2f) # Mop Up Chrome Remnants (2)
)

id_to_raven = {raven.id: raven for raven in all_ravens}
name_to_raven = {raven.name: raven for raven in all_ravens}