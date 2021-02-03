"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""


from random import randint


def print_random_numbers_to_file(file_name:str):
    with open(file_name, "a") as f_obj:
        limit = randint(5, 100)
        for number in range(limit):
            print(f"{randint(0, 100)}" , end=' ', file=f_obj)


def calc_sum_numbers_from_file(file_name:str):
    with open(file_name, "r") as f_obj:
        return sum([int(i) for i in f_obj.readline().split()])


file_name = "new_f5.txt"
print_random_numbers_to_file(file_name)
print(calc_sum_numbers_from_file(file_name))