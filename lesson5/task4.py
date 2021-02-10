# coding: utf8
"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""


my_l = []
with open(r"new_f4.txt", "r") as f_obj:
    for line in f_obj:
        my_l.append(line.split())
rus_l = ["Один", "Два", "Три", "Четыре"]

for id, el in enumerate(my_l):
    el[0] = rus_l[id]

with open("new_f4_out.txt", "a") as f_out:
    for line in my_l:
        print(f"{line[0]} {line[1]} {line[2]}", file=f_out)

print(my_l)