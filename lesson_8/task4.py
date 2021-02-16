"""
Начните работу над проектом «Склад оргтехники».
Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определите параметры, общие для приведённых типов.
В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.
"""


class Storage:
    def __init__(self, list_nomenclature, adress):
        self.positions = list_nomenclature
        self.adress = adress

    def __str__(self):
        return f"Адрес склада и хранимые в нем позиции {self.adress} {self.positions}"


class OfficeEquipment:
    def __init__(self, brand, model, adoption_year, lan_type=None):
        self.brand = brand
        self.model = model
        self.lan_type = lan_type
        self.adoption_year = adoption_year

    def __str__(self):
        return self.brand, self.model, self.adoption_year, self.lan_type

class Printer(OfficeEquipment):
    def __init__(self, brand, model, adoption_year, lan_type=None, color=True, species="laser"):
        super().__init__(brand, model, adoption_year, lan_type)
        self.color = color
        self.species = species


class Xerox(OfficeEquipment):
    def __init__(self, brand, model, adoption_year, lan_type=None, color=False, bilateral=False):
        super().__init__(brand, model, adoption_year, lan_type)
        self.color = color
        self.bilateral = bilateral


class Scaner(OfficeEquipment):
    def __init__(self, brand, model, adoption_year, lan_type, dpi, streaming=False):
        super().__init__(brand, model, adoption_year, lan_type)
        self.dpi = dpi
        self.streaming = streaming


reseption_printer = Printer("Самсунг", "svr101010", 2020, lan_type="wi-fi", species="jet")
main_xerox = Xerox("LG", "awesome_model", adoption_year=2021, color=True, bilateral=True)
reserved_scan = Scaner("Xiaomi", "mi-redmi-note-plus-ultra-turbo-28", 2019, "ethernet + wifi", 20000, True)

sclad1 = Storage([], "Mayakovskaya d.1")
sclad1.positions.append(reserved_scan)
sclad1.positions.append(main_xerox)
sclad1.positions.append(reseption_printer)
print(sclad1)
