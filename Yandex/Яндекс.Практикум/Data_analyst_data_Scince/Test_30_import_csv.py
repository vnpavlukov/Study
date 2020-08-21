import pandas as pd

df = pd.read_csv('music_log.csv')
music_head = df.head()
music_tail = df.tail(10)
print(music_head)