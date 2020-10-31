"""4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции."""

# inp_string = input()
inp_string = '76548932'


def the_biggest_in_string(string):
    number = int(string)
    n_max = number % 10

    while number // 10:
        number //= 10
        n = number % 10
        if n > n_max:
            n_max = n

    return n_max


print(the_biggest_in_string(inp_string))
