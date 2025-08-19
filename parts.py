import typing

class Part:
    id: int
    name: str
    part_type: str
    price: int
    
    def __init__(self, _id: int, name: str, part_type: str, price: int):
        self.id = _id
        self.name = name
        self.part_type = part_type
        self.price = price

    def __str__(self) -> str:
        return (
            f"{self.name} "
        )
    
# For parts that do not have specific parameters, -1 if its an int and they don't have it, "" if its a string and they don't have it
# Could pull data right from game... But also I feel like this data will be nice to have documented for posterity
    
class Head(Part):
    weight: int
    energy_drain: int
    armor_point: int
    def_shell: int
    def_energy: int
    computer_type: str
    map_type: str
    noise_canceler: str
    bio_sensor: str
    radar_function: str
    radar_range: str
    radar_type: str

    def __init__(self, _id: int, name: str, part_type: str, price: int,
                 weight: int, energy_drain: int, armor_point: int,
                 def_shell: int, def_energy: int, computer_type: str, 
                 map_type: str, noise_canceler: str, bio_sensor: str,
                 radar_function: str, radar_range: int = -1, radar_type: str = ""):
        self.id = _id
        self.name = name
        self.part_type = part_type
        self.price = price
        self.weight = weight
        self.energy_drain = energy_drain
        self.armor_point = armor_point
        self.def_shell = def_shell
        self.def_energy = def_energy
        self.computer_type = computer_type
        self.map_type = map_type
        self.noise_canceler = noise_canceler
        self.bio_sensor = bio_sensor
        self.radar_function = radar_function
        self.radar_range = radar_range
        self.radar_type = radar_type

all_heads: typing.Tuple[Head, ...] = (
    Head(0x00, "HD-01-SRVT", "HEAD UNIT", 26500, 122, 350, 816, 154, 149, "DETAILED", "AREA MEMORY", "NONE", "PROVIDED", "NONE"), #Head unit with built-in bio sensor.
    Head(0x01, "HD-2002", "HEAD UNIT", 29000, 156, 457, 787, 140, 154, "STANDARD", "AREA MEMORY", "NONE", "NONE", "PROVIDED", 6000, "STANDARD"), #Head unit equipped with radar function.

)

class Core(Part):
    weight: int
    energy_drain: int
    armor_point: int
    def_shell: int
    def_energy: int
    max_weight: int
    anti_missile_response: int
    anti_missile_angle: int
    extension_slots: int

    def __init__(self, _id: int, name: str, part_type: str, price: int,
                 weight: int, energy_drain: int, armor_point: int,
                 def_shell: int, def_energy: int, max_weight: int,
                 anti_missile_response: int, anti_missile_angle: int,
                 extension_slots: int):
        self.id = _id
        self.name = name
        self.part_type = part_type
        self.price = price
        self.weight = weight
        self.energy_drain = energy_drain
        self.armor_point = armor_point
        self.def_shell = def_shell
        self.def_energy = def_energy
        self.max_weight = max_weight
        self.anti_missile_response = anti_missile_response
        self.anti_missile_angle = anti_missile_angle
        self.extension_slots = extension_slots

all_cores: typing.Tuple[Core, ...] = (
    Core(0x??, "XCA-00", "CORE UNIT", 61500, 1103, 1046, 2710, 530, 505, 2770, 48, 48, 8), #Standard core unit with average performance overall

)

class Arms(Part):
    weight: int
    energy_drain: int
    armor_point: int
    def_shell: int
    def_energy: int
    weapon_lock: str
    attack_power: int
    number_of_ammo: int
    ammo_type: str
    ammo_price: int
    arms_range: int
    maximum_lock: int
    reload_time: int

    def __init__(self, _id: int, name: str, part_type: str, price: int,
                 weight: int, energy_drain: int, armor_point: int,
                 def_shell: int, def_energy: int, weapon_lock: str = "",
                 attack_power: int = -1, number_of_ammo: int = -1,
                 ammo_type: str = "", ammo_price: int = -1, arms_range: int = -1,
                 maximum_lock: int = -1, reload_time: int = -1):
        self.id = _id
        self.name = name
        self.part_type = part_type
        self.price = price
        self.weight = weight
        self.energy_drain = energy_drain
        self.armor_point = armor_point
        self.def_shell = def_shell
        self.def_energy = def_energy
        self.weapon_lock = weapon_lock
        self.attack_power = attack_power
        self.number_of_ammo = number_of_ammo
        self.ammo_type = ammo_type
        self.ammo_price = ammo_price
        self.arms_range = arms_range
        self.maximum_lock = maximum_lock
        self.reload_time = reload_time

