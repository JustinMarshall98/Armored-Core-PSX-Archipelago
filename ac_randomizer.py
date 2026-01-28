# Authors: Vartazian, edited by Justin(Jumza)

from .parts import *
import random
import typing
#Randomizer can generate ACs with weighting on Specific tiers. Check Parts.py to see Tiers of parts.

def get_random_head_by_tier():
    tiers = [1, 2, 3, 4] 
    tier_weights = [100, 0, 0, 0] # %chance of each part being selected by the tier.  50, 50, 0 ,0 for example means that you have 50% chance of getting a T1 or T2 Part. No T3 or T4 in Pool.

    selected_tier = random.choices(tiers, weights = tier_weights, k=1)[0]

    if selected_tier == 1:
        eligible_heads = heads_by_tier[1]
    elif selected_tier == 2:
        eligible_heads = heads_by_tier[2]
    elif selected_tier == 3:
        eligible_heads = heads_by_tier[3]
    elif selected_tier == 4:
        eligible_heads = all_heads
    else:
        return None
    

    return random.choice(eligible_heads)

def get_random_core_by_tier():
    tiers = [1, 2]
    tier_weights = [50, 50]

    selected_tier = random.choices(tiers, weights = tier_weights, k=1)[0]

    if selected_tier == 1:
        eligible_cores = cores_by_tier[1]
    elif selected_tier == 2:
        eligible_cores  = all_cores
    else:
        return None

    return random.choice(eligible_cores)

def get_random_arms_by_tier():
    tiers = [1, 2, 3, 4]
    tier_weights = [100, 0, 0, 0]

    selected_tier = random.choices(tiers, weights = tier_weights, k=1)[0]

    if selected_tier == 1:
        eligible_Arms = arms_by_tier[1]
    elif selected_tier == 2:
        eligible_Arms = arms_by_tier[2]
    elif selected_tier == 3 or selected_tier == 4:
        eligible_Arms  = all_arms
    else:
        return None

    return random.choice(eligible_Arms)

def get_random_legs_by_tier():
    tiers = [1, 2, 3, 4]
    tier_weights = [100, 0, 0, 0]

    selected_tier = random.choices(tiers, weights = tier_weights, k=1)[0]

    if selected_tier == 1:
        eligible_Legs = legs_by_tier[1]
    elif selected_tier == 2:
        eligible_Legs = legs_by_tier[2]
    elif selected_tier == 3:
        eligible_Legs  = legs_by_tier[3]
    elif selected_tier == 4:
        eligible_Legs = legs_by_tier[4]

    else:
        return None

    return random.choice(eligible_Legs)

def get_random_booster_by_tier():
    tiers = [1, 2, 3]
    tier_weights = [100, 0, 0]

    selected_tier = random.choices(tiers, weights = tier_weights, k=1)[0]

    if selected_tier == 1:
        eligible_booster = booster_by_tier[1]
    elif selected_tier == 2:
        eligible_booster = booster_by_tier[2]
    elif selected_tier == 3:
        eligible_booster  = all_boosters
    else:
        return None

    return random.choice(eligible_booster)

def get_random_generator_by_tier():
    tiers = [1, 2, 3, 4]
    tier_weights = [100, 0, 0, 0]

    selected_tier = random.choices(tiers, weights = tier_weights, k=1)[0]

    if selected_tier == 1:
        eligible_generators = generator_by_tier[1]
    elif selected_tier == 2:
        eligible_generators = generator_by_tier[2]
    elif selected_tier == 3 or selected_tier == 4:
        eligible_generators = all_generators
    else:
        return None

    return random.choice(eligible_generators)

def get_random_FCS_by_tier():
    tiers = [1, 2, 3]
    tier_weights = [100, 0, 0]

    selected_tier = random.choices(tiers, weights = tier_weights, k=1)[0]

    if selected_tier == 1:
        eligible_FCS = fcs_by_tier[1]
    elif selected_tier == 2:
        eligible_FCS = fcs_by_tier[2]
    elif selected_tier == 3:
        eligible_FCS  = all_fcs
    else:
        return None

    return random.choice(eligible_FCS)

