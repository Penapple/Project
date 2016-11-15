import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('shot_logs.csv')
#cavs = df[df['MATCHUP'].str.contains("CLE @" or "vs. CLE") == True]  not work well
love = df[df['player_name'] == 'kevin love']
kyrie = df[df['player_name'] == 'kyrie irving']
print(love['SHOT_DIST'].count())
print(kyrie['SHOT_DIST'].count())

sns.violinplot(love['SHOT_DIST'])
plt.title('love')
plt.show()
sns.violinplot(kyrie['SHOT_DIST'])
plt.title('kyrie')
plt.show()





