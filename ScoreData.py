import csv
import glob
import os
import pandas as pd
# with open('data/E0.csv', 'r') as f:
#     for i in range(1):
#         print(f.readline().strip())


path=r'data'
file=glob.glob(os.path.join(path, "E0*.csv"))
print(file)
dl= []
for f in file:
   dl.append(pd.read_csv(f, usecols=['Date', 'HomeTeam', 'AwayTeam','FTHG','FTAG']))

df=pd.concat(dl)
print(df)

df.to_csv('data/score-data.csv')
print(type(df))