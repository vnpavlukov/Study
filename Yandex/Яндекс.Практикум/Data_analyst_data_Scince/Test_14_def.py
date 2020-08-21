rubles_for_dollar = 67.01


def print_budget_in_rubles(dollars):
    rubles = dollars * rubles_for_dollar
    print('Бюджет: {:.2f} млн ₽'.format(rubles))


print('Титаник')
print_budget_in_rubles(200.0)
print()
print('Гладиатор')
print_budget_in_rubles(103.0)
