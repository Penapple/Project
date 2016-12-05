from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('sqlite:///database.sqlite')

df = pd.read_sql_query("SELECT * FROM Player_Attributes as a \
INNER JOIN (SELECT player_name, player_api_id FROM Player) \
as b ON a.player_api_id = b.player_api_id", engine)

df1 = df[['player_name', 'overall_rating']]
list_name, list_rating = df1.values.transpose()
#print(list_rating)

d = {}
d_rating = {}
for name, rating in zip(list_name, list_rating):
    d.setdefault(name, []).append(rating)

for key in d:
    #print (key, sum(d[key])/len(d[key]))
    d_rating[key] = sum(d[key])/len(d[key])


s = pd.Series(d_rating, name = 'overall_rating')
s.index.name = 'Name'
s.reset_index()
s = s.sort_values(ascending=False)
print(s.head(n=5))
