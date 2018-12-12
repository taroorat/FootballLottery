
import pandas as pd
df = pd.read_csv("data/score-data.csv", usecols=['Date', 'HomeTeam', 'AwayTeam','FTHG','FTAG','B365H','B365D','B365A'
      ,'BWH','BWD','BWA','IWH','IWD','IWA','LBH','LBD','LBA','WHH','WHD','WHA','VCH','VCD','VCA'])

df["AGVH"]=(df['B365H']+ df['BWH']+df['IWH']+df['LBH']+df['WHH']+df['VCH'])/6
df["AGVD"]=(df['B365D']+ df['BWD']+df['IWD']+df['LBD']+df['WHD']+df['VCD'])/6
df["AGVA"]=(df['B365A']+ df['BWA']+df['IWA']+df['LBA']+df['WHA']+df['VCA'])/6
df=df.round(2)
df["SCORE"] = df["FTHG"]-df["FTAG"]

df["SCORE"]=df["SCORE"].astype('float')
# df["SCORE"]=df["SCORE"].astype('int32')

for indexs in df.index:
    # print(df.loc[indexs].values[0:5],df.loc[indexs].values[-4:])
    print(df.loc[indexs].values[-4:])

df.to_csv('data/answer-data.csv')



