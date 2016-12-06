from sqlalchemy import create_engine, select, Table, MetaData
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

engine = create_engine('sqlite:///database.sqlite')
connection = engine.connect()
df = pd.read_sql_query("SELECT * FROM Player_Attributes as a \
INNER JOIN (SELECT player_name, player_api_id FROM Player) \
as b ON a.player_api_id = b.player_api_id", engine)

df1 = df[['player_fifa_api_id','player_name', 'overall_rating']]
list_id, list_name, list_rating = df1.values.transpose()

d = {}
d_rating = {}
for id, rating in zip(list_id, list_rating):
    d.setdefault(id, []).append(rating)

for key in d:
    #print (key, sum(d[key])/len(d[key]))
    d_rating[key] = sum(d[key])/len(d[key])


s = pd.Series(d_rating, name = 'overall_rating')
s.index.name = 'id'
s.reset_index()
s = s.sort_values(ascending=False)
top10 = s.head(10)
print(top10)
top10_int = list(top10.index)
top10_str = map(str, top10.index)

metadata = MetaData()
Player_Attributes = Table('Player_Attributes', metadata, autoload=True,
autoload_with=engine)

stmt = select([Player_Attributes.columns.date, Player_Attributes.columns.overall_rating, Player_Attributes.columns.player_fifa_api_id])
stmt = stmt.where(Player_Attributes.columns.player_fifa_api_id.in_(top10_str))
res = connection.execute(stmt).fetchall()
growth = pd.DataFrame(res)
growth.columns = connection.execute(stmt).keys()

growth = pd.merge(growth, df[['player_fifa_api_id','player_name']])
growth['year'] = growth.date.str[:4].apply(int)
growth['player_fifa_api_id'] = growth.player_fifa_api_id.apply(int)
growth = growth.groupby(['year','player_name','player_fifa_api_id']).overall_rating.mean()
growth = growth.reset_index()
print(growth.head())
print(type(growth))

growth1 = growth[growth.player_fifa_api_id.isin(top10_int[:5])]
growth2 = growth[growth.player_fifa_api_id.isin(top10_int[5:10])]

sns.factorplot(x='year', y='overall_rating', hue='player_name',
               data=growth1,  size=6, aspect=2, legend=False)
plt.legend(loc=0)
plt.show()

sns.factorplot(x='year', y='overall_rating', hue='player_name',
               data=growth2,  size=6, aspect=2, legend=False)
plt.legend(loc=0)
plt.show()
