"""3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
Считаем 3 + 33 + 333 = 369."""

# num_input = int(input())
num_input = int('3')

second = num_input * 10 + num_input
third = num_input * 100 + second

print(num_input + second + third)
