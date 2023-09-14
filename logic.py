# Kinda just figuring out the flow of the damage calc as of now
# Terminal Gaming

import math

class Weapon:
    """The class for weapon and weapon stats"""
    def __init__(self, name, penetration, damage, mag_size, fire_rate, weight, length, bullet_accuracy,
                 hip_fire_accuracy, aiming_accuracy, running_accuracy, **attachments):
        self.name = name
        self.penetration = penetration
        self.damage = damage
        self.mag_size = mag_size
        self.fire_rate = fire_rate
        self.weight = weight
        self.length = length
        # Base accuracy
        self.bullet_accuracy = bullet_accuracy
        # Added to bullet acc with rounding
        self.hip_fire_accuracy = hip_fire_accuracy
        # Added to bullet acc without rounding
        self.aiming_accuracy = aiming_accuracy
        # Calc for running accuracy is depending on length and weight (unknown formula)
        self.running_accuracy = running_accuracy
        self.__dict__.update(attachments)

class Armor:
    """The class for the 3 types of armor"""
    def __init__(self, name, body_protection, head_protection, limb_protection):
        self.name = name
        self.body_protection = body_protection
        self.head_protection = head_protection
        self.limb_protection = limb_protection


# name, pen, dmg, mag, rof, weight, length, bul_acc, hip_acc, aim_acc, run_acc, **attachments
# for **attachments, pass through list of available attachments by type -- Figure out how to do stats per attachment :/
# Attachment Order: Sight, Body, Barrel, Stock, Bottom, Side, Magazine, other*
# MTF Firearms
com_15 = Weapon('COM-15', 20, 25, 12, 300, 0.65, 18, 0.2, 1.7, 0.25, 2.4,
                barrel=['Standard Barrel', 'Suppressor'],
                side=['None', 'Flashlight'],
                magazine=['JHP Magazine', 'Extended JHP Magazine'])
com_18 = Weapon('COM-18', 55, 21.2, 15, 420, 0.72, 19, 0.2, 1.7, 0.23, 2.4,
                sight=['Iron Sights', 'Dot Sight'],
                barrel=['Standard Barrel', 'Extended Barrel', 'Suppressor'],
                side=['None', 'Laser Sight', 'Flashlight'],
                magazine=['AP Magazine', 'JHP Magazine', 'Extended AP Magazine', 'Extended JHP Magazine'])
fsp_9 = Weapon('FSP-9', 35, 22.3, 30, 690, 2.45, 45, 0.17, 1.7, 0.4, 2.5,
               sight=['Iron Sights', 'Dot Sight', 'Holographic Sight'],
               barrel=['Standard Barrel', 'Flash Hider', 'Suppressor'],
               stock=['Retracted Stock', 'Extended Stock'],
               bottom=['Retracted Foregrip', 'Foregrip'],
               side=['None', 'Ammo Counter', 'Laser Sight', 'Flashlight'])
crossvec = Weapon('Crossvec', 25, 23.5, 40, 750, 2.65, 61, 0.17, 1.7, 0.2, 2.8,
                  sight=['Iron Sights', 'Holographic Sight', 'Dot Sight', 'Night Vision Scope'],
                  barrel=['Standard Barrel', 'Suppressor', 'Extended Barrel', 'Flash Hider'],
                  stock=['Stock', 'Retracted Stock'],
                  bottom=['None', 'Foregrip', 'Laser Sight', 'Flashlight'],
                  magazine=['JHP Magazine', 'Low-Cap AP Mag'])
mtf_e11_sr = Weapon('MTF-E11-SR', 70, 25.1, 40, 570, 3.15, 87, 0.05, 2, 0.08, 5.8,
                    sight=['Iron Sight', 'Holographic Sight', 'Dot Sight', 'Night-Vision Scope', 'Telescopic Sight'],
                    body=['Carbine Body', 'Rifle Body'],
                    barrel=['Standard Barrel', 'Suppressor', 'Flash Hider', 'Muzzle Booster', 'Muzzle Brake'],
                    stock=['Standard Stock', 'Lightweight Stock', 'Recoil-Reducing Stock'],
                    bottom=['None', 'Foregrip', 'Laser Sight'],
                    side=['None', 'Flashlight', 'Ammo Counter'],
                    magazine=['FMJ Magazine', 'FMJ Drum Magazine', 'Low-Cap JHP Magazine', 'Low-Cap AP Magazine'])
fr_mg_0 = Weapon('FR-MG-0', 80, 22.9, 100, 750, 7.2, 102, 0.05, 3.5, 0.08, 10.9,
                 sight=['Iron Sights', 'Dot Sight', 'Holographic Sight', 'Night Vision Scope', 'Telescopic Sight'],
                 barrel=['Standard Barrel', 'Muzzle Brake', 'Flash Hider', 'Short Barrel', 'Suppressor'],
                 stock=['Standard Stock', 'Heavy Stock'],
                 bottom=['None', 'Foregrip', 'Laser Sight', 'Flashlight'],
                 magazine=['FMJ Drum', 'AP Drum'])
