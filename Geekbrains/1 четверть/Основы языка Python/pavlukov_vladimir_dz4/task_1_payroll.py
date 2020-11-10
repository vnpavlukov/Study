""" 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника. В расчете
необходимо использовать формулу: (выработка в часах * ставка в час) + премия. Для выполнения расчета для конкретных
значений необходимо запускать скрипт с параметрами."""

import sys


def payroll_accounting(hours, rate, bonus):
    return hours * rate + bonus


if __name__ == '__main__':
    program_name, *inp_args = sys.argv
    input_hours, input_rate = int(inp_args[0]), int(inp_args[1])
    if len(inp_args) == 3:
        input_bonus = int(inp_args[2])
    else:
        input_bonus = 0

    print(payroll_accounting(input_hours, input_rate, input_bonus))
