import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (8.0, 6.0)

df = pd.read_csv('uber-raw-data-janjune-15.csv')
print(len(df))
print(df.columns.values)

df['Pickup_date'] = pd.to_datetime(df['Pickup_date'], format='%Y-%m-%d %H:%M:%S')
df['Month'] = df['Pickup_date'].apply(lambda x: x.month)
df['Day'] = df['Pickup_date'].apply(lambda x: x.day)
df['Hour'] = df['Pickup_date'].apply(lambda x: x.hour)
df['Weekday'] = df['Pickup_date'].apply(lambda x: x.strftime('%A'))
#print(df.head())

sns.set_style('darkgrid')
ax = sns.countplot(x="Month", data=df, color="lightsteelblue")
plt.show()

sns.set_style('darkgrid')
ax = sns.countplot(x="Hour", data=df, color="lightsteelblue")
plt.show()

sns.set_style('darkgrid')
ax = sns.countplot(x="Weekday", data=df, color="lightsteelblue")
plt.show()
