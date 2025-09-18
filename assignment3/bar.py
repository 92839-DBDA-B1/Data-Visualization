import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def function1():

    df=pd.read_csv("tips.csv",index_col=0)
    print(df)
    x=df['day'].value_counts().values
    y=df['day'].value_counts().index

    plt.bar(y,x,label="Days",color="skyblue",alpha=0.7,edgecolor='black')
    plt.title("Days Count")
    plt.xlabel("count")
    plt.ylabel("Day")

    plt.legend()

    plt.tight_layout()
    plt.show()

    #print(df)
function1()

