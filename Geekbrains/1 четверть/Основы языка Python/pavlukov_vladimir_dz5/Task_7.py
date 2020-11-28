"""

7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма
собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила
убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""
import json

file_name_task_7 = 'task_7.txt'

with open(file_name_task_7, 'r', encoding="utf8") as f:
    objects_and_loads = dict()

    number_of_firms_with_profit = 0
    total_profit = 0
    firm_data = dict()

    for line in f:
        split_line = line.split()
        name = split_line[0]
        profit = int(split_line[2]) - int(split_line[3])

        if profit >= 0:
            number_of_firms_with_profit += 1
            total_profit += profit
        firm_data[name] = profit

    average_profit = total_profit / number_of_firms_with_profit
    firm_data['average_profit'] = average_profit

print(firm_data)


def write_data_in_file(data, f_name):
    with open(f_name, 'w', encoding='utf8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


write_data_in_file(firm_data, 'test_7_out.json')
