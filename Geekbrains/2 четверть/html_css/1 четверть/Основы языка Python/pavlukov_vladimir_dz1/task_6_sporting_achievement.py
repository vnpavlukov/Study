"""6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров. Каждый день
спортсмен увеличивал результат на 10 % относительно предыдущего. Требуется определить номер дня, на который общий
результат спортсмена составить не менее b километров. Программа должна принимать значения параметров a и b и выводить
одно натуральное число — номер дня.
Например: a = 2, b = 3.
Результат:
1-й день: 2
2-й день: 2,2
3-й день: 2,42
4-й день: 2,66
5-й день: 2,93
6-й день: 3,22
Ответ: на 6-й день спортсмен достиг результата — не менее 3 км."""

# first_day_result = int(input('Revenue: '))
# goal = int(input('Expenses '))

start_result = 2
goal = 3


def print_day_achieve_the_goal(first_day_result, target):
    current_day_result = first_day_result
    current_day = 1
    while current_day_result < target:
        # print(f'{current_day}-й день: {current_day_result:0.2f}')
        current_day_result *= 1.1
        current_day += 1
    # print(f'{current_day}-й день: {current_day_result:0.2f}')
    print(f'на {current_day}-й день спортсмен достиг результата — не менее {int(current_day_result)} км.')


print_day_achieve_the_goal(start_result, goal)
