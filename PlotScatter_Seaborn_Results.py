import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import xlwings as xw

sns.set_style("whitegrid")

df = xw.Range('B1:E31').options(pd.DataFrame, index=False).value
df = df.sort(columns=df.columns.values[1])

ax = sns.swarmplot(x=df[df.columns[1]], y=df[df.columns[2]], hue=df[df.columns[0]], data=df)
ax.set(ylabel=df.columns.values[2])
ax.set_title(df.columns.values[3])
ax.legend(loc='upper right')

sns.plt.show()


# http://seaborn.pydata.org/tutorial/categorical.html
