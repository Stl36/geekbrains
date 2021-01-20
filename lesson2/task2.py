"""
Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""
someList = []
print('Вводите числа по очереди. Для окончания ввода введите " "(пробел) ')
while True:
    element = input("Введите число или пробел ")
    if element == ' ':
        break
    else:
        someList.append(int(element))
for i in range(len(someList)):
    if (i % 2) != 0:
        temp = someList[i - 1]
        someList[i - 1] = someList[i]
        someList[i] = temp
print(someList)