all_arms: typing.Tuple[Arms, ...] = (
    Arms(0x??, "AN-101", "ARM UNIT", 19000, 1228, 1006, 1670, 384, 374), #Normal arm units with average performance.

    Arms(0x??, "AW-MG25/2", "MACHINE GUN", 54500, 1193, 78, 812, 0, 0, "SPECIAL", 158, 400, "SOLID", 33, 8800, 1, 2), #Can strafe with 4 rifles at once
)

class Legs(Part):
    weight: int
    energy_drain: int
    armor_point: int
    def_shell: int
    def_energy: int
    max_weight: int
    speed: int
    stability: int
    jump_function: str

    def __init__(self, _id: int, name: str, part_type: str, price: int,
                 weight: int, energy_drain: int, armor_point: int,
                 def_shell: int, def_energy: int, max_weight: int,
                 speed: int, stability: int, jump_function: str):
        self.id = _id
        self.name = name
        self.part_type = part_type
        self.price = price
        self.weight = weight
        self.energy_drain = energy_drain
        self.armor_point = armor_point
        self.def_shell = def_shell
        self.def_energy = def_energy
        self.max_weight = max_weight
        self.speed = speed
        self.stability = stability
        self.jump_function = jump_function

all_legs: typing.Tuple[Legs, ...] = (
    Legs(0x??, "LN-1001", "HUMANOID LEGS", 28500, 1966, 1725, 3235, 556, 531, 4470, 277, 1018, "PROVIDED"), #Balanced, standard humanoid legs.

)

class Generator(Part):
    weight: int
    energy_output: int
    maximum_charge: int
    charge_redzone: int

    def __init__(self, _id: int, name: str, part_type: str, price: int,
                 weight: int, energy_output: int, maximum_charge: int,
                 charge_redzone: int):
        self.id = _id
        self.name = name
        self.part_type = part_type
        self.price = price
        self.weight = weight
        self.energy_output = energy_output
        self.maximum_charge = maximum_charge
        self.charge_redzone = charge_redzone

all_generators: typing.Tuple[Generator, ...] = (
    Generator(0x??, "GPS-VVA", "PULSE GENERATOR", 19500, 308, 4728, 28000, 7800), #Low in both power and capacity. Wide red zone.

)

class FCS(Part):
    weight: int
    energy_drain: int
    maximum_lock: int
    lock_type: str

    def __init__(self, _id: int, name: str, part_type: str, price: int,
                 weight: int, energy_drain: int, maximum_lock: int,
                 lock_type: str):
        self.id = _id
        self.name = name
        self.part_type = part_type
        self.price = price
        self.weight = weight
        self.energy_drain = energy_drain
        self.maximum_lock = maximum_lock
        self.lock_type = lock_type

all_fcs: typing.Tuple[FCS, ...] = (
    FCS(0x??, "COMDEX-C7", "FCS", 11100, 14, 24, 4, "STANDARD"), #Maximum of 4 lock-ons, average performance

)


class Option_Part(Part):
    slot_spend: int

    def __init__(self, _id: int, name: str, part_type: str, price: int,
                 slot_spend: int):
        self.id = _id
        self.name = name
        self.part_type = part_type
        self.price = price
        self.slot_spend = slot_spend

all_options_parts: typing.Tuple[Option_Part, ...] = (
    Option_Part(0x??, "SP-MAW", "RADAR OPTION", 14200, 1), #Adds a missile display function to the radar.

)


class Booster(Part):
    weight: int
    energy_drain: int
    boost_power: int
    charge_drain: int

    def __init__(self, _id: int, name: str, part_type: str, price: int,
                 weight: int, energy_drain: int, boost_power: int,
                 charge_drain: int):
        self.id = _id
        self.name = name
        self.part_type = part_type
        self.price = price
        self.weight = weight
        self.energy_drain = energy_drain
        self.boost_power = boost_power
        self.charge_drain = charge_drain

