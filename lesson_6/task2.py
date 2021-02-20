"""
Реализовать класс Road (дорога).

определить атрибуты: length (длина), width (ширина);
значения атрибутов должны передаваться при создании экземпляра класса;
атрибуты сделать защищёнными;
определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом,
толщиной в 1 см*число см толщины полотна;
проверить работу метода.

Например: 20 м*5000 м*25 кг*5 см = 12500 т.

"""
class Road:

    def __init__(self, l, w, d = 25, t = 5):
        self.__length = l
        self.__width = w
        self.__density = d
        self.__thickness = t

    def calc_mass(self, t = 5):
        self.__thickness = t
        return (self.__length * self.__width * self.__density * self.__thickness)


el_1 = Road(5000, 20)
print(el_1.__dict__)
print(el_1.calc_mass(25))
