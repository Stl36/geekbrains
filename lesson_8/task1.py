"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod.
Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""


class MyDate:
    def __init__(self, date):
        self.date = date

    @staticmethod
    def chek_date(param):
        if "2021" >= param[6:10] >= "1900":
            mouth = param[3:5]
            if ((mouth[:1] == "1") and ("12" >= mouth >= "10")) or ((mouth[:1] == "0") and ("9" >= mouth[1:] >= "1")):
                day = param[:2]
                if (("1" <= day[:1] <= "9") and (day[:1] == "0")) or (("1" <= day[:1] <= "3") and ("10" <= day <= "31")):
                    return True
        return False

    @classmethod
    def int_date(cls, param):
        if MyDate.chek_date(param):
            return int(param[:2]), int(param[3:5]), int(param[6:])
        else:
            raise ValueError("Неверный формат даты. Формат должен быть день-месяц-год, например 01-02-1990")


hb_vasya = MyDate("28-03-1992")
hb_petya = "13-08-1992"
hb_vi = "10-33-2021"
print(hb_vasya.date)
print(MyDate.chek_date(hb_vasya.date))
print(MyDate.chek_date(hb_vi))
print(MyDate.int_date(hb_vasya.date))
print(MyDate.int_date(hb_petya))
print(MyDate.int_date(hb_vi))