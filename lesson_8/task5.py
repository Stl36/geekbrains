"""
Продолжить работу над первым заданием.
Разработайте методы, которые отвечают за приём оргтехники на склад и передачу в определённое подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру (например, словарь).
"""


class Storage:
    def __init__(self, adress):
        self.positions = dict()
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


reseption_printer = Printer("Самсунг", "svr101010", 2020, "Office", lan_type="wi-fi", species="jet")
main_xerox = Xerox("LG", "awesome_model", 2021, "Office", color=True, bilateral=True)
reserved_scan = Scaner("Xiaomi", "mi-redmi-note-plus-ultra-turbo-28", 2019, "ethernet + wifi", 20000, True)
main_storage = Storage("Mayakovskaya d.1")

main_storage.show_units_in_storeage(main_xerox)
main_storage.accept_unit(reserved_scan)
print(reserved_scan)
main_storage.accept_unit(reseption_printer)
main_storage.accept_unit(main_xerox)
main_storage.accept_unit(main_xerox)
print(main_xerox)
main_storage.show_units_in_storeage(main_xerox)
main_storage.list_of_positions()
main_storage.deregister_unit(reserved_scan)
main_storage.deregister_unit(reserved_scan)
print(reserved_scan)
main_storage.list_of_positions()