# revenue = int(input('Revenue: '))
# expenses = int(input('Expenses '))

revenue = 1000
expenses = 500

if revenue > expenses:
    print('Прибыль')
    profitability = revenue / expenses
    print('Рентабельность компании:', profitability)
    # employees = int(input("Количество сотрудников: "))
    employees = 5  # по умолчанию 5ть сотрудников для теста
    print('Прибыль на одного сотрудника:', (revenue - expenses) / employees)
else:
    print('Убыток')