def get_random_Arm_Weapon_R_by_tier():
    tiers = [1, 2, 3, 4]
    tier_weights = [100, 0, 0, 0]

    selected_tier = random.choices(tiers, weights = tier_weights, k=1)[0]

    if selected_tier == 1:
        eligible_Arm_r = arm_weapon_r_by_tier[1]
    elif selected_tier == 2:
        eligible_Arm_r = arm_weapon_r_by_tier[2]
    elif selected_tier == 3:
        eligible_Arm_r = arm_weapon_r_by_tier[3]
    elif selected_tier == 4:
        eligible_Arm_r = all_arm_weapon_rs
    else:
        return None

    return random.choice(eligible_Arm_r)

def get_random_Arm_Weapon_L_by_tier():
    tiers = [1, 2, 3]
    tier_weights = [100, 0, 0]

    selected_tier = random.choices(tiers, weights = tier_weights, k=1)[0]

    if selected_tier == 1:
        eligible_Arm_l = arm_weapon_l_by_tier[1]
    elif selected_tier == 2:
        eligible_Arm_l = arm_weapon_l_by_tier[2]
    elif selected_tier == 3:
        eligible_Arm_l = arm_weapon_l_by_tier[3]
    elif selected_tier == 4:
        eligible_Arm_l = all_arm_weapon_ls
    else:
        return None

    return random.choice(eligible_Arm_l)

def get_Back_Weapon_by_tier(guarantee_unlocked, RADAR):
    tiers = [1, 2, 3, 4]
    tier_weights = [100, 0, 0, 0]
      
    selected_tier = random.choices(tiers, weights = tier_weights, k=1)[0]

    if selected_tier == 1:
        eligible_Back_Weapon = back_weapon_by_tier[1]
    elif selected_tier == 2:
        eligible_Back_Weapon = back_weapon_by_tier[2]
    elif selected_tier == 3:
        eligible_Back_Weapon = back_weapon_by_tier[3]
    elif selected_tier == 4:
        eligible_Back_Weapon = all_back_weapons
    else:
        return None

    back_weapon = random.choice(eligible_Back_Weapon)

    if guarantee_unlocked:
        if back_weapon.fire_unlocked == False:
            back_weapon_inelgible = True
        else:
            back_weapon_inelgible = False
        while (back_weapon_inelgible):
            back_weapon = random.choice(eligible_Back_Weapon)
            if back_weapon.fire_unlocked == False:
                back_weapon_inelgible = True
            else:
                back_weapon_inelgible = False
    
    if RADAR:
        if back_weapon.part_type == "RADAR":
            back_weapon_inelgible = True
        else:
            back_weapon_inelgible = False
        while (back_weapon_inelgible):
            back_weapon = random.choice(eligible_Back_Weapon)
            if back_weapon.part_type == "RADAR":
                back_weapon_inelgible = True
            else: 
                back_weapon_inelgible = False


    #print(f"Selected tier: {selected_tier}")
    #print(f"Eligible weapons for this tier: {eligible_Back_Weapon}")
    #print(guarantee_unlocked)

    return back_weapon


