import pandas as pd
rating = ['date','name','points']
players = [
['2018.01.01',    'Рафаэль Надаль',10645],
['2018.01.08',    'Рафаэль Надаль',    10600],
['2018.01.29',    'Рафаэль Надаль',    9760],
['2018.02.19',    'Роджер Федерер',    10105],
['2018.03.05',    'Роджер Федерер',    10060],
['2018.03.19',    'Роджер Федерер',    9660],
['2018.04.02',    'Рафаэль Надаль',    8770],
['2018.06.18',    'Roger Federer',    8920],
['2018.06.25',    'Рафаэль Надаль',    8770],
['2018.07.16',    'Рафаэль Надаль',    9310],
['2018.08.13',    'Рафаэль Надаль',    10220],
['2018.08.20',    'Рафаэль Надаль',    10040],
['2018.09.10',    'Рафаэль Надаль',    8760],
['2018.10.08',    'Рафаэль Надаль',    8260],
['2018.10.15',    'Рафаэль Надаль',    7660],
['2018.11.05',    'Новак Джокович',    8045],
['2018.11.19',    'Новак Джокович',    9045]
]
tennis = pd.DataFrame(data = players, columns= rating)
print(tennis)
print('-----------------')
print(tennis['name'].unique())

tennis['name'] = tennis['name'].replace('Roger Federer', 'Роджер Федерер')
print('-----------------')
print(tennis['name'].unique())
