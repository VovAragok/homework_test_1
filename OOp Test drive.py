class Human:
    default_name = "Миша"
    default_age = 34

    def __init__(self, _money, _house, name=default_name, age=default_age):
        self.money = _money
        self.house = _house
        self.name = name
        self.age = age

    def info(self):
        print(f"имя {self.name}, возраст {self.age}, денежных средств {self.money}, дом {self.house}")

    @staticmethod
    def default_info():
        print(f"{Human.default_age}, {Human.default_name}")

    def _make_deal(self):
        pass

    def earn_money(self, give_money):
        self.money += give_money
        return self.money

    def buy_house(self):
        pass


class House:
    def __init__(self, _area, _price):
        self.area = _area
        self.price = _price

    def final_price(self, discount):
        self.price -= (self.price / 100 * discount)
        return self.price


class SmallHouse(House):
    def __init__(self, area, _price):
        self.price = _price
        super().__init__("40м2", self.price)


Human.default_info()

human_1 = Human(50000, 0, "Олег", 20)  # объект человек
Human.info(human_1)
small_house_verona = SmallHouse("40м2", 20000)  # объкет маленький дом
human_1.buy_house()
