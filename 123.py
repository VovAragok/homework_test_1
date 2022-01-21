# Задача 1
#
# Определите три класса: Switzerland, England и Japan.
# Для каждого из них определите всего один метод - currency ().
# Метод должен возвращать значение
# 'franc"(для Switzerland)," pound "(для England) или" yen "(для Japan). ' \
# 'Создайте по одному экземпляру каждого класса и выведите на экран денежную единицу каждой страны.s
#
# class Switzerland:
#     pass
#
#     @staticmethod
#     def currency():
#         return "franc"
#
#
# class England:
#     pass
#
#     @staticmethod
#     def currency():
#         return "pound"
#
#
# class Japan:
#     pass
#
#     @staticmethod
#     def currency():
#         return "yen"
#


# japan_money = Japan.currency()
# england_money = England.currency()
# switzer_money = Switzerland.currency()
# print(japan_money)
# print(england_money)
# print(switzer_money)

#
# class Switzerland:
#     def __init__(self, currency):
#         self.currency = currency
#
#
# class England(Switzerland):
#     def __init__(self, currency):
#         super().__init__(currency)
#
#
# class Japan(Switzerland):
#     def __init__(self, currency):
#         super().__init__(currency)
#
#
# switzer_money = Switzerland("franc")
# print(switzer_money.currency)
# england_money = England("pound")
# print(england_money.currency)
# japan_money = Japan("yen")
# print(japan_money.currency)

# Задача 2
#
# Создайте класс, который называется Element, с методом init,
# что имеет атрибуты экземпляра name, symbol и number.
# Создайте экземпляр этого класса el со значениями 'Silicium "," Si "и 14'
# и выведите на экран значение его атрибутов.

# class Element:
#     def __init__(self, name, symbol, number):
#         self._name = name
#         self._symbol = symbol
#         self._number = number
#
#     @property
#     def result(self):
#         return f"{self._name}, {self._symbol}, {self._number}"
#
#
# el = Element("Silicium", "Si", 14)
# print(el.result)
#
