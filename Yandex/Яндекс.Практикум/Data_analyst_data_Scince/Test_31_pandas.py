import pandas as pd

data = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, '-', '-', '-', 0, 0, 0, 0, 0, 0],
        [0, '-', 'X', '-', 0, 0, 'X', 'X', 'X', 'X'],
        [0, '-', 'X', '-', 0, 0, 0, 0, 0, 0],
        [0, '-', '-', '-', 0, 0, 0, 0, 0, 0],
        [0, 0, '-', 0, 0, 0, 0, 0, 'X', 0],
        [0, '-', 'X', 'X', 0, 0, 0, 0, 0, 0],
        [0, 0, '-', '-', 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, '-', 'X', 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

columns = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'К']

battle = pd.DataFrame(data=data, columns=columns)

# print(battle)
# print()
#
# print(battle.loc[:, 'В'])
# print()
#
# print(battle.loc[5:7])
# print()
#
# print(battle.loc[:, 'А':'Д'])
# print()

# print(battle.loc[:,'В'] == 'X')

var = battle[battle['В'] == 'X']['В'].count()

print(var)
