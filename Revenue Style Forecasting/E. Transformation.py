#### 0.- PRELIMINARIES
import pandas as pd
import numpy as np
import datetime
from datetime import timedelta as td
import matplotlib.pyplot as plt

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

#### II.- MERGING FINAL DB
ls_columns = ['FirstNight','Reservaciones_Libros_2019']
frame = df[pd.isnull(df[df.columns[1]])][ls_columns]
frame.rename(columns = {ls_columns[0]:'toMerge',
                        ls_columns[len(ls_columns)-1]:'Libros'}, 
                            inplace = True)

df = df[[c for c in df if c in ['toMerge'] or c.startswith('Tasa')\
         or c.startswith('Estancia')]]
frame = frame.merge(df, how = 'left', on = ['toMerge'])
frame.rename(columns = {'toMerge':'FirstNight'}, inplace = True)
frame['ResvGorro'] = frame['Libros']*(1+frame['Tasa_PickUP'])*\
                                     (1-frame['TasaNoShow'])*\
                                     (1-frame['TasaCancelación'])
                                     
frame.to_csv('tacitas.csv')
print(frame.shape)
print(frame.head())