# Chaos Insurgency Firearms
ak = Weapon('AK', 85, 26.2, 30, 498, 3.9, 96, 0.07, 2.5, 0.08, 7.4,
            sight=['Iron Sight', 'Holographic Sight', 'Ammo Counter Sight', 'Telescopic Sight'],
            barrel=['Standard Barrel', 'Extended Barrel', 'Suppressor', 'Muzzle Brake', 'Muzzle Booster'],
            stock=['Standard Stock', 'Heavy Stock', 'No Stock'],
            bottom=['None', 'Foregrip', 'Flashlight', 'Laser'],
            magazine=['Banana AP Mag', 'Banana JHP Mag', 'Drum AP Mag', 'Drum JHP Mag'])
logicer = Weapon('Logicer', 90, 26.8, 100, 660, 11.3, 115, 0.035, 3.5, 0.15, 16.6,
                 sight=['Iron Sights', 'Dot Sight', 'Ammo Counter Sight', 'Night-Vision Scope'],
                 barrel=['Standard Barrel', 'Flash Hider', 'Muzzle Brake', 'Light Barrel'],
                 bottom=['None', 'Foregrip', 'Flashlight', 'Laser Sight'])
shotgun = Weapon('Shotgun', 70, 66.64, 14, 100, 3.95, 74, 0, 0.6, 0.1, 4.,
                 sight=['Iron Sights', 'Holographic Sight'],
                 barrel=['Standard Barrel', 'Choke', 'Extended Barrel'],
                 side=['None', 'Ammo Counter', 'Laser Sight', 'Flashlight'],
                 trigger=['Single-Shot System', 'Double-Shot System'])
revolver = Weapon('.44 Revolver', 65, 57.77, 6, 240, 2.15, 34, 0.15, 2, 0.75, 2.7,
                  sight=['Iron Sights', 'Dot Sight', 'Telescopic Sight'],
                  barrel=['Medium Barrel', 'Long Barrel', 'Short Barrel'],
                  stock=['Standard Stock', 'Heavy Stock'],
                  magazine=['6-Shot Cylinder', '4-Shot Cylinder', '8-Shot Cylinder'])

no_armor = Armor('No Armor', 0, 0, 0)
light_armor = Armor('Light Armor', 40, 0, 0)
combat_armor = Armor('Combat Armor', 60, 80, 0)
heavy_armor = Armor('Heavy Armor', 80, 80, 0)

weapon_list = [com_15, com_18, fsp_9, crossvec, mtf_e11_sr, fr_mg_0, ak, logicer, shotgun, revolver]
armor_list = [no_armor, light_armor, combat_armor, heavy_armor]

print("Welcome to the SCP:SL Damage Calculator\n"
      "v13.2.1\n"
      "Made By: D-Guy (d.guy, formerly D-Guy#2157)")

def choose_weapon():
    """Returns chosen weapon object based on user input"""
    while True:
        for num, weapon in enumerate(weapon_list):
            print(f"{num}. {weapon.name}")
        weapon_choice = input("Choose a weapon (Type either number or name):\n").lower()
        valid_choice = [weapon for weapon in weapon_list if weapon.name.lower() == weapon_choice]
        valid_index = [weapon for num, weapon in enumerate(weapon_list) if str(num) == weapon_choice]
        if not valid_choice and not valid_index:
            print("Invalid input, please try again.")
            continue
        elif valid_choice:
            print(f"You have chosen the {valid_choice[0].name}")
            weapon = valid_choice[0]
            break
        elif valid_index:
            print(f"You have chosen the {valid_index[0].name}")
            weapon = valid_index[0]
            break
        else:
            print("How did you get here")
            exit("Guh??1")
    return weapon

def choose_armor():
    """Returns chosen armor object based on user input"""
    while True:
        for num, armor in enumerate(armor_list):
            print(f"{num}. {armor.name}")
        armor_choice = input("Choose an armor type to test the weapon against (number or name):\n").lower()
        valid_choice = [armor for armor in armor_list if armor.name.lower() == armor_choice]
        valid_index = [armor for num, armor in enumerate(armor_list) if str(num) == armor_choice]
        if not valid_choice and not valid_index:
            print("Invalid input, please try again.")
            continue
        elif valid_choice:
            print(f"You have chosen {valid_choice[0].name}")
            armor = valid_choice[0]
            break
        elif valid_index:
            print(f"You have chosen {valid_index[0].name}")
            armor = valid_index[0]
            break
        else:
            print("How did you get here")
            exit("Guh??2")
    return armor

