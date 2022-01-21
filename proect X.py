# Напишите программу на Python, которая печатает все числа от 0 до 6, кроме 3 и 6.
# Примечание. Используйте оператор «продолжить».

# for i in range(6):
#     if i == 3 or i == 6:
#         continue
#     else:
#         print(i)
# print(list(filter(lambda x: x != 3 and x != 6, [i for i in range(6 + 1)])))

# Выпринимаете от пользователя последовательность чисел,разделённых запятой.Составьте список и кортеж
# с этими числами.

# a = "1,2,3,4,5,6,7,8,9,10"
# a_tup = tuple(a.split(","))
# a_lst = list(a.split(","))
# print(a_tup)
# print(a_lst)

# Сложите цифры целого числа.
# a = 1234
# i = 0
# result = 0
# c1 = len(str(a))
# # while i < c1:
# #     z = a % 10
# #     a = a//10
# #     i += 1
# #     result += z
# # print(result)

# С помощью анонимной функии извликите числа делимыеп на 15
# import random
# rand = [random.randint(1, 250) for i in range(30)]
# print(rand)
# print(list(filter(lambda x: x % 15 == 0, rand)))


# Нужнопроверить,все ли числа в последовательности уникальны.
# lst1 = [10, 20, 10, 2, 1, 4, 5, 6]
# if len(lst1) == len(set(lst1)):
#     print(True)
# else:
#     print(False)


# программа обЪединяющая словарь
# def add(a, b):
#     a.update(b)
#     return a
#
#
# print(add({"Груша": 4}, {"Виноград": 2}))


# Даны списки:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# Нужно вернуть список,который состоит из элементов,общих для этих двух списков
# result1 = []
# for i in a:
#     if i in b:
#         result1.append(i)
# print(result1)
