"""
1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""


def w_file(u_str: str):
    if u_str == "":
        return 1
    else:
        f_obj = open("new_f1.txt", 'a')
        f_obj.write(u_str + "\n")
        f_obj.close()


f = 0
while not f:
    string_ = input()
    f = w_file(string_)
