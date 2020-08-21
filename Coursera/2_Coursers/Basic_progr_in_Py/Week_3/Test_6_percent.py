Percent = int(input())
Rubles = int(input())
Kopeck = int(input())


def deposit_amount_year(percent, rubles, kopeck):
    all_kopecks = int(((rubles * 100 + kopeck) * (percent + 100)) / 100)
    return all_kopecks // 100, all_kopecks % 100


rub, kop = deposit_amount_year(Percent, Rubles, Kopeck)
print(rub, kop)
