"""3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет
средней величины дохода сотрудников."""

employees_file_name = 'task_3.txt'


def data_from_txt(file_name):
    file = open(file_name, encoding="utf8")
    data = file.read()
    file.close()
    return data


def print_little_receive_average(data):
    split_data = data.split()
    all_income = 0
    num = 0
    for num, employee_data in enumerate(split_data):
        second_name, income = employee_data.split(',')
        all_income += int(income)
        if int(income) < 20000:
            print(f'{second_name} имеет доход: {income}')
    average_income = all_income / (num + 1)
    print(f'\nСредний доход всех сотрудников: {average_income:.2f}')


employees_file_text = data_from_txt(employees_file_name)
print_little_receive_average(employees_file_text)
