import pandas as pd

atlas = [
    ['Франция', 'Париж'],
    ['Россия', 'Москва']
]

geography = ['country', 'capital']

frame = pd.DataFrame(data=atlas, columns=geography)

frame['Some'] = (True, False)

print(frame)
