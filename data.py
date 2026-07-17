from .raven import all_ravens
from .mail import all_mail
from .mission import all_missions
from .parts import all_parts, all_options_parts, all_arm_weapon_ls, all_arm_weapon_rs, all_arms, all_back_weapons, all_boosters, all_cores, all_dummy_parts, all_fcs, all_generators, all_heads, all_legs
from .locations import get_location_name_for_raven, get_location_name_for_mail, get_location_name_for_mission, get_location_name_for_shop_listing

raven_locations: list[str] = []
for raven in all_ravens:
    raven_locations.append(get_location_name_for_raven(raven))

mail_locations: list[str] = []
for mail in all_mail:
    mail_locations.append(get_location_name_for_mail(mail))

mission_locations: list[str] = []
for mission in all_missions:
    mission_locations.append(get_location_name_for_mission(mission))

all_parts_shop_locations: list[str] = []
for part in all_parts:
    all_parts_shop_locations.append(get_location_name_for_shop_listing(part))

all_head_shop_locations: list[str] = []
for part in all_heads:
    all_head_shop_locations.append(get_location_name_for_shop_listing(part))

all_core_shop_locations: list[str] = []
for part in all_cores:
    all_core_shop_locations.append(get_location_name_for_shop_listing(part))

all_arm_shop_locations: list[str] = []
for part in all_arms:
    all_arm_shop_locations.append(get_location_name_for_shop_listing(part))

all_leg_shop_locations: list[str] = []
for part in all_legs:
    all_leg_shop_locations.append(get_location_name_for_shop_listing(part))

all_generator_shop_locations: list[str] = []
for part in all_generators:
    all_generator_shop_locations.append(get_location_name_for_shop_listing(part))

all_fcs_shop_locations: list[str] = []
for part in all_fcs:
    all_fcs_shop_locations.append(get_location_name_for_shop_listing(part))

all_option_part_shop_locations: list[str] = []
for part in all_options_parts:
    all_option_part_shop_locations.append(get_location_name_for_shop_listing(part))

all_booster_shop_locations: list[str] = []
for part in all_boosters:
    all_booster_shop_locations.append(get_location_name_for_shop_listing(part))

all_back_weapon_shop_locations: list[str] = []
for part in all_back_weapons:
    all_back_weapon_shop_locations.append(get_location_name_for_shop_listing(part))

all_arm_weapon_r_shop_locations: list[str] = []
for part in all_arm_weapon_rs:
    all_arm_weapon_r_shop_locations.append(get_location_name_for_shop_listing(part))

all_arm_weapon_l_shop_locations: list[str] = []
for part in all_arm_weapon_ls:
    all_arm_weapon_l_shop_locations.append(get_location_name_for_shop_listing(part))

all_dummy_shop_locations: list[str] = []
for part in all_dummy_parts:
    all_dummy_shop_locations.append(get_location_name_for_shop_listing(part))
    
location_groups = {
    "Ravens": raven_locations,
    "Mail": mail_locations,
    "Missions": mission_locations,
    "All Parts": all_parts_shop_locations,
    "Heads": all_head_shop_locations,
    "Cores": all_core_shop_locations,
    "Arms": all_arm_shop_locations,
    "Legs": all_leg_shop_locations,
    "Generators": all_generator_shop_locations,
    "FCS": all_fcs_shop_locations,
    "Option Parts": all_option_part_shop_locations,
    "Boosters": all_booster_shop_locations,
    "Back Weapons": all_back_weapon_shop_locations,
    "Arm Weapon Rs": all_arm_weapon_r_shop_locations,
    "Arm Weapon Ls": all_arm_weapon_l_shop_locations,
    "Dummy": all_dummy_shop_locations
}