import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from matplotlib import cm

df = pd.read_csv('uber-raw-data-may14.csv')

N = 405146
west, south, east, north = -74.26, 40.50, -73.70, 40.92

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111)
m = Basemap(projection='merc', llcrnrlat=south, urcrnrlat=north,
            llcrnrlon=west, urcrnrlon=east, lat_ts=south, resolution='i')
x, y = m(df['Lon'].values, df['Lat'].values)
m.hexbin(x, y, gridsize=1000, bins='log')
m.drawcoastlines()
m.fillcontinents(color='coral',lake_color='aqua')
plt.show()
