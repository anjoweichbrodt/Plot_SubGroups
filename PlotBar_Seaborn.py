import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

np.random.seed(1983)
num = 21
y = np.random.random((num))
cat1 = np.random.choice(['a', 'b', 'c'], num)
cat2 = np.random.choice(['I', 'II', 'III'], num)
df = pd.DataFrame(dict(y=y, cat1=cat1, cat2=cat2))

print(df)

sns.barplot(x="cat1", y="y", hue="cat2", data=df)

sns.plt.show()

# http://seaborn.pydata.org/tutorial/categorical.html
