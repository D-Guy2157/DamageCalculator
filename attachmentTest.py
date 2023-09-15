class Weapon:
    """The class for weapon and weapon stats"""

    def __init__(self, name, penetration, damage, mag_size, fire_rate, weight, length, equip_time, bullet_accuracy,
                 hip_fire_accuracy, aiming_accuracy, running_accuracy, **attachments):
        self.name = name
        self.penetration = penetration
        self.damage = damage
        self.mag_size = mag_size
        self.fire_rate = fire_rate
        self.weight = weight
        self.length = length
        self.equip_time = equip_time
        self.bullet_accuracy = bullet_accuracy
        self.hip_fire_accuracy = hip_fire_accuracy
        self.aiming_accuracy = aiming_accuracy
        self.running_accuracy = running_accuracy
        self.attachments = attachments or {}


class Armor:
    """The class for the 3 types of armor"""

    def __init__(self, name, body_protection, head_protection, limb_protection):
        self.name = name
        self.body_protection = body_protection
        self.head_protection = head_protection
        self.limb_protection = limb_protection


com_15 = Weapon('COM-15', 20, 25, 12, 300, 0.65, 18, 0.5, 0.2, 1.7, 0.25, 2.4,
                barrel={'Standard Barrel': (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
                        'Suppressor': (0, 0, 0, 0, '46%', '94%', 0.17, '25%', 0, 0, 0)},
                side={'None': (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
                      'Flashlight': (0, 0, 0, 0, '31%', 0, 0, 0.03, 0, 0, 0)},
                magazine={'JHP Magazine': (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
                          'Extended JHP Magazine': (0, 0, 5, 0, '46%', 0, 0.06, 0, 0, 0)},
                )
# Using tuple for stats, going to use same order as class stats, dumb solution, but hopefully it works
# pen, dmg, mag, rof, weight, length, equip, bul_acc, hip_acc, aim_acc, run_acc
test = ({'barrel': {'Standard Barrel': (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
                    'Suppressor': (0, 0, 0, 0, '46%', '94%', 0.17, '25%', 0, 0, 0)},
         'side': {'None': (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
                  'Flashlight': (0, 0, 0, 0, '31%', 0, 0, 0.03, 0, 0, 0)},
         'magazine': {'JHP Magazine': (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
                      'Extended JHP Magazine': (0, 0, 5, 0, '46%', 0, 0.06, 0, 0, 0)}})
# Losing my mind
print(f"Full: {com_15.attachments}")
print(f"Keys: {com_15.attachments.keys()}")
print(f"Values: {com_15.attachments.values()}")
print(f"Get: {com_15.attachments.get('barrel').get('Standard Barrel')}")
# Ok so this WORKS but im not sure if i want to do this for all attachment values
# im not sure what else to do at this point though
