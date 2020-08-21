rub = int(input())
kop = int(input())
number = int(input())

price_kop = rub * 100 + kop
budget_kop = number * price_kop

print(budget_kop // 100, budget_kop % 100)
