import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import time

# Reading the file as a dataset
df = pd.read_csv('activity.csv')

# What is the average daily activity pattern?

# Making the total number of steps every 5-minute interval as two lists (Ignoring the NA)
interval = []
steps = []
for i in df['interval'].unique():
    interval.append(i)
    steps.append(df.loc[df['interval']==i, 'steps'].dropna().mean())

dfB = pd.DataFrame({'Interval':interval, 'Steps':steps})
dfB.plot(x ='Interval', y='Steps', kind = 'line')
plt.title('Average number of steps taken in 5-minute intervals')
plt.xticks(np.linspace(0,2355,15))
plt.show()

# Checking which interval has the max average
print(f"Interval with max number of average steps is {dfB.loc[dfB['Steps']==dfB['Steps'].max(), 'Interval'].item()}.")