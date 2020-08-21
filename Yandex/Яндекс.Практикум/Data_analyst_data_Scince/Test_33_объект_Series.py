import pandas as pd
df = pd.read_csv('music_log.csv')

rock = df.loc[df['genre'] == 'rock']
rock_time = rock['total play']
rock_haters = rock_time.loc[rock_time <= 5].count()

print('Количество пропущенных треков жанра рок равно', rock_haters)

pop = df.loc[df['genre'] == 'pop']
pop_time = pop['total play']
pop_haters = pop_time.loc[pop_time <= 5].count()

print('Количество пропущенных треков жанра поп равно', pop_haters)
#
# rock_skip = rock_haters /
# pop_skip = pop_haters /
#
# print('Доля пропущенных композиций жанра рок равна:', rock_skip)
# print('Доля пропущенных композиций жанра поп равна:', pop_skip)