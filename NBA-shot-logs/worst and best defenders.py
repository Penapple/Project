import pandas as pd

df = pd.read_csv('shot_logs.csv')

dfmd = df[df['SHOT_RESULT'] == 'made']
print(dfmd.groupby(['CLOSEST_DEFENDER']).agg({'GAME_ID': lambda x: x.count()/x.nunique()}).sort_values(['GAME_ID'], ascending=False).head())

dfms = df[df['SHOT_RESULT'] == 'missed']
print(dfms.groupby(['CLOSEST_DEFENDER']).agg({'GAME_ID': lambda x: x.count()/x.nunique()}).sort_values(['GAME_ID'], ascending=False).head(n = 10))
