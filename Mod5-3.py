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
        action = random.choice(['unit_1' , 'unit_2'])
        if action == "unit_1":
            unit_1.attacks(unit_2)
        else:
            unit_2.attacks(unit_1)
    if unit_1.health > 0:
        print("Побеждает unit_1")
    else:
        print("Побеждает unit_2")



unit_1 =Warrior("Unit_1")
unit_2 = Warrior("Unit_2")

battle(unit_1,unit_2)