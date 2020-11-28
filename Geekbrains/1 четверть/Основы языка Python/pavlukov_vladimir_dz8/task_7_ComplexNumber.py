"""7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа)
и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата."""


class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __str__(self):
        if self.imaginary >= 0:
            return f'{self.real} + {self.imaginary}i'
        else:
            return f'{self.real} - {self.imaginary * -1}i'

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def __mul__(self, other):
        mul_real = self.real * other.real - self.imaginary * other.imaginary
        mul_imaginary = self.real * other.imaginary + other.real * self.imaginary
        return ComplexNumber(mul_real, mul_imaginary)


first_complex = ComplexNumber(2, 3)
second_complex = ComplexNumber(-1, 1)
print(first_complex)

print(first_complex + second_complex)
print(first_complex * second_complex)
