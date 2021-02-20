"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

31 22
37 43
51 86

3 5 32
2 4 6
-1 64 -8

3 5 8 3
8 3 7 1

Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
(двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
складываем с первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return "\n".join(" ".join(str(elem) for elem in row) for row in self.matrix)

    def __add__(self, other):
        if len(self.matrix) != len(other.matrix):
            raise ValueError("Размеры матриц должны быть одинаковыми!")
        for i, row in enumerate(self.matrix):
            if len(row) != len(other.matrix[i]):
                raise ValueError("Размеры матриц должны быть одинаковыми!")

        matrix_out = []
        for i, row in enumerate(self.matrix):
            matrix_out.append(row.copy())
            for j, elem in enumerate(row):
                matrix_out[i][j] = matrix_out[i][j] + other.matrix[i][j]
        return Matrix(matrix_out)


m1 = Matrix([[1, 2, 3], [2, 3, 4], [4, 5, 6]])
m2 = Matrix([[9, 2, 9], [7, 0, 4], [1, 5, 8]])
print(m1, "\n")
print(m2, "\n")
print(m1 + m2)