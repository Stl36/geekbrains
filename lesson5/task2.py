"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""


source_f = open("new_f2.txt", "r")
my_f = []
for line in source_f:
    my_f.append(line.replace("\n", ""))

source_f.close()
number_of_string = len(my_f)
talmud = []
for el in my_f:
    k = len(el.split())
    talmud.append(k)

print(f"Строки исходного файла {my_f}\n"
      f"Количество строк {number_of_string}\n"
      f"Количество слов в каждой строке соответственно {talmud}")