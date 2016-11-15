import pandas as pd

df = pd.read_csv('shot_logs.csv')

dfmd = df[df['SHOT_RESULT'] == 'made']
print(dfmd.groupby(['CLOSEST_DEFENDER']).agg({'GAME_ID': lambda x: x.count()/x.nunique()}).sort_values(['GAME_ID'], ascending=False).head())

dfms = df[df['SHOT_RESULT'] == 'missed']
print(dfms.groupby(['CLOSEST_DEFENDER']).agg({'GAME_ID': lambda x: x.count()/x.nunique()}).sort_values(['GAME_ID'], ascending=False).head(n = 10))

#'Kyrie Irving', 'Lebron James', 'Kevin Love', 'Tristan Thompson'
print('Player /', 'defence failed /', 'defence successful')
print('Kyrie Irving', dfmd[dfmd['CLOSEST_DEFENDER'] == 'Irving, Kyrie']['GAME_CLOCK'].count(), dfms[dfms['CLOSEST_DEFENDER'] == 'Irving, Kyrie']['GAME_CLOCK'].count())
print('Lebron James', dfmd[dfmd['CLOSEST_DEFENDER'] == 'James, LeBron']['GAME_CLOCK'].count(), dfms[dfms['CLOSEST_DEFENDER'] == 'James, LeBron']['GAME_CLOCK'].count())
print('Kevin Love', dfmd[dfmd['CLOSEST_DEFENDER'] == 'Love, Kevin']['GAME_CLOCK'].count(), dfms[dfms['CLOSEST_DEFENDER'] == 'Love, Kevin']['GAME_CLOCK'].count())
print('Tristan Thompson', dfmd[dfmd['CLOSEST_DEFENDER'] == 'Thompson, Tristan']['GAME_CLOCK'].count(), dfms[dfms['CLOSEST_DEFENDER'] == 'Thompson, Tristan']['GAME_CLOCK'].count())
