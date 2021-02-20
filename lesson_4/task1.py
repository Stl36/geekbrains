"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""
# -*- coding: UTF-8 -*-
# example script start - python task1.py 160 500 30000


from sys import argv

def calc_salary(hour, rate, bonus):
    return hour * rate + bonus
name_script, hour, rate, bonus = argv
hour = int(hour)
rate = int(rate)
bonus = int(bonus)
print(f"Скрипт {name_script}\n"
      f"Зарплата сотрудника {calc_salary(hour, rate, bonus)}")