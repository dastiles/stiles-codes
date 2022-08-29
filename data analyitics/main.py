import numpy as np
import matplotlib.pyplot as plt

# %matplotlib inline
plt.style.use('seaborn-whitegrid')
x = [590, 540, 740, 130, 810, 300, 320, 230, 470, 620, 770, 250]
y = [32, 36, 39, 52, 61, 72, 77, 75, 68, 57, 48, 48]

plt.scatter(x, y)
plt.xlim(0, 1000)
plt.ylim(0, 100)

# scatter the plot color
plt.scatter(x, y, s=60, c='red', marker='^')

# change axes ranges
plt.xlim(0, 1000)
plt.ylim(0, 100)

# add title
plt.title('Relationship between Temperature and iced coffe sales')

# add x and y labels
plt.xlabel('sold coffe')
plt.ylabel('Temperature in Fahrenhet')

# show plot
plt.show()
