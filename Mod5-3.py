import random

class Warrior:

    def __init__(self, name):
        self.name = name
        self.health = 100

    def attacks(self, other):
        if other.health > 0:
            other.health -= 20
            print(f"{self.name} атаковал {other.name}. У {other.name} осталось здоровья {other.health}")


def battle(unit_1, unit_2):
    while unit_1.health > 0 and unit_2.health > 0:
        units = [unit_1, unit_2]
        attack_unit = random.choice(units)
        if attack_unit == unit_1:
            attack_unit.attacks(unit_2)
        else:
            attack_unit.attacks(unit_1)
    if unit_1.health > 0:
        print("Побеждает unit_1")
    else:
        print("Побеждает unit_2")



unit_1 =Warrior("Unit_1")
unit_2 = Warrior("Unit_2")

battle(unit_1,unit_2)