Percent = int(input())
Rubles = int(input())
Kopeck = int(input())
Years = int(input())


def deposit_amount_year(percent, rubles, kopeck, years):
    start_year = 1
    all_kopecks = int(((rubles * 100 + kopeck) * (percent + 100)) / 100)
    while start_year < years:
        all_kopecks = int((all_kopecks * (percent + 100)) / 100)
        start_year += 1
    return all_kopecks // 100, all_kopecks % 100


rub, kop = deposit_amount_year(Percent, Rubles, Kopeck, Years)
print(rub, kop)
