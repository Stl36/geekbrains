"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def devision_elements(numerator, denominator):
    if denominator != 0:
        return numerator / denominator
    else:
        return 'Деление на 0 запрещено'


numerator, denominator = int(input("Введите числитель ")), int(input("Введите знаменатель "))
print(devision_elements(numerator, denominator))