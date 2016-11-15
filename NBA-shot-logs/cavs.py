import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from pylab import xticks
import numpy as np

matplotlib.style.use('fivethirtyeight')

df = pd.read_csv('shot_logs.csv')

kyrie = df[df['player_name'] == 'kyrie irving']
love = df[df['player_name'] == 'kevin love']
lebron = df[df['player_name'] == 'lebron james']
tt = df[df['player_name'] == 'tristan thompson']

plt.hist([kyrie['PERIOD'], lebron['PERIOD'], love['PERIOD'], tt['PERIOD']])
plt.legend(['Kyrie Irving', 'Lebron James', 'Kevin Love', 'Tristan Thompson'])
plt.xlabel("Period")
plt.ylabel("Shot Counts")
xticks(range(1, 5))
plt.show()

def shotpct(df, feature='SHOT_RESULT', result='made'):
    return len(df[df[feature] == result])/len(df)

cavs = [kyrie, love, lebron, tt]
names = ['Kyrie','Love','Lebron','Thompson']
pct = []
for i in cavs:
    pct.append(shotpct(i))
df2 = pd.DataFrame()
df2['names'] = names
df2['p'] = pct

fig, ax = plt.subplots()
ax.bar(df2.index, df2['p'], align='center', alpha=0.65, color='red')
xticks(np.arange(len(names)), df2['names'])
plt.show()

plt.hist([kyrie['SHOT_DIST'], lebron['SHOT_DIST'], love['SHOT_DIST'], tt['SHOT_DIST']])
plt.legend(['Kyrie Irving', 'Lebron James', 'Kevin Love', 'Tristan Thompson'])
plt.show()

