"""
Реализовать базовый класс Worker (работник).

определить атрибуты: name, surname, position (должность), income (доход);
последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы:
оклад и премия, например, {"wage": wage, "bonus": bonus};
создать класс Position (должность) на базе класса Worker;
в классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учётом премии (get_total_income);
проверить работу примера на реальных данных: создать экземпляры класса Position,
передать данные, проверить значения атрибутов, вызвать методы экземпляров.

"""


class Worker:

    def __init__(self, name, surname, position, income:dict):
        self.name = name
        self.surname = surname
        self.position = position
        self.__income = income


class Position(Worker):

    def __init__(self, name, surname, position, income):
        super().__init__(name, surname, position, income)
        self.__income = self._Worker__income

    def get_full_name(self):
        return self.name + "\n" + self.surname

    def get_total_income(self):
        return self.__income["wage"] + self.__income["bonus"]


staff_1 = Position("Коба", "Джугашвили", "Агитатор", {"wage": 500, "bonus": 50})
staff_2 = Position("Felix", "Ed", "KGB", {"wage": 400, "bonus": 200})
print(staff_1.get_full_name())
print(staff_1.get_total_income())
print(staff_2.get_full_name())
print(staff_2.get_total_income())