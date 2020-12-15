import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import time

# Reading the file as a dataset
df = pd.read_csv('activity.csv')

# Inputting missing values

# Calculate and report the total number of missing values in the dataset (i.e. the total number of rows with NAs)
print(pd.isnull(df).sum())

# Create a new dataset that is equal to the original dataset but with the missing data filled in.
# The strategy I am using is by filling all the NAs with the value 0
new_df = df.fillna(0)
# Showing that there is no null values in the new dataframe
print(pd.isnull(new_df).sum())

# Making the total number of steps per day as two lists (Ignoring the NA)
days = []
steps = []
for i in new_df['date'].unique():
    days.append(i)
    steps.append(new_df.loc[df['date']==i, 'steps'].sum())

# Made the two list into a dataframe
df_plot = pd.DataFrame({'Days':days, 'Steps':steps})

# Plotting Bar Graph
ax = df_plot.plot.bar(x='Days', y='Steps', width=0.5 , color='g')
plt.title('Total Number of Steps Per Day')
plt.xlabel('Days')
plt.ylabel('Steps')
plt.xticks(rotation = 45, size=7)
plt.show()

# Printing the report of mean and median
print("Report:")
print(f"Mean: {df_plot.mean().item()}")
print(f"Median: {df_plot.median().item()}")
