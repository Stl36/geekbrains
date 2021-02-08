"""
Реализуйте базовый класс Car.

у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Вызовите методы и покажите результат.
"""


class Car:

    def __init__(self, speed: int, color: str, name: str, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"{self.color} {self.name} поехал")

    def stop(self):
        print(f"{self.color} {self.name} остановился")

    def turn(self, direction:str):
        print(f"{self.color} {self.name} повернул {direction}")

    def show_speed(self):
        print(f"Скорость {self.color} {self.name} составляет {self.speed}")


class SportCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)


class TownCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print(f"Скорость превышена на {self.speed - 60}")


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print(f"Скорость превышена на {self.speed - 40}")


car_petya = SportCar(320, "red", "Ferrari", True)
car_vasya = PoliceCar(110, "blue", "LADA")
car_ivan = TownCar(193, "white", "RENO")
car_nikolay = WorkCar(44, "green", "Kamaz", False)
car_petya.show_speed()
car_vasya.show_speed()
car_ivan.show_speed()
car_nikolay.show_speed()
print(f"{car_petya.__dict__}\n"
      f"{car_vasya.__dict__}\n"
      f"{car_ivan.__dict__}\n"
      f"{car_nikolay.__dict__}\n")
car_nikolay.go()
car_ivan.stop()
car_vasya.turn("налево")
car_petya.turn("направо")