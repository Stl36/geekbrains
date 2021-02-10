"""
6. Необходимо создать (не программно) текстовый файл,
где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран.
Примеры строк файла:

Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —
Пример словаря:

{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}"""


# coding: utf8


def get_course_name(line_: str, char_: str):
    return line_[: line_.find(char_)]


def get_number_from_line(line_: str):
    i = 0
    c = ''
    numbers_set = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
    while i < len(line_):
        if line_[i] in numbers_set:
            c = c + line_[i]
        i += 1
    if c == '':
        return 0
    else:
        return int(c)


def calc_sum_of_split_line(line_: str):
    return sum(get_number_from_line(el) for el in line_.split())


my_l = []
with open("new_f6.txt", "r", encoding="utf8") as f_obj:
    for line in f_obj:
        my_l.append(line)
print(my_l)
final_dict = {}
char = ":"
for line in my_l:
    final_dict[get_course_name(line, char)] = calc_sum_of_split_line(line)

for el in final_dict:
    print(el, final_dict[el])