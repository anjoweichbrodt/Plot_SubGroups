import xlwings as xw
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
#%matplotlib inline

# Generate the data
df = xw.Range('B1:E11').options(pd.DataFrame, index=False).value

# Plot
mean = df.groupby(['Nom'])['Force Rupture (N)'].mean()
#plt(x=DfGrouped_mean('Nom'), y=DfGrouped_mean('Force Rupture (N)'), yerr=DfGrouped_std('Force Rupture (N)'), color='k', grid=False, marker='o', ls='')
mean.plot(style=['o','rx'])
plt.show()

#appearance
sns.set_style('white')
sns.set_style('ticks')

plt.xlim([34.5, 44.5])
plt.ylim([72, 128])

#Resource
#sns.despine()
#http://anki.xyz/publication-grade-plot-using-python/
