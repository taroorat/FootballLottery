import pandas as pd
df = pd.read_csv("data/score-data.csv", usecols=['Date', 'HomeTeam', 'AwayTeam','FTHG','FTAG'])

HomeTeam=df['HomeTeam'].str.contains('Man United')
for indexs in df.index:
    # print(bool[indexs])
    if HomeTeam[indexs] == True:
        AwayTeam = df['AwayTeam'].str.contains('Liverpool')
        if AwayTeam[indexs] == True:
            print(df.loc[indexs].values)
            if df['FTHG'][indexs] > df['FTAG'][indexs]:
                print(3)
            elif df['FTHG'][indexs] == df['FTAG'][indexs]:
                print(1)
            else:
                print(0)

