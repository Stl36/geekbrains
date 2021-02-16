"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
Проверьте его работу на данных, вводимых пользователем.
При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class MyZeroDivisionError(Exception):
    def __init__(self, txt): # обязателен ли такой конструктор для данного exception-а?
        self.txt = txt

my_number = 89087

try:
    my_divisor = input("Введите делитель ")
    my_divisor = int(my_divisor)
    if my_divisor == 0:
        print(MyZeroDivisionError("Зафиксирована попытка деления на ноль. Записал IP, за Вами выехали"))
    else:
        print(my_number / my_divisor)

except Exception as myerr:
    print(myerr)

# такая реализация корректа?