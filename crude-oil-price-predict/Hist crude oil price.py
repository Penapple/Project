import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
excel = pd.ExcelFile('PET_PRI_SPT_S1_W.xls')
df = excel.parse(excel.sheet_names[1])
df = df.rename(columns=dict(zip(df.columns, ['Date','WTI','Brent'])))
df = df[18:]

df.index = df['Date']
df = df[['WTI','Brent']]

sns.set_style("darkgrid")
plt.plot(df[['WTI','Brent']][::4])
plt.title('Crude Oil Prices')
plt.xlabel('Year')
plt.ylabel('Price [USD]')
plt.legend(df)
plt.show()

plt.plot(df[-36*4:])
plt.title('Crude Oil Prices')
plt.xlabel('Year')
plt.ylabel('Price [USD]')
plt.legend(df)
plt.show()

df[-36*4:].to_csv('prices_last_three_years.csv')

