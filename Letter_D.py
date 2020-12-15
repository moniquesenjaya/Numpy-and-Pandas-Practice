import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import datetime 
import calendar 

# Reading the file as a dataset
df = pd.read_csv('activity.csv')


# Are there differences in activity patterns between weekdays and weekends?

# Function to check the date using datetime and calendar module
def findDay(date): 
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    the_date = datetime.datetime.strptime(date, '%Y-%m-%d').weekday() 
    if calendar.day_name[the_date] in weekdays:
        return 'weekday'
    else:
        return 'weekend'

# Making a new factor variable by applying the findDay function  
df['day'] = df['date'].apply(findDay)


# Making the total number of steps every 5-minute interval as two lists (Ignoring the NA)
interval = []
steps_weekday = []
steps_weekend = []
for i in df['interval'].unique():
    interval.append(i)
    steps_weekday.append(df.loc[(df['interval']==i) & (df['day']=='weekday'), 'steps'].dropna().mean())
    steps_weekend.append(df.loc[(df['interval']==i) & (df['day']=='weekend'), 'steps'].dropna().mean())

dfB = pd.DataFrame({'Interval':interval, 'Weekday': steps_weekday,'Weekend':steps_weekend})

dfB.plot(x ='Interval', kind = 'line')
plt.title('Average number of steps taken in 5-minute intervals')
plt.xticks(np.linspace(0,2355,15))
plt.ylabel('Steps')
plt.show()
