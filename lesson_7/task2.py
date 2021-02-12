"""
Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""


from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def consumption(self):
        pass


class Caot(Clothes):
    def __init__(self, name, v):
        self.name = name
        self.size = v

    @property
    def consumption(self):
        return self.size / 6.5 + 0.5


class Costume(Clothes):
    def __init__(self, name, h):
        self.name = name
        self.size = h

    @property
    def consumption(self):
        return self.size * 2 + 0.3


my_fabric1 = Caot("Рубин", 46)
my_fabric2 = Costume("Ирис", 178)

print(f"Общий расход ткани для изделий {my_fabric1.name} и {my_fabric2.name} составляет "
      f"{(my_fabric1.consumption + my_fabric2.consumption):.2f} единиц чего-то там")