all_boosters: typing.Tuple[Booster, ...] = (
    Booster(0x??, "B-P320", "BOOST UNIT", 10800, 208, 28, 9800, 4360), #Low priced but seems a bit underpowered.

)

class Back_Weapon(Part):
    weight: int
    energy_drain: int
    radar_function: str
    weapon_lock: str
    attack_power: int
    number_of_ammo: int
    ammo_type: str
    ammo_price: int
    arms_range: int
    maximum_lock: int
    reload_time: int

    def __init__(self, _id: int, name: str, part_type: str, price: int,
                 weight: int, energy_drain: int, radar_function: str, 
                 weapon_lock: str, attack_power: int, number_of_ammo: int, 
                 ammo_type: str, ammo_price: int, arms_range: int, 
                 maximum_lock: int, reload_time: int):
        self.id = _id
        self.name = name
        self.part_type = part_type
        self.price = price
        self.weight = weight
        self.energy_drain = energy_drain
        self.radar_function = radar_function
        self.weapon_lock = weapon_lock
        self.attack_power = attack_power
        self.number_of_ammo = number_of_ammo
        self.ammo_type = ammo_type
        self.ammo_price = ammo_price
        self.arms_range = arms_range
        self.maximum_lock = maximum_lock
        self.reload_time = reload_time

all_back_weapons: typing.Tuple[Back_Weapon, ...] = (
    Back_Weapon(0x??, "WM-S40/1", "SMALL MISSILE", 18700, 245, 245, "NONE", "STANDARD", 830, 40, "SOLID", 130, 9000, 1, 10), #Pod that fires single small missiles.

)


class Arm_Weapon_L(Part): #laserblades
    weight: int
    energy_drain: int
    charge_drain: int
    attack_power: int

    def __init__(self, _id: int, name: str, part_type: str, price: int,
                 weight: int, energy_drain: int, charge_drain: int,
                 attack_power: int):
        self.id = _id
        self.name = name
        self.part_type = part_type
        self.price = price
        self.weight = weight
        self.energy_drain = energy_drain
        self.charge_drain = charge_drain
        self.attack_power = attack_power

all_arm_weapon_ls: typing.Tuple[Arm_Weapon_L, ...] = (
    Arm_Weapon_L(0x??, "LS-2001", "LASERBLADE", 11500, 123, 28, 2050, 738), #Infinitely reusable laser blade.

)

class Arm_Weapon_R(Part): #guns
    weight: int
    energy_drain: int
    weapon_lock: str
    attack_power: int
    number_of_ammo: int
    ammo_type: str
    ammo_price: int
    arms_range: int
    maximum_lock: int
    reload_time: int

    def __init__(self, _id: int, name: str, part_type: str, price: int,
                 weight: int, energy_drain: int, weapon_lock: str, 
                 attack_power: int, number_of_ammo: int, ammo_type: str, 
                 ammo_price: int, arms_range: int, maximum_lock: int, 
                 reload_time: int):
        self.id = _id
        self.name = name
        self.part_type = part_type
        self.price = price
        self.weight = weight
        self.energy_drain = energy_drain
        self.weapon_lock = weapon_lock
        self.attack_power = attack_power
        self.number_of_ammo = number_of_ammo
        self.ammo_type = ammo_type
        self.ammo_price = ammo_price
        self.arms_range = arms_range
        self.maximum_lock = maximum_lock
        self.reload_time = reload_time

all_arm_weapon_rs: typing.Tuple[Arm_Weapon_R, ...] = (
    Arm_Weapon_R(0x??, "NO WEAPON", "- - - - - - - -", 0, 0, 0, "WIDE & SHALLOW", 0, 0, "- - - - - -", 0, 0, 0, 0), #
    Arm_Weapon_R(0x??, "WG-RF35", "RIFLE", 11400, 415, 6, "WIDE & SHALLOW", 218, 200, "SOLID", 18, 8500, 1, 5), #Standard portable rifle. Suitable for various missions.
    
)