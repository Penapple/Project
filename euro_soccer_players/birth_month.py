from sqlalchemy import create_engine, select, Table, MetaData
import pandas as pd
import matplotlib.pyplot as plt

engine = create_engine('sqlite:///database.sqlite')

df = pd.read_sql_query("SELECT birthday FROM Player", engine)

df['month'] = df.birthday.str[5:7].apply(int)
print(df.head())


his = plt.hist(df['month'], bins=12)
fig, ax = plt.subplots()
offset = .5
plt.bar(his[1][1:], his[0])
ax.set_xticks(his[1][1:] + offset)
ax.set_xticklabels(('1', '2', '3', '4','5','6','7','8','9','10','11','12'))
plt.xlim([2,13])
plt.xlabel('birth month')
plt.ylabel('counts')
plt.show()
