# Data ripped by Vartazian
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
            f"{self.part_type} - {self.name}"
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
    Head(0x02, "HD-X1487", "HEAD UNIT", 19000, 166, 420, 975, 160, 185, "ROUGH", "NO MEMORY", "PROVIDED", "PROVIDED", "NONE"), #Full range of sensors but without the auto-map function.
    Head(0x03, "HD-REDEYE", "HEAD UNIT", 41100, 146, 538, 840, 148, 151, "DETAILED", "AREA&PLACE NAME", "NONE", "NONE", "PROVIDED", 5980, "STANDARD"), #Equipped with radar and an enhanced auto-map function.
    Head(0x04, "HS-D-9066", "HEAD UNIT", 43200, 138, 657, 885, 165, 232, "STANDARD", "AREA MEMORY", "NONE", "PROVIDED", "PROVIDED", 6120, "STANDARD"), #Full range of options and good EG shields.
    Head(0x05, "HD-GRY-NX", "HEAD UNIT", 14700, 232, 218, 1001, 194, 134, "ROUGH", "NO MEMORY", "NONE", "NONE", "NONE"), #Economy Unit with good shields but no optional equipment.
    Head(0x06, "HD-06-RADAR", "HEAD UNIT", 51800, 145, 875, 741, 109, 194, "STANDARD", "AREA&PLACE NAME", "PROVIDED", "NONE", "PROVIDED", 8120, "STANDARD"), #Equiped with wide-area radar and various options.
    Head(0x07, "HD-ONE", "HEAD UNIT", 68100, 161, 304, 800, 132, 129, "DETAILED", "AREA MEMORY", "PROVIDED", "PROVIDED", "PROVIDED", 7980, "STANDARD"), #Fully equipped with wide-area radar and all options.
    Head(0x08, "HD-08-DISH", "HEAD UNIT", 33200, 133, 716, 870, 205, 162, "STANDARD", "AREA&PLACE NAME", "NONE", "NONE", "NONE"), #Equipped with an enhanced auto-map function.
    Head(0x09, "HD-ZERO", "HEAD UNIT", 22500, 185, 431, 925, 221, 149, "ROUGH", "NO MEMORY", "NONE", "NONE", "PROVIDED", 6300, "STANDARD"), #Equipped with radar functions and enhanced shock protection.

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
    Core(0x0A, "XCA-00", "CORE UNIT", 61500, 1103, 1046, 2710, 530, 505, 2770, 48, 48, 8), #Standard core unit with average performance overall.
    Core(0x0B, "XCL-01", "CORE UNIT", 88000, 885, 1380, 2380, 492, 610, 2450, 45, 64, 16), #Electronic warfare core with many slots for special equipment.
    Core(0x0C, "XCH-01", "CORE UNIT", 72000, 1384, 873, 3015, 615, 543, 3600, 48, 32, 12), #Heavyweight core with an excellent shoulder load and heavy armor.
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
    Arms(0x0D, "AN-101", "ARM UNIT", 19000, 1228, 1006, 1670, 384, 374), #Normal arm units with average performance.
    Arms(0x0E, "AN-201", "ARM UNIT", 15300, 1054, 877, 1635, 352, 334), #Low energy consumption version of the AN-101.
    Arms(0x0F, "AN-K1", "ARM UNIT", 49000, 905, 930, 1790, 337, 402), #Reduced-weight arm units with full AP and shields.
    Arms(0x10, "AN-D-7001", "ARM UNIT", 23000, 1445, 1512, 1743, 306, 453), #Average arm units with enhanced performance.
    Arms(0x11, "AN-3001", "ARM UNIT", 39500, 1612, 1258, 1935, 487, 353), #Middleweight arms with maximum energy shielding.
    Arms(0x12, "ANKS-1A46J", "ARM UNIT", 42100, 2120, 1415, 1990, 679, 496), #Offers the maximum AP but interferes with some parts.
    Arms(0x13, "AN-863-B", "ARM UNIT", 34000, 1726, 1394, 1880, 517, 406), #Weight is increased for added durability.
    Arms(0x14, "AN-25", "ARM UNIT", 28400, 853, 682, 1826, 344, 284), #Lightweight type arm units with better performance.
    Arms(0x15, "AW-MG25/2", "MACHINE GUN", 54500, 1193, 78, 812, 0, 0, "SPECIAL", 158, 400, "SOLID", 33, 8800, 1, 2), #Can strafe with 4 rifles at once
    Arms(0x16, "AW-GT2000", "GATLING GUN", 48600, 1415, 92, 1132, 0, 0, "SPECIAL", 305, 300, "SOLID", 62, 7800, 1, 2), #Dual Gatling guns can concentrate high-speed rounds at a single point.
    Arms(0x17, "AW-RF105", "CANNON", 77600, 1530, 106, 1280, 0, 0, "NARROW & DEEP", 1530, 100, "SOLID", 220, 9300, 1, 15), #2 cannons with incredible firepower.
    Arms(0x18, "AW-30/3", "DUAL MISSILE", 56400, 480, 377, 688, 0, 0, "STANDARD", 830, 80, "SOLID", 130, 9000, 3, 10), #Fires 2 rounds of 3 small missiles for a total of 6 missiles.
    Arms(0x19, "AW-RF120", "CANNON", 67200, 1827, 137, 1420, 0, 0, "NARROW & DEEP", 2120, 50, "SOLID", 300, 9800, 1, 18), #Enhanced dual cannons. Somewhat fewer shots. 
    Arms(0x1A, "AW-S60/2", "DUAL MISSILE", 66600, 762, 420, 725, 0, 0, "STANDARD", 830, 120, "SOLID", 130, 9000, 2, 10), #Fires 2 rounds of 2 missiles at once for extra shots.
    Arms(0x1B, "AW-XC5500", "PLASMA CANNON", 83600, 1688, 547, 875, 0, 0, "NARROW & DEEP", 1241, 70, "ENERGY", 0, 12000, 1, 7), #Energy weapon. Fires twin bursts of light.
    Arms(0x1C, "AW-XC65", "LASER CANNON", 98500, 1905, 625, 792, 0, 0, "NARROW & DEEP", 2322, 40, "ENERGY", 0, 8300, 1, 10) #Energy Weapon. Fires two beams. 
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
    Legs(0x1D, "LN-1001", "HUMANOID LEGS", 28500, 1966, 1725, 3235, 556, 531, 4470, 277, 1018, "PROVIDED"), #Balanced, standard humanoid legs.
    Legs(0x1E, "LN-SSVT", "HUMANOID LEGS", 44000, 1528, 2338, 2795, 482, 507, 3560, 445, 596, "PROVIDED"), #Light, fast humanoid legs but with low load capacity and AP.
    Legs(0x1F, "LN-3001", "HUMANOID LEGS", 52200, 3137, 2206, 3703, 870, 594, 6600, 153, 2518, "PROVIDED"), #Heavily armored humanoid legs with high load capacity. Poor speed. 
    Legs(0x20, "LN-1001-PX-0", "HUMANOID LEGS", 25000, 1892, 1844, 3035, 528, 508, 4100, 280, 904, "PROVIDED"), #Balanced humanoid legs for combat on all terrain.
    Legs(0x21, "LN-501", "HUMANOID LEGS", 71800, 1675, 2910, 2947, 508, 535, 3990, 451, 854, "PROVIDED"), #Has the shield performance and load capacity of a middleweight.
    Legs(0x22, "LN-SSVR", "HUMANOID LEGS", 32400, 2750, 2013, 3606, 805, 532, 5400, 148, 2150, "PROVIDED"), #Lightest of the heavily armored humanoid legs.
    Legs(0x23, "LN-1001B", "HUMANOID LEGS", 45200, 2305, 1889, 3383, 585, 543, 4630, 272, 1320, "PROVIDED"), #Enhanced variation of the LN-1001.
    Legs(0x24, "DUMMY1", "DUMMY PARTS", 0, 0, 0, 0, 0, 0, 0, 0, 0, "NONE"), #
    Legs(0x25, "LN-3001C", "HUMANOID LEGS", 64100, 3528, 2418, 3977, 889, 602, 7100, 151, 2977, "PROVIDED"), #Best AP and shields among the humanoid legs.
    Legs(0x26, "DUMMY2", "DUMMY PARTS", 0, 0, 0, 0, 0, 0, 0, 0, 0, "NONE"), #
    Legs(0x27, "LN-502", "HUMANOID LEGS", 35800, 1790, 2466, 3343, 538, 592, 3800, 275, 843, "PROVIDED"), #This middleweight has reduced weight without sacrificing performance.
    Legs(0x28, "LN-D-8000R", "HUMANOID LEGS", 49000, 2426, 2350, 3532, 510, 656, 4720, 269, 1200, "PROVIDED"), #Humanoid legs with special anti-energy weapon armor.
    Legs(0x29, "DUMMY3", "DUMMY PARTS", 0, 0, 0, 0, 0, 0, 0, 0, 0, "NONE"), #
    Legs(0x2A, "LNKS-1B46J", "HUMANOID LEGS", 48000, 3065, 2304, 3788, 822, 618, 6100, 146, 3802, "PROVIDED"), #Shock absorbing structure reduces recoil from shell hits.
    Legs(0x2B, "LB-4400", "REVERSE JOINT", 17300, 2520, 1400, 3560, 617, 451, 4020, 294, 2084, "PROVIDED"), #Standard reverse joint type. Good maneuverability and inexpensive. 
    Legs(0x2C, "DUMMY4", "DUMMY PARTS", 0, 0, 0, 0, 0, 0, 0, 0, 0, "NONE"), #
    Legs(0x2D, "LB-4401", "REVERSE JOINT", 31800, 2910, 1456, 3810, 672, 468, 4510, 287, 2713, "PROVIDED"), #Best overall performance of the reverse joint types.
    Legs(0x2E, "LB-4303", "REVERSE JOINT", 24000, 2647, 1585, 3575, 643, 488, 4180, 291, 2505, "PROVIDED"), #Increased ground contact area for enhanced shock absorbing capacity.
    Legs(0x2F, "LB-1000-P", "REVERSE JOINT", 20500, 2095, 1228, 3514, 609, 444, 3775, 286, 2310, "PROVIDED"), #Phenomenal maneuverability but low load carrying capacity.
    Legs(0x30, "LBKS-2B45A", "REVERSE JOINT", 27000, 2480, 1703, 3731, 584, 515, 3990, 299, 1985, "PROVIDED"), #Deluxe type with enhanced shielding against energy weapons.
    Legs(0x31, "DUMMY5", "DUMMY PARTS", 0, 0, 0, 0, 0, 0, 0, 0, 0, "NONE"), #
    Legs(0x32, "LF-205-SF", "FOUR LEGS TYPE", 42600, 2137, 2810, 2841, 446, 654, 3450, 483, 580, "PROVIDED"), #Standard four-leg type. Top-class maneuverability. 
    Legs(0x33, "LFH-X3", "FOUR LEGS TYPE", 56000, 2400, 2988, 3100, 468, 610, 3810, 421, 710, "PROVIDED"), #Energy gauge recovers quickly when halted.
    Legs(0x34, "LF-DEX-1", "FOUR LEGS TYPE", 69000, 2650, 4016, 3179, 557, 553, 4450, 360, 820, "PROVIDED"), #Increased load carrying capacity requires vast amounts of power.
    Legs(0x35, "DUMMY6", "DUMMY PARTS", 0, 0, 0, 0, 0, 0, 0, 0, 0, "NONE"), #
    Legs(0x36, "DUMMY7", "DUMMY PARTS", 0, 0, 0, 0, 0, 0, 0, 0, 0, "NONE"), #
    Legs(0x37, "LFH-X5X", "FOUR LEGS TYPE", 82000, 2880, 3584, 3328, 497, 700, 5000, 442, 1110, "PROVIDED"), #New four-leg type pushes the specs to the limit.
    Legs(0x38, "LC-MOS18", "CATERPILLAR", 16000, 4182, 978, 3928, 858, 572, 8000, 105, 4245, "NONE"), #Maximum load carrying capacity but poor speed and weight. 
    Legs(0x39, "LC-UKI60", "CATERPILLAR", 25500, 3860, 1104, 3822, 812, 589, 6950, 138, 3710, "NONE"), #Economy wheeled truck type with finely adjusted performance. 
    Legs(0x3A, "DUMMY8", "DUMMY PARTS", 0, 0, 0, 0, 0, 0, 0, 0, 0, "NONE"), #
    Legs(0x3B, "LC-HTP-AAA", "CATERPILLAR", 38500, 2915, 2877, 3688, 728, 694, 4130, 250, 630, "NONE"), #Has performance near that of a four-legged type.
    Legs(0x3C, "LC-MOS4545", "CATERPILLAR", 59000, 3610, 2609, 3990, 905, 753, 7400, 211, 5101, "NONE") #A dreadfully durable monster machine.
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
    Generator(0x3D, "GPS-VVA", "PULSE GENERATOR", 19500, 308, 4728, 28000, 7800), #Low in both power and capacity. Wide red zone.
    Generator(0x3E, "GPS-V6", "PULSE GENERATOR", 32000, 363, 4728, 43000, 5000), #Load increased to nearly twice that of the GPS-VVA.
    Generator(0x3F, "GRD-RX5", "PULSE GENERATOR", 23300, 225, 5300, 38000, 4000), #Balanced-performance generator.
    Generator(0x40, "GRD-RX6", "PULSE GENERATOR", 27800, 286, 6000, 33000, 4000), #Performance not bad, but the equipment is so-so.
    Generator(0x41, "GRD-RX7", "PULSE GENERATOR", 38700, 348, 6810, 31500, 5000), #Very good power but poor stamina.
    Generator(0x42, "GBG-10000", "PULSE GENERATOR", 43500, 398, 9988, 34000, 2980), #High Power provides a wide selection of equipment.
    Generator(0x43, "GBG-XR", "PULSE GENERATOR", 56000, 452, 8207, 48000, 3250) #Custom-made unit having both power and capacity.
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
    FCS(0x44, "COMDEX-C7", "FCS", 11100, 14, 24, 4, "STANDARD"), #Maximum of 4 lock-ons, average performance
    FCS(0x45, "COMDEX-G0", "FCS", 22500, 14, 24, 4, "STANDARD"), #Maximum of 4 lock-ons, fast lock-on.
    FCS(0x46, "COMDEX-G8", "FCS", 16400, 14, 24, 6, "STANDARD"), #Maximum of 6 lock-ons, long-distance lock-on.
    FCS(0x47, "QX-21", "FCS", 20300, 8, 12, 1, "WIDE & SHALLOW"), #Maximum of 1 lock-on, short lock over a wide area. 
    FCS(0x48, "QX-AF", "FCS", 35700, 10, 16, 2, "WIDE & SHALLOW"), #Maximum of 2 lock-ons, short lock. 
    FCS(0x49, "TRYX-BOXER", "FCS", 48100, 10, 19, 3, "TALL"), #Maximum of 3 lock-ons, vertical sight. 
    FCS(0x4A, "TRYX-QUAD", "FCS", 63000, 18, 38, 6, "WIDE"), #Maximum of 6 lock-ons, horizontal sight.
    FCS(0x4B, "QX-9009", "FCS", 96000, 24, 55, 6, "NARROW & DEEP") #Maximum of 6 lock-ons, longest lock distance.  
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
    Option_Part(0x4C, "SP-MAW", "RADAR OPTION", 14200, 1), #Adds a missile display function to the radar.
    Option_Part(0x4D, "SP-JAM", "MISSILE JAMMER", 26000, 3), #Regularly generates pulses that disable missile lock-ons.
    Option_Part(0x4E, "SP-M/AUTO", "AUTO LAUNCHER", 12900, 1), #Fires a missile automatically on full lock-on.
    Option_Part(0x4F, "SP-ABS", "BALANCER OPTION", 29600, 1), #Reduces the recoil of shell hits.
    Option_Part(0x50, "SP-SAP", "ABSORBER OPTION", 31800, 1), #Reduces the recoil of cannon fire.
    Option_Part(0x51, "SP-CND-K", "CHARGE EXPANDER", 21000, 4), #Increases the number of capacitors in the generator. 
    Option_Part(0x52, "SP-AXL", "FCS ACCELERATOR", 24000, 2), #Shortens the lock-on time.
    Option_Part(0x53, "SP-S/SCR", "SHELL SCREEN", 33000, 2), #Reduces the damage from solid rounds.
    Option_Part(0x54, "SP-E/SCR", "ENERGY SCREEN", 38500, 1), #Reduces damage from energy rounds.
    Option_Part(0x55, "SP-EH", "RAPID CHARGE", 45000, 1), #Increases the burst fire rate of energy weapons.
    Option_Part(0x56, "SP-E+", "ENERGY AMPLIFIER", 45000, 1) #Increases the firepower of energy weapons. 
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
    Booster(0x57, "B-P320", "BOOST UNIT", 10800, 208, 28, 9800, 4360), #Low priced but seems a bit underpowered.
    Booster(0x58, "B-P350", "BOOST UNIT", 13700, 162, 33, 12800, 4410), #Economy type with high power but high energy consumption.
    Booster(0x59, "B-T001", "BOOST UNIT", 34000, 149, 30, 17300, 4600), #Achieves both enhanced power and low weight at the same time.
    Booster(0x5A, "B-T2", "BOOST UNIT", 31500, 235, 38, 14800, 3850), #Power itself is low but offers the highest efficiency.
    Booster(0x5B, "B-P351", "BOOST UNIT", 25500, 288, 41, 21000, 6980), #High-Performance model with both high power and energy consumption.
    Booster(0x5C, "B-VR-33", "BOOST UNIT", 48500, 255, 35, 19000, 5070) #Maintains the top-class power to achieve good efficiency.
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
                 weapon_lock: str, attack_power: int, number_of_ammo: int = -1, 
                 ammo_type: str = "", ammo_price: int = -1, arms_range: int = -1, 
                 maximum_lock: int = -1, reload_time: int = -1):
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
    Back_Weapon(0x5D, "WM-S40/1", "SMALL MISSILE", 18700, 245, 245, "NONE", "STANDARD", 830, 40, "SOLID", 130, 9000, 1, 10), #Pod that fires single small missiles.
    Back_Weapon(0x5E, "WM-S40/2", "SMALL MISSILE", 23000, 337, 320, "NONE", "STANDARD", 830, 40, "SOLID", 130, 9000, 2, 10), #Fires up to 2 small missiles at once.
    Back_Weapon(0x5F, "WM-S60/4", "SMALL MISSILE", 28800, 520, 349, "NONE", "STANDARD", 830, 60, "SOLID", 130, 9000, 4, 10), #Fires up to 4 small missiles at once.
    Back_Weapon(0x60, "WM-S60/6", "SMALL MISSILE", 38100, 583, 353, "NONE", "STANDARD", 830, 60, "SOLID", 130, 9000, 6, 10), #Fires up to 6 small missiles at once.
    Back_Weapon(0x61, "WM-MVG404", "MISSILE", 31000, 620, 280, "NONE", "STANDARD", 1560, 24, "SOLID", 252, 10000, 1, 10), #Pod that fires singles missiles.
    Back_Weapon(0x62, "WM-MVG802", "MISSILE", 44000, 718, 220, "NONE", "STANDARD", 1560, 32, "SOLID", 252, 10000, 2, 10), #Fires up to 2 missiles at once.
    Back_Weapon(0x63, "WM-L201", "LARGE MISSILE", 46200, 835, 180, "NONE", "STANDARD", 4300, 12, "SOLID", 897, 12500, 1, 10), #Powerful large missiles fired singly
    Back_Weapon(0x64, "WM-X201", "MULTI MISSILE", 62250, 720, 250, "NONE", "STANDARD", 980, 18, "SOLID", 1125, 12000, 1, 15), #Multi-warhead missile that scatters warheads in flight.
    Back_Weapon(0x65, "WM-X5-AA", "BOMB DISPENSER", 19300, 616, 85, "NONE", "NONE", 675, 10, "SOLID", 270, 0, 0, 50), #Drops 8 ground-attack mines. For experts.
    Back_Weapon(0x66, "WM-X10", "BOMB DISPENSER", 24800, 939, 105, "NONE", "NONE", 675, 10, "SOLID", 560, 0, 0, 50), #Drops 16 powerful ground-attack mines.
    Back_Weapon(0x67, "WM-P40001", "DUAL MISSILE", 43800, 755, 320, "NONE", "STANDARD", 830, 60, "SOLID", 130, 9000, 1, 10), #Fires 2 left or right curving indirect attack missiles.
    Back_Weapon(0x68, "WM-PS-2", "TRIPLE MISSILE", 66700, 1125, 360, "NONE", "STANDARD", 830, 90, "SOLID", 130, 9000, 1, 10), #Fires 3 up-curving indirect attack missiles.
    Back_Weapon(0x69, "WR-S50", "SMALL ROCKET", 15900, 218, 8, "NONE", "NONE", 1310, 50, "SOLID", 110, 12500, 0, 8), #Carries 50 small rockets.
    Back_Weapon(0x6A, "WR-S100", "SMALL ROCKET", 32400, 846, 15, "NONE", "NONE", 1310, 100, "SOLID", 110, 12500, 0, 12), #Carries 100 small rockets.
    Back_Weapon(0x6B, "WR-M50", "ROCKET", 27600, 677, 13, "NONE", "NONE", 2240, 50, "SOLID", 220, 14000, 0, 12), #Carries 50 rockets.
    Back_Weapon(0x6C, "WR-M70", "ROCKET", 36500, 718, 24, "NONE", "NONE", 2240, 70, "SOLID", 220, 14000, 0, 16), #Carries 70 rockets.
    Back_Weapon(0x6D, "WR-L24", "LARGE ROCKET", 29460, 805, 18, "NONE", "NONE", 3980, 24, "SOLID", 417, 17700, 0, 16), #This Rocket has the greatest firepower of any single weapon.
    Back_Weapon(0x6E, "WC-CN35", "CHAIN GUN", 32750, 593, 11, "NONE", "SPECIAL", 338, 250, "SOLID", 52, 10000, 1, 2), #Fast reloading rifle. Easy to use.
    Back_Weapon(0x6F, "WC-ST120", "SLUG GUN", 56000, 827, 6, "NONE", "SPECIAL", 183, 80, "SOLID", 156, 8100, 1, 22), #Fires 7 simultaneous shots that scatter over a wide range.
    Back_Weapon(0x70, "WC-LN350", "LINEAR GUN", 41800, 425, 8, "NONE", "SPECIAL", 690, 120, "SOLID", 108, 9000, 1, 6), #Burst-fire type weapon emphasizing firepower over number of shots.
    Back_Weapon(0x71, "WC-GN230", "GRENADE LAUNCHER", 75200, 1230, 8, "NONE", "NARROW & DEEP", 3520, 15, "SOLID", 985, 12000, 1, 32), #An AC’s symbolic weapon that mows down enemies in a firestorm.
    Back_Weapon(0x72, "WC-XP4000", "PULSE CANNON", 61000, 318, 364, "NONE", "NARROW & DEEP", 770, 100, "ENERGY", 0, 9000, 1, 5), #Energy weapon. Reloading ion cannon.
    Back_Weapon(0x73, "WC-XC8000", "LASER CANNON", 78700, 1110, 455, "NONE", "NARROW & DEEP", 2065, 50, "ENERGY", 0, 8500, 1, 10), #Energy weapon. Fires laser rounds.
    Back_Weapon(0x74, "WC-01QL", "PLASMA CANNON", 69500, 273, 618, "NONE", "NARROW & DEEP", 1531, 80, "ENERGY", 0, 12000, 1, 7), #Energy weapon. Beam cuts down enemies.
    Back_Weapon(0x75, "RXA-01WE", "RADAR", 12100, 210, 243, "PROVIDED", 8650, "STANDARD"), #Old-style antenna but still holds up well in use.
    Back_Weapon(0x76, "RZ-A0", "RADAR", 17900, 480, 387, "PROVIDED", 11500, "CIRCLE"), #This radar uses 2 dishes for enhanced enemy-search capability.
    Back_Weapon(0x77, "RXA-99", "RADAR", 14500, 160, 267, "PROVIDED", 8800, "STANDARD"), #New-type radar permits even wider area to be searched.
    Back_Weapon(0x78, "RXA-77", "RADAR", 23000, 125, 274, "PROVIDED", 8700, "STANDARD"), #This radar can detect the approach of homing missiles.
    Back_Weapon(0x79, "RZ-A1", "RADAR", 33000, 433, 403, "PROVIDED", 15700, "CIRCLE"),  #Expands the enemy-search range up to the current technological limit.
    Back_Weapon(0x7A, "RZT-333", "RADAR", 27700, 343, 451, "PROVIDED", 11700, "OCTAGON"), #Combines both missile detection and wide-range search capability.
    Back_Weapon(0x7B, "RZ-BBP", "RADAR", 40900, 454, 566, "PROVIDED", 16300, "CIRCLE"), #Highest-quality radar with highest-class performance.
    Back_Weapon(0x7C, "WX-S800/2", "DUAL MISSILE", 69400, 1650, 415, "NONE", "STANDARD", 1120, 60, "SOLID", 515, 11000, 1, 12), #Fires 2 missiles with 1 lock-on
    Back_Weapon(0x7D, "WX-S800-GF", "DUAL MISSILE", 90900, 1110, 656, "NONE", "STANDARD", 1120, 60, "SOLID", 515, 11000, 1, 10), #Fires 6 missiles with 1 lock-on
    Back_Weapon(0x7E, "XCS-9900", "MULTI MISSILE", 94500, 1480, 310, "NONE", "STANDARD", 980, 20, "SOLID", 1125, 12000, 1, 15) #Fires 2 multi-warhead missiles simultaneously. 
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
    Arm_Weapon_R(0x7F, "NO WEAPON", "- - - - - - - -", 0, 0, 0, "WIDE & SHALLOW", 0, 0, "- - - - - -", 0, 0, 0, 0), #
    Arm_Weapon_R(0x80, "WG-RF35", "RIFLE", 11400, 415, 6, "WIDE & SHALLOW", 218, 200, "SOLID", 18, 8500, 1, 5), #Standard portable rifle. Suitable for various missions.
    Arm_Weapon_R(0x81, "WG-MGA1", "MACHINE GUN", 14000, 370, 4, "WIDE & SHALLOW", 85, 500, "SOLID", 9, 6300, 1, 1), #Fast-reloading solid round machine gun. Low single-round firepower.
    Arm_Weapon_R(0x82, "WG-MG500", "MACHINE GUN", 28400, 458, 4, "WIDE & SHALLOW", 135, 500, "SOLID", 15, 7800, 1, 2), #Enhanced version of the machine gun with higher firepower.
    Arm_Weapon_R(0x83, "WG-AR1000", "MACHINE GUN", 42300, 516, 8, "SPECIAL", 105, 1000, "SOLID", 12, 7000, 1, 1), #Most powerful portable type machine gun.
    Arm_Weapon_R(0x84, "WG-HG235", "HAND GUN", 19000, 170, 22, "WIDE & SHALLOW", 226, 100, "SOLID", 68, 4800, 1, 5), #Wide scatter-shot pistol. Very short range.
    Arm_Weapon_R(0x85, "WG-RF/5", "SNIPER RIFLE", 41500, 295, 5, "SPECIAL", 530, 80, "SOLID", 83, 20000, 1, 10), #Long-barrel sniper rifle.
    Arm_Weapon_R(0x86, "WG-RF/P", "SNIPER RIFLE", 33100, 308, 4, "SPECIAL", 612, 60, "SOLID", 95, 16000, 1, 12), #Superior firepower and range, but low reload rate.
    Arm_Weapon_R(0x87, "WG-HG512", "HAND GUN", 26200, 324, 10, "WIDE & SHALLOW", 437, 120, "SOLID", 48, 5800, 1, 8), #Lower performance, but inexpensive.
    Arm_Weapon_R(0x88, "WG-FG99", "FLAMETHROWER", 58300, 352, 9, "NONE", 512, 500 , "SOLID", 41, 900, 1, 1), #Close-in combat gun shows off its true worth in hand-to-hand combat.
    Arm_Weapon_R(0x89, "WG-B2120", "BAZOOKA", 59740, 778, 13, "NARROW & DEEP", 1250, 80, "SOLID", 163, 8200, 1, 16), #High firepower but slow-moving bazooka fire is easily avoidable.
    Arm_Weapon_R(0x8A, "WG-B2180", "BAZOOKA", 75900, 905, 16, "NARROW & DEEP", 1930, 50, "SOLID", 348, 7800, 1, 22), #Ultra-attack bazooka for betting it all on one shot.
    Arm_Weapon_R(0x8B, "WG-XP1000", "PULSE RIFLE", 46000, 188, 246, "SPECIAL", 302, 180, "ENERGY", 0, 15000, 1, 3), #Energy weapon. Noted for its long range and reload speed.
    Arm_Weapon_R(0x8C, "WG-XP2000", "PULSE RIFLE", 61500, 265, 285, "SPECIAL", 435, 200, "ENERGY", 0, 18000, 1, 6), #Energy weapon. Emphasizes its long range and number of shots.
    Arm_Weapon_R(0x8D, "WG-XC4", "LASER RIFLE", 51000, 686, 308, "SPECIAL", 820, 100, "ENERGY", 0, 8000, 1, 10), #Energy weapon. High firepower and energy consumption.
    Arm_Weapon_R(0x8E, "WG-1-KARASAWA", "LASER RIFLE", 75000, 1000, 422, "SPECIAL", 1550, 50, "ENERGY", 0, 10000, 1, 8) #Energy Weapon. Powerful but heavy.
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
    Arm_Weapon_L(0x8F, "LS-2001", "LASERBLADE", 11500, 123, 28, 2050, 738), #Infinitely reusable laser blade.
    Arm_Weapon_L(0x90, "LS-200G", "LASERBLADE", 29000, 181, 45, 1700, 950), #Powerful weapon exclusively for close-in combat.
    Arm_Weapon_L(0x91, "LS-3303", "LASERBLADE", 37200, 224, 43, 2630, 1210), #Enhanced blade weapon. Both power and energy consumption are higher.
    Arm_Weapon_L(0x92, "LS-99-MOONLIGHT", "LASERBLADE", 54000, 336, 93, 810, 2801) #Blade weapon with more than twice the power of conventional blades.
)


all_parts: typing.Tuple[Part, ...] = all_heads + all_cores + all_legs + all_arms + all_arm_weapon_rs + all_back_weapons + all_arm_weapon_ls + all_boosters + all_fcs + all_generators + all_options_parts  

all_dummy_parts: typing.Tuple[Part, ...] = (part for part in all_parts if part.name == "DUMMY" or part.name == "NO WEAPON")

base_starting_parts: typing.Tuple[Part, ...] = (part for part in all_parts if 
                                                part.name == "HD-GRY-NX" or
                                                part.name == "XCA-00" or
                                                part.name == "AN-201" or
                                                part.name == "LN-1001-PX-0" or
                                                part.name == "GPS-VVA" or
                                                part.name == "COMDEX-C7" or
                                                part.name == "B-P320" or
                                                part.name == "WM-S40/1" or
                                                part.name == "RXA-01WE" or
                                                part.name == "WG-RF35" or
                                                part.name == "LS-2001")

id_to_part = {part.id: part for part in all_parts}
name_to_part = {part.name: part for part in all_parts}