"""1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
(двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д."""


class Matrix:
    def __init__(self, matrix_data):
        self.matrix_data = matrix_data

    def __add__(self, other):
        a = self.matrix_data
        b = other.matrix_data
        new_matrix_data = [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(b))]
        return Matrix(new_matrix_data)


a = [[1, 1, 1],
     [2, 2, 2],
     [2, 2, 2],
     [2, 2, 2]]

b = [[1, 1, 1],
     [2, 2, 2],
     [2, 2, 2],
     [2, 2, 2]]

a_1 = Matrix(a)
b_1 = Matrix(b)
sum_a_b = a_1 + b_1
print(sum_a_b.matrix_data)
