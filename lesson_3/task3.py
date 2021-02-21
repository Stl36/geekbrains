"""
3. Реализовать функцию my_func(),
которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def my_func(arg1, arg2, arg3):
    inputList = [arg1, arg2, arg3]
    minArg = min([arg1, arg2, arg3])
    inputList.remove(minArg)
    return sum(inputList)


arguments = [int(i) for i in input("Введите 3 числа через пробел\n").split()]
print(my_func(*arguments))