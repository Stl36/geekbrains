"""
Реализовать класс Stationery (канцелярская принадлежность).

определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
в каждом классе реализовать переопределение метода draw.
Для каждого класса метод должен выводить уникальное сообщение;
создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

"""


class Stationery:

    def __init__(self, tittle):
        self.tittle = tittle

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):

    def __init__(self, tittle):
        super().__init__(tittle)

    def draw(self):
        print(f"Ручка {self.tittle} пишет")


class Pencil(Stationery):

    def __init__(self, tittle):
        super().__init__(tittle)

    def draw(self):
        print(f"Карандаш {self.tittle} рисует")


class Handle(Stationery):

    def __init__(self, tittle):
        super().__init__(tittle)

    def draw(self):
        print(f"Маркер {self.tittle} выделяет")


first = Stationery("Стикер")
second = Pen("Parker")
third = Pencil("Koh-i-Noor")
fourth = Handle("Sharpy")
first.draw()
second.draw()
third.draw()
fourth.draw()