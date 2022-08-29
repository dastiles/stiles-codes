import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

plt.style.use('classic')
plt.style.use('seaborn-whitegrid')

# create some data
data = np.random.multivariate_normal([0, 0], [[5, 2], [2, 2]], size=2000)
data = pd.DataFrame(data, columns=['x', 'y'])

# plot the data with seaborn
sns.displot(data['x'])
sns.displot(data['y'])

plt.show()
