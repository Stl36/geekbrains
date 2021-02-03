"""
7. Создать (не программно) текстовый файл,
в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.

Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список.
Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:

[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджеры контекста.
"""

import json


def calc_profit(line_: str):
    proceeds = int(line_.split()[2])
    costs = int(line_.split()[3])
    return proceeds - costs


def get_company_name(line_: str):
    return line_.split()[0]


my_l = []
with open("new_f7.txt", "r", encoding="utf8") as f_obj:
    for line in f_obj:
        my_l.append(line)
firms_dict = {}
for line in my_l:
    firms_dict[get_company_name(line)] = calc_profit(line)
average_profit_list = {}
average_profit_list["average_profit"] = sum(firms_dict.get(i) for i in firms_dict.keys() if firms_dict.get(i) > 0)
out_list = [firms_dict, average_profit_list]

with open("my_file.json", "w") as write_f:
    json.dump(out_list, write_f)
