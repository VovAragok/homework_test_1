import random
#123
class Warrior:
    object = None
    _health1 = 100
    _damage = 20

    def __init__(self, name):
        self._health = Warrior._health1
        self.name = name
        self._damage = Warrior._damage

    @property
    def info(self):
        return f" {self.name} имеет {self._health} жизни"


War_1 = Warrior("Игорь")
War_2 = Warrior("Карл")
print(War_1)
