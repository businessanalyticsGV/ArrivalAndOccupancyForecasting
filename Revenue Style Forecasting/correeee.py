import pandas as pd
import numpy as np
import datetime
pd.set_option('display.max_columns',500)

df = pd.read_excel('paranomoverle.xlsx')

frame = pd.DataFrame()

for date in df['FirstNight']:
    fr = df[df['FirstNight'] == date]
    n = list(fr['Estancia'])[0]
    concat = pd.DataFrame()
    for i in range(n):
        concat = pd.concat([concat,fr])
    frame = pd.concat([frame,concat])

frame.to_excel('repetidas.xlsx', index = False)