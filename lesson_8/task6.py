"""
Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
"""


class Storage:
    def __init__(self, adress, position):
        if position is None:
            self.positions = dict()
        elif type(position.keys()[0]) != int and position.keys()[0] < 1: # воткнул примитивную проверку. По аналогии можно раскатать на все параметры в любом из классов.
            print(f"Количество единиц должно определятся численными значениями. Вы ввели {position.keys()[0]}")
        else:
            self.positions = position
        self.adress = adress

    def __str__(self):
        return f"Адрес склада {self.adress}"

    def accept_unit(self, unit):
        if unit.place != self.adress:
            if unit.model in self.positions.keys():
                self.positions[unit.model] += 1
            else:
                self.positions[unit.model] = 1
                unit.place = self.adress
        else:
            print(f"{unit.model} уже находится на складе {self.adress}")

    def deregister_unit(self, unit):
        if unit.model in self.positions.keys() and self.positions[unit.model] > 0:
            self.positions[unit.model] -= 1
            unit.place = f"единица ушла со склада {self.adress}"
        else:
            print(f"Единицы {unit.model} нет на складе {self.adress}")

    def show_units_in_storeage(self, unit):
        if unit.model in self.positions.keys() and self.positions[unit.model] > 0:
            print(f"На складе {self.adress} находится {unit.model} в количестве {self.positions[unit.model]}")
        else:
            print(f"На складе {self.adress} позиций {unit.model} не обнаружено")

    def list_of_positions(self):
        for elem in self.positions:
            print(f"{elem} {self.positions[elem]}")


class OfficeEquipment:
    def __init__(self, brand, model, adoption_year, place="Office", lan_type=None):
        self.brand = brand
        self.model = model
        self.lan_type = lan_type
        self.adoption_year = adoption_year
        self.place = place

    def __str__(self):
        return f"{self.brand}, {self.model}, {self.adoption_year}, {self.lan_type}, {self.place}"


class Printer(OfficeEquipment):
    def __init__(self, brand, model, adoption_year, place, lan_type=None, color=True, species="laser"):
        super().__init__(brand, model, adoption_year, place, lan_type)
        self.color = color
        self.species = species


class Xerox(OfficeEquipment):
    def __init__(self, brand, model, adoption_year, place, lan_type=None, color=False, bilateral=False):
        super().__init__(brand, model, adoption_year, place, lan_type)
        self.color = color
        self.bilateral = bilateral


class Scaner(OfficeEquipment):
    def __init__(self, brand, model, adoption_year, place, lan_type, dpi, streaming=False):
        super().__init__(brand, model, adoption_year, place, lan_type)
        self.dpi = dpi
        self.streaming = streaming
