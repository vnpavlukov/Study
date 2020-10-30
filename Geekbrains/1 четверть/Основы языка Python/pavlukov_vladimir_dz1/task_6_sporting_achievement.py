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
