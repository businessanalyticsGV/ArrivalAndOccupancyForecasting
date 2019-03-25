#### 0.- PRELIMINARIES
import pandas as pd
import numpy as np
import datetime
pd.set_option('display.max_columns',500)

#### I.- EXTRACTING AND CREATING DATA FORMATS
df = pd.read_csv('C:/Users/alexisalvarez/OneDrive - Grupo Vidanta/UPDATE/Work/19 25Mar19 - Arrivals-Occupancy Forecasting/ArrivalAndOccupancyForecasting/Revenue Style Forecasting/E. TEAMS__Base_Trabajo.csv')
df['FirstNight'] = [datetime.datetime(int(d[-4:]),
                                      int(d[3:5]),
                                      int(d[:2])) \
                    for d in df['FirstNight']]
df = df.sort_values(by = 'FirstNight')
print(df.shape)
print(df.head())