import pandas as pd

atlas = [
    ['Франция','Париж'],
    ['Россия','Москва'],
    ['Китай','Пекин'],
    ['Мексика','Мехико'],
    ['Египет','Каир'],
]

geography = ['country', 'capital']

world_map = pd.DataFrame(data = atlas, columns = geography)

print(world_map)

