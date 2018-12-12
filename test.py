import pandas as pd
import matplotlib.pyplot as plt

def WinLevelLose(bunko):
    df = pd.read_csv("data/home-%s.csv"%bunko,sep=' ')

    df.columns=["AGVH","AGVD","AGVA","LEVEL"]
    df["SUM"]=df["AGVH"]+df["AGVD"]+df["AGVA"]
    df["AGVH"]=(df["AGVH"]/df["SUM"])
    df["AGVD"]=(df["AGVD"]/df["SUM"])
    df["AGVA"]=(df["AGVA"]/df["SUM"])
    df=df.round(2)
    print(df)
    df.to_csv('data/home-%s-answer.csv'%bunko)
    df = pd.read_csv("data/home-%s-answer.csv" % bunko,usecols=["AGVH","AGVD","AGVA"])

    df.plot(figsize=(15, 5),grid=True)
    plt.show()

WinLevelLose("lose")