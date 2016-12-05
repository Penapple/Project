from sqlalchemy import create_engine
import pandas as pd
engine = create_engine('sqlite:///database.sqlite')

table_names = engine.table_names()
print(table_names)

with engine.connect() as con:
    rs = con.execute('SELECT * FROM Player_Attributes')
    df = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys()

#print(df.columns.values)
#print(df.head())


