
import pandas as pd
df = pd.read_csv("data/home-level.csv",sep=' ')

df.columns=["AGVH","AGVD","AGVA","LEVEL"]
df["SUM"]=df["AGVH"]+df["AGVD"]+df["AGVA"]
df["AGVH"]=(df["AGVH"]/df["SUM"])
df["AGVD"]=(df["AGVD"]/df["SUM"])
df["AGVA"]=(df["AGVA"]/df["SUM"])
df=df.round(2)
print(df)
df.to_csv('data/home-level-answer.csv')