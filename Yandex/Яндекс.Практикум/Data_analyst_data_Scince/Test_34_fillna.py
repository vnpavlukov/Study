import pandas as pd
df = pd.read_csv('music_log_upd_col.csv')

df['track_name'] = df['track_name'].fillna('unknown')

