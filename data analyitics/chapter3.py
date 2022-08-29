import numpy as np
import pandas as pd

Series1 = pd.Series(np.random.randn(4), index=['a', 'b', 'c', 'd'])

print(Series1)
print(Series1.index)


Series2 = pd.Series(np.random.randn(4))

print(Series2)
print(Series2.index)
