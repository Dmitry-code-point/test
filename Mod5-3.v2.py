import random

class Warrior:

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.endurance = 100
        self.armor = 100

    def attacks(self, other):
        return self.get_hit(other)

    def get_hit(self, other):
        if other.armor > 0 and other.endurance > 0:
            other.health -= random.randint(0, 20)
            other.armor -= random.randint(0, 10)
            self.endurance -= 10
            print(f"{self.name} атаковал {other.name}. "
                  f"У {other.name} осталось брони {other.armor}. "
                  f"У {self.name} осталось выносливости {self.endurance}."
                  f"У {other.name} осталось здоровья {other.health}")

        elif other.armor <= 0 and other.endurance > 0:
            other.health -= random.randint(10, 30)
            self.endurance -= 10
            print(
                f"{self.name} атаковал {other.name}."
                f"У {other.name} осталось брони 0."
                f"У {self.name} осталось выносливости {other.endurance}."
                f"У {other.name} осталось здоровья {other.health}")
        else:
            other.health -= random.randint(0, 10)
            self.endurance -= 10
            print(
                f"{self.name} атаковал {other.name}."
                f"У {other.name} осталось брони 0."
                f"У {self.name} осталось выносливости 0."
                f"У {other.name} осталось здоровья {other.health}")

def battle(unit_1, unit_2):
    while unit_1.health > 10 and unit_2.health > 10:
        action1 = random.choice(['attack' , 'defend'])
        action2 = random.choice(['attack' , 'defend'])
        if action1 == "attack" and action2 == "attack":
            unit_1.attacks(unit_2)
            unit_2.attacks(unit_1)

        elif action1 == "attack" and action2 == "defend":
            unit_1.attacks(unit_2)

        elif action1 == "defend" and action2 == "attack":
            unit_2.attacks(unit_1)

        else:
            print(f"Unit_1 защищается и Unit_2 защищается - они ничего не теряют ")
    if unit_1.health > 0:
        print("Побеждает unit_1")
    else:
        print("Побеждает unit_2")



unit_1 =Warrior("Unit_1")
unit_2 = Warrior("Unit_2")

battle(unit_1,unit_2)