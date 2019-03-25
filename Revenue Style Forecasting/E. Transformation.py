#### 0.- PRELIMINARIES
import pandas as pd
import numpy as np
import datetime
from datetime import timedelta as td

pd.set_option('display.max_columns',500)

#### I.- EXTRACTING, CREATING DATA FORMATS AND CREATING DATE MERGING VARIABLES
df = pd.read_csv('C:/Users/alexisalvarez/OneDrive - Grupo Vidanta/UPDATE/Work/19 25Mar19 - Arrivals-Occupancy Forecasting/ArrivalAndOccupancyForecasting/Revenue Style Forecasting/E. TEAMS__Base_Trabajo.csv')
df['FirstNight'] = [datetime.datetime(int(d[-4:]),
                                      int(d[3:5]),
                                      int(d[:2])) \
                    for d in df['FirstNight']]
df['toMerge'] = [d + td(days=-1) for d in df['FirstNight']]
df['toMerge'] = [datetime.datetime(d.year+1,d.month,d.day) for d in df['toMerge']]


df = df.sort_values(by = 'FirstNight')
print(df.shape)
print(df.head())