from sqlalchemy import create_engine, select, Table, MetaData
import pandas as pd
import matplotlib.pyplot as plt

engine = create_engine('sqlite:///database.sqlite')
connection = engine.connect()
df = pd.read_sql_query("SELECT * FROM Player_Attributes as a \
INNER JOIN (SELECT birthday, player_api_id FROM Player) \
as b ON a.player_api_id = b.player_api_id", engine)

df1 = df[['player_fifa_api_id','birthday', 'overall_rating']]
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
top = s.head(100)
top_str = map(str, top.index)

metadata = MetaData()
Player_Attributes = Table('Player_Attributes', metadata, autoload=True,
autoload_with=engine)

stmt = select([Player_Attributes.columns.overall_rating, Player_Attributes.columns.player_fifa_api_id])
stmt = stmt.where(Player_Attributes.columns.player_fifa_api_id.in_(top_str))
res = connection.execute(stmt).fetchall()
top100 = pd.DataFrame(res)
top100.columns = connection.execute(stmt).keys()

top100 = pd.merge(top100, df[['player_fifa_api_id','birthday']])
top100 = top100.drop_duplicates(subset='player_fifa_api_id', keep='first')
top100['month'] = top100.birthday.str[5:7].apply(int)

his = plt.hist(top100['month'], bins=12)
fig, ax = plt.subplots()
offset = .5
plt.bar(his[1][1:], his[0])
ax.set_xticks(his[1][1:] + offset)
ax.set_xticklabels(('1', '2', '3', '4','5','6','7','8','9','10','11','12'))
plt.xlim([2,13])
plt.xlabel('birth month')
plt.ylabel('counts')
plt.show()
