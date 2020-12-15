import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import time

# Reading the file as a dataset
df = pd.read_csv('activity.csv')

#What is mean total number of steps taken per day?

# Making the total number of steps per day as two lists (Ignoring the NA)
days = []
steps = []
for i in df['date'].unique():
    days.append(i)
    steps.append(df.loc[df['date']==i, 'steps'].dropna().sum())

# Made the two list into a dataframe
dfA = pd.DataFrame({'Days':days, 'Steps':steps})

# Plotting Bar Graph
ax = dfA.plot.bar(x='Days', y='Steps', width=0.5 , color='g')
plt.title('Total Number of Steps Per Day')
plt.xlabel('Days')
plt.ylabel('Steps')
plt.xticks(rotation = 45, size=7)
plt.show()

# Printing the report of mean and median
print("Report:")
print(f"Mean: {dfA.mean().item()}")
print(f"Median: {dfA.median().item()}")