def choose_attachments():
    """Returns a dict of attachments based on user input"""
    repeat = input(f"Modify attachments for {weapon.name}? (y/n)\n").lower()
    while repeat != 'y' and repeat != 'n':
        repeat = input("Invalid input, try again. (y/n)\n").lower()
    chosen_attachments = {}
    attachment_dict = {}
    print(weapon.__dict__)
    for (i, key) in enumerate(weapon.__dict__):
        # Ideally eventually figure a better way here rather than i < #.
        if i < 11:
            continue
        else:
            attachment_dict.update({key: weapon.__dict__.get(key)})
    while repeat == 'y':
        print(f"Choosing attachments for: {weapon.name}")
        for num, attachment_type in enumerate(attachment_dict):
            print(f"{num}. {attachment_type}")
        while True:
            attachment_type_choice = input("Select a location to modify:\n").lower()
            valid_choice = [attachment_type for attachment_type in attachment_dict.keys() if
                            attachment_type.lower() == attachment_type_choice]
            valid_index = [attachment_type for num, attachment_type in enumerate(attachment_dict) if
                           str(num) == attachment_type_choice]
            if not valid_choice and not valid_index:
                print("Invalid input, please try again.")
                continue
            elif valid_choice:
                print(f"You have chosen {valid_choice[0]}")
                attachment_type = valid_choice[0]
                break
            elif valid_index:
                print(f"You have chosen {valid_index[0]}")
                attachment_type = valid_index[0]
                break
            else:
                print("How did you get here")
                exit("Guh??3")
        while True:
            print(f"Modifying {attachment_type} attachment.")
            for num, attachment in enumerate(attachment_dict.get(attachment_type)):
                print(f"{num}. {attachment}")
            attachment_choice = input("Select the attachment to use:\n").lower()
            valid_choice = [attachment for attachment in attachment_dict.get(attachment_type) if
                            attachment.lower() == attachment_choice]
            valid_index = [attachment for num, attachment in enumerate(attachment_dict.get(attachment_type)) if
                           str(num) == attachment_choice]
            if not valid_choice and not valid_index:
                print("Invalid input, please try again.")
                continue
            elif valid_choice:
                print(f"You have chosen {valid_choice[0]}")
                attachment = valid_choice[0]
                break
            elif valid_index:
                print(f"You have chosen {valid_index[0]}")
                attachment = valid_index[0]
                break
            else:
                print("How did you get here")
                exit("Guh??4")
        chosen_attachments.update({attachment_type: attachment})
        repeat = input("Do you want to continue modifying attachments? (y/n)\n").lower()
        while repeat != 'y' and repeat != 'n':
            repeat = input("Invalid input, try again. (y/n)\n").lower()
    return chosen_attachments

def adjust_stats():
    """WIP: adjusts stats of weapon object based on chosen attachments"""
    pass

def calculate():
    """Calculates damage stats and prints results to screen"""
    damage_reduced = (armor.head_protection * (100 - weapon.penetration)) / 100
    damage_per_shot = (weapon.damage * 2) * (1 - (damage_reduced / 100))
    total_damage = weapon.mag_size * damage_per_shot
    damage_per_second = damage_per_shot * (weapon.fire_rate / 60)
    shots_to_kill = math.ceil((100 / damage_per_shot))
    time_to_kill = (shots_to_kill / (weapon.fire_rate / 60))

    print(f"Headshot Damage Analysis\n"
          f"Reduced: {damage_reduced}%\n"
          f"Per Shot: {round(damage_per_shot, 2)}\n"
          f"Total: {round(total_damage, 2)}\n"
          f"DPS: {round(damage_per_second, 2)}\n"
          f"STK: {shots_to_kill}\n"
          f"TTK: {round(time_to_kill, 2)}\n"
          , end="")

    damage_reduced = (armor.body_protection * (100 - weapon.penetration)) / 100
    damage_per_shot = weapon.damage * (1 - (damage_reduced / 100))
    total_damage = weapon.mag_size * damage_per_shot
    damage_per_second = damage_per_shot * (weapon.fire_rate / 60)
    shots_to_kill = math.ceil((100 / damage_per_shot))
    time_to_kill = (shots_to_kill / (weapon.fire_rate / 60))

    print(f"Bodyshot damage Analysis:\n"
          f"Reduced: {damage_reduced}%\n"
          f"Per Shot: {round(damage_per_shot, 2)}\n"
          f"Total: {round(total_damage, 2)}\n"
          f"DPS: {round(damage_per_second, 2)}\n"
          f"STK: {shots_to_kill}\n"
          f"TTK: {round(time_to_kill, 2)}\n"
          , end="")

    damage_reduced = (armor.limb_protection * (100 - weapon.penetration)) / 100
    damage_per_shot = (weapon.damage * 0.7) * (1 - (damage_reduced / 100))
    total_damage = weapon.mag_size * damage_per_shot
    damage_per_second = damage_per_shot * (weapon.fire_rate / 60)
    shots_to_kill = math.ceil((100 / damage_per_shot))
    time_to_kill = (shots_to_kill / (weapon.fire_rate / 60))

    print(f"Limb Damage Analysis:\n"
          f"Reduced: {damage_reduced}%\n"
          f"Per Shot: {round(damage_per_shot, 2)}\n"
          f"Total: {round(total_damage, 2)}\n"
          f"DPS: {round(damage_per_second, 2)}\n"
          f"STK: {shots_to_kill}\n"
          f"TTK: {round(time_to_kill, 2)}\n"
          , end="")


weapon = choose_weapon()
armor = choose_armor()
attachments_dict = choose_attachments()
adjust_stats()
calculate()
