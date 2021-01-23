"""
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел,
то вначале нужно добавить сумму этих чисел к полученной ранее сумме
и после этого завершить программу.
"""


def input_list():
    return [i for i in input("Введите список чисел\nДля завершения введите q\n").split()]


def update_list(input_list):
    return [int(i) for i in input_list]


def q_remove(input_list):
    return input_list.remove("q")


def q_search(input_list):
    if "q" in input_list:
        q_remove(input_list)
        return True
    else:
        return False


def add_sum(input_list):
    localSum = 0
    for x in input_list:
        localSum += x
    return localSum


saveSum = 0
flag = False
getList = []
while flag != True:
    getList = input_list()
    flag = q_search(getList)
    getList = update_list(getList)
    saveSum += add_sum(getList)
    print(f"Cумма всех элементов {saveSum} \n")