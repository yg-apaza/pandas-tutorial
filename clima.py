import pandas as pd
import re
from datetime import datetime

import matplotlib
import pylab

def string_to_date(date_string):
    return datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")

df = pd.read_csv('arequipa.csv',skiprows=1)

print(df.shape)
print(df.columns)
print(df.mean())
print(df['Precipitation'].describe())

print(df['Temperature'].head(10))
print(df.Temperature.head(10))
print(df['Cloud Cover'].head(10))
#print(df.Cloud Cover.head(10))

dcol = [ re.sub(r'\(.*?\)', '', col).strip(' ').replace(' ', '_') for col in df.columns ]
#dcol = ['Time', 'Temperature', 'Precipitation', 'Cloud_Cover', 'Shortwave_Radiation', 'Wind_Speed']
df.columns = dcol
print(df.columns)

print(df.index)
df.date = df['Time'].apply(string_to_date)
print(df.date.head())
df.index = df.date
print(df.index)

df.today = df[ ( df.index.month == 2 ) & ( df.index.day == 1 )]
print(df.today)
print(df.today.Temperature.max())
print(df.ix[datetime(2019, 1, 27, 17, 0, 0)])


df.Temperature.plot(title='Temperature')
pylab.show()

df.Precipitation.plot(title='Precipitation')
pylab.show()

df.today.Cloud_Cover.plot(title='Today Cloud Cover')
pylab.show()

df.today.Shortwave_Radiation.plot(title='Today Radiation')
pylab.show()

df.today.Wind_Speed.plot(title='Today Wind Speed')
pylab.show()