def generate_AC():
    ac_head = get_random_head_by_tier()
    ac_core = get_random_core_by_tier()
    ac_arms = get_random_arms_by_tier()
    ac_legs = get_random_legs_by_tier()
    ac_booster = get_random_booster_by_tier()
    ac_generator = get_random_generator_by_tier()
    ac_FCS = get_random_FCS_by_tier()
    ac_arm_weapon_r = get_random_Arm_Weapon_R_by_tier()
    ac_arm_weapon_l = get_random_Arm_Weapon_L_by_tier()

    ac_arm_weapon_r_status = "VALID"
    ac_arm_weapon_l_status = "VALID"
    ac_back_weapon_r_status = "VALID"
    ac_back_weapon_l_status = "VALID"
    percentage_chance_r = 80  #Base Percentage chances can me modified here. Logic will still give 100% for specific parts if rolls are unsuccessful.
    percentage_chance_l = 50
    percentage_chance_back_r = 50
    percentage_chance_back_l = 33

    ac_remaining_weight = ac_legs.max_weight - ac_core.weight - ac_generator.weight - ac_arms.weight - ac_booster.weight - ac_head.weight - ac_FCS.weight

    ac_core_weight = ac_core.max_weight - ac_arms.weight

    ac_remaining_energy = ac_generator.energy_output - ac_core.energy_drain - ac_legs.energy_drain - ac_arms.energy_drain - ac_booster.energy_drain - ac_head.energy_drain - ac_FCS.energy_drain
    
    if  ac_arms.part_type == "ARM UNIT":
        if  0 <= percentage_chance_r <= 100:
            ac_arm_weapon_r = get_random_Arm_Weapon_R_by_tier()
        if random.random() < percentage_chance_r / 100:
                ac_remaining_weight -= ac_arm_weapon_r.weight
        else:
            ac_arm_weapon_r_status = "NO EQUIP"

        if 0 <= percentage_chance_l <= 100: #Laser Blade Guaranteed if Arm Weapon R is not generated.
            if ac_arm_weapon_r_status == "NO EQUIP":
                percentage_chance_l = 100
            ac_arm_weapon_l = get_random_Arm_Weapon_L_by_tier()
            if random.random() < percentage_chance_l / 100:
                ac_remaining_weight -= ac_arm_weapon_l.weight
            else:
                ac_arm_weapon_l_status = "NO EQUIP"

    if ac_arms.part_type != "ARM UNIT": #Flag for Weapon names 
        ac_arm_weapon_r_status = "EQUIPMENT IMPOSSIBLE"
        ac_arm_weapon_l_status = "EQUIPMENT IMPOSSIBLE"


# Back Weapon is 100% Chance if Weapon arms are present or only one arm is present. Will also guarantee a fire unlocked weapon if AC has none currently.

    if ac_arm_weapon_l_status == "NO EQUIP" or ac_arm_weapon_l_status == "EQUIPMENT IMPOSSIBLE" or ac_arm_weapon_r_status == "NO EQUIP" or ac_arm_weapon_r_status == "EQUIPMENT IMPOSSIBLE":    
        percentage_chance_back_r = 100
    ac_back_weapon_r = get_Back_Weapon_by_tier(guarantee_unlocked = ac_arms.part_type != "ARM UNIT", RADAR = False)
    if random.random() < percentage_chance_back_r / 100:
        ac_remaining_weight -= ac_back_weapon_r.weight 
    
    else : 
        ac_back_weapon_r_status = "NO EQUIP"

    #print (percentage_chance_back_r)    

# If Back Weapon R is generated as a RADAR. 100% chance of getting a back weapon that can deal damage. 

    if ac_back_weapon_r.part_type == "RADAR":
        percentage_chance_back_l = 100
    ac_back_weapon_l = get_Back_Weapon_by_tier(guarantee_unlocked = False, RADAR = True)
    if random.random() < percentage_chance_back_l / 100:
        ac_remaining_weight -= ac_back_weapon_l.weight
    
    else : 
        ac_back_weapon_l_status = "NO EQUIP"

    if ac_arm_weapon_r == True:
        ac_remaining_energy -= ac_arm_weapon_r.energy_drain

    if ac_arm_weapon_l == True:
        ac_remaining_energy -= ac_arm_weapon_l.energy_drain
    if ac_back_weapon_r == True:
        ac_remaining_energy -= ac_back_weapon_r.energy_drain
    if ac_back_weapon_l == True:
        ac_remaining_energy -= ac_back_weapon_l.energy_drain

    if ac_arms.part_type != "ARM UNIT": #Flag for Weapon names 
        ac_arm_weapon_r_status = "EQUIPMENT IMPOSSIBLE"
        ac_arm_weapon_l_status = "EQUIPMENT IMPOSSIBLE"

    if ac_arms.part_type == "ARM UNIT":
        ac_core_weight -= ac_arm_weapon_r.weight - ac_arm_weapon_l.weight

    if (ac_remaining_weight < 0 or ac_core_weight < 0 or ac_remaining_energy < 0):
        invalid_AC = True
    else:
        invalid_AC = False

    return (invalid_AC, ac_head, ac_core, ac_arms, ac_legs, ac_booster, ac_generator, ac_FCS, ac_arm_weapon_r, ac_arm_weapon_l, ac_back_weapon_r, ac_back_weapon_l, ac_remaining_weight, ac_core_weight, ac_remaining_energy, ac_arm_weapon_r_status, ac_arm_weapon_l_status, ac_back_weapon_r_status, ac_back_weapon_l_status)


def randomize_start_parts():
    (invalid_AC, ac_head, ac_core, ac_arms, ac_legs, ac_booster, ac_generator, ac_FCS, ac_arm_weapon_r, ac_arm_weapon_l, ac_back_weapon_r, ac_back_weapon_l, ac_remaining_weight, ac_core_weight, ac_remaining_energy, ac_arm_weapon_r_status, ac_arm_weapon_l_status, ac_back_weapon_r_status, ac_back_weapon_l_status) = generate_AC()
    
    while invalid_AC == True:
        print ("Invalid AC Detected: Retrying...")
        (invalid_AC, ac_head, ac_core, ac_arms, ac_legs, ac_booster, ac_generator, ac_FCS, ac_arm_weapon_r, ac_arm_weapon_l, ac_back_weapon_r, ac_back_weapon_l, ac_remaining_weight, ac_core_weight, ac_remaining_energy, ac_arm_weapon_r_status, ac_arm_weapon_l_status, ac_back_weapon_r_status, ac_back_weapon_l_status) = generate_AC()

    if ac_arm_weapon_l_status == "NO EQUIP":
        ac_arm_weapon_l = "NO EQUIP"
    if ac_arm_weapon_l_status == "EQUIPMENT IMPOSSIBLE":
        ac_arm_weapon_l = "EQUIPMENT IMPOSSIBLE"
    
    if ac_arm_weapon_r_status == "NO EQUIP":
        ac_arm_weapon_r = "NO EQUIP"
    if ac_arm_weapon_r_status == "EQUIPMENT IMPOSSIBLE":
        ac_arm_weapon_r = "EQUIPMENT IMPOSSIBLE"
    
    if ac_back_weapon_r_status == "NO EQUIP":
        ac_back_weapon_r = "NO EQUIP"
    if ac_back_weapon_l_status == "NO EQUIP":
        ac_back_weapon_l     = "NO EQUIP"

    print (ac_head.name)
    print (ac_core.name)
    print (ac_arms.name)
    print (ac_legs.name)
    print (ac_booster.name)
    print (ac_generator.name)
    print (ac_FCS.name)
    print (ac_arm_weapon_r)
    print (ac_arm_weapon_l)
    print (ac_back_weapon_r)
    print (ac_back_weapon_l)
    
    print(f"Remaining Weight:", ac_remaining_weight, f"Remaining Arm Weight:", ac_core_weight, f"Remaining Energy:", ac_remaining_energy)

    new_start_parts: typing.Tuple[Part, ...] = {ac_head, ac_core, ac_arms, ac_legs, ac_booster, ac_generator, ac_FCS, ac_arm_weapon_r, ac_arm_weapon_l, ac_back_weapon_r, ac_back_weapon_l}

    return new_start_parts