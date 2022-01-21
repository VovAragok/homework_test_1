class Tomato:
    states = {0: "nothing", 1: "flower", 2: "green tomato", 3: "red tomato"}

    def __init__(self, index):
        self._index = index
        self._states = 0

    def grow(self):
        if self._states < 3:
            self._states += 1

    def print_state(self):
        print(f"Toto index {self._index} is {self._states}")

    def is_ripe(self):
        if self._states == 3:
            return True
        return False


class TomatoBush:

    def __init__(self, col_tomato):
        self.tomatoes = [Tomato(i) for i in range(col_tomato)]  # i - index class Tomato

    def grow_all(self):
        for i in self.tomatoes:
            i.grow()

    def all_are_ripe(self):
        return all([i.is_ripe() for i in self.tomatoes])

    def give_away_all(self):
        self.tomatoes = []


class Gender:

    def __init__(self, name):
        self.name = name
        self._plants = Tomato(self)

    def work(self):
        Tomato.grow(self._plants)

    def harvest(self):
        if TomatoBush.all_are_ripe(TomatoBush(self._plants)) == True:
            TomatoBush.give_away_all(TomatoBush(self._plants))

        else:
            return "Нельзя собрать урожай!!!"

    @staticmethod
    def knowledge_base():
        print(Tomato.states)

t1 = Tomato(index=5)
gen1 = Gender("Миша")
print(gen1.work())