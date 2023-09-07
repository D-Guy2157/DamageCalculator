# Kinda just figuring out the flow of the damage calc as of now
# Terminal Gaming

class Weapon:
    """The class for weapon and weapon stats"""
    def __init__(self, name, penetration, damage, mag_size, fire_rate, **attachments):
        self.name = name
        self.penetration = penetration
        self.damage = damage
        self.mag_size = mag_size
        self.fire_rate = fire_rate
        self.__dict__.update(attachments)


# name, pen, dmg, mag, rof, **attachments
# for **attachments, pass through list of available attachments by type
# Generalized Order: Sight, Body, Barrel, Stock, Bottom, Side, Magazine, other*
# MTF Firearms
com_15 = Weapon('COM-15', 20, 25, 12, 300,
                barrel=['Standard Barrel', 'Suppressor'],
                side=['None', 'Flashlight'],
                magazine=['JHP Magazine', 'Extended JHP Magazine'])
com_18 = Weapon('COM-18', 55, 21.2, 15, 420,
                sight=['Iron Sights', 'Dot Sight'],
                barrel=['Standard Barrel', 'Extended Barrel', 'Suppressor'],
                side=['None', 'Laser Sight', 'Flashlight'],
                magazine=['AP Magazine', 'JHP Magazine', 'Extended AP Magazine', 'Extended JHP Magazine'])
fsp_9 = Weapon('FSP-9', 35, 22.3, 30, 690,
               sight=['Iron Sights', 'Dot Sight', 'Holographic Sight'],
               barrel=['Standard Barrel', 'Flash Hider', 'Suppressor'],
               stock=['Retracted Stock', 'Extended Stock'],
               bottom=['Retracted Foregrip', 'Foregrip'],
               side=['None', 'Ammo Counter', 'Laser Sight', 'Flashlight'])
crossvec = Weapon('Crossvec', 25, 23.5, 40, 750,
                  sight=['Iron Sights', 'Holographic Sight', 'Dot Sight', 'Night Vision Scope'],
                  barrel=['Standard Barrel', 'Suppressor', 'Extended Barrel', 'Flash Hider'],
                  stock=['Stock', 'Retracted Stock'],
                  bottom=['None', 'Foregrip', 'Laser Sight', 'Flashlight'],
                  magazine=['JHP Magazine', 'Low-Cap AP Mag'])
mtf_e11_sr = Weapon('MTF-E11-SR', 70, 25.1, 40, 570,
                    sight=['Iron Sight', 'Holographic Sight', 'Dot Sight', 'Night-Vision Scope', 'Telescopic Sight'],
                    body=['Carbine Body', 'Rifle Body'],
                    barrel=['Standard Barrel', 'Suppressor', 'Flash Hider', 'Muzzle Booster', 'Muzzle Brake'],
                    stock=['Standard Stock', 'Lightweight Stock', 'Recoil-Reducing Stock'],
                    bottom=['None', 'Foregrip', 'Laser Sight'],
                    side=['None', 'Flashlight', 'Ammo Counter'],
                    magazine=['FMJ Magazine', 'FMJ Drum Magazine', 'Low-Cap JHP Magazine', 'Low-Cap AP Magazine'])
fr_mg_0 = Weapon('FR-MG-0', 80, 22.9, 100, 750,
                 sight=['Iron Sights', 'Dot Sight', 'Holographic Sight', 'Night Vision Scope', 'Telescopic Sight'],
                 barrel=['Standard Barrel', 'Muzzle Brake', 'Flash Hider', 'Short Barrel', 'Suppressor'],
                 stock=['Standard Stock', 'Heavy Stock'],
                 bottom=['None', 'Foregrip', 'Laser Sight', 'Flashlight'],
                 magazine=['FMJ Drum', 'AP Drum'])
# Chaos Insurgency Firearms
ak = Weapon('AK', 85, 26.2, 30, 498,
            sight=['Iron Sight', 'Holographic Sight', 'Ammo Counter Sight', 'Telescopic Sight'],
            barrel=['Standard Barrel', 'Extended Barrel', 'Suppressor', 'Muzzle Brake', 'Muzzle Booster'],
            stock=['Standard Stock', 'Heavy Stock', 'No Stock'],
            bottom=['None', 'Foregrip', 'Flashlight', 'Laser'],
            magazine=['Banana AP Mag', 'Banana JHP Mag', 'Drum AP Mag', 'Drum JHP Mag'])
logicer = Weapon('Logicer', 90, 26.8, 100, 660,
                 sight=['Iron Sights', 'Dot Sight', 'Ammo Counter Sight', 'Night-Vision Scope'],
                 barrel=['Standard Barrel', 'Flash Hider', 'Muzzle Brake', 'Light Barrel'],
                 bottom=['None', 'Foregrip', 'Flashlight', 'Laser Sight'])
shotgun = Weapon('Shotgun', 70, 66.64, 14, 100,
                 sight=['Iron Sights', 'Holographic Sight'],
                 barrel=['Standard Barrel', 'Choke', 'Extended Barrel'],
                 side=['None', 'Ammo Counter', 'Laser Sight', 'Flashlight'],
                 trigger=['Single-Shot System', 'Double-Shot System'])
revolver = Weapon('.44 Revolver', 65, 57.77, 6, 240,
                  sight=['Iron Sights', 'Dot Sight', 'Telescopic Sight'],
                  barrel=['Medium Barrel', 'Long Barrel', 'Short Barrel'],
                  stock=['Standard Stock', 'Heavy Stock'],
                  magazine=['6-Shot Cylinder', '4-Shot Cylinder', '8-Shot Cylinder'])

weapon_list = [com_15, com_18, fsp_9, crossvec, mtf_e11_sr, fr_mg_0, ak, logicer, shotgun, revolver]

print("Welcome to the SCP:SL Damage Calculator\n"
      "v13.2.1\n"
      "Made By: D-Guy (d.guy, formerly D-Guy#2157)")

while True:
    for num, weapon in enumerate(weapon_list):
        print(f"{num}. {weapon.name}")
    weapon_choice = input("Choose a weapon (Type either number or name):\n").lower()
    valid_choice = [weapon for weapon in weapon_list if weapon.name.lower() == weapon_choice]
    valid_index = [weapon for num, weapon in enumerate(weapon_list) if str(num) == weapon_choice]
    if not valid_choice and not valid_index:
        print("Invalid input, please try again")
        continue
    elif valid_choice:
        print(f"You have chosen the {valid_choice[0].name}")
        break
    elif valid_index:
        print(f"You have chosen the {valid_index[0].name}")
        break
    else:
        print("How did you get here")
        exit()
