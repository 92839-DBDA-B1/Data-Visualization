import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def function1():
    df=pd.read_csv("tips.csv")
    colors=['#ff9999', '#66b3ff', "#99ffa7", '#ffcc99']
    print(df)

    colmun_modified=['sex','smoker','day','time']
    df_mod=df.drop(columns=colmun_modified,axis=1)
    
    explodes = [0, 0.1, 0, 0]
    data=df['day'].value_counts().values
    data1=df['day'].value_counts().index
    #print(df_mod)

    plt.pie(data,
            labels=data1,
            colors=colors,
            autopct='%1.2f%%',
            explode=explodes,
            shadow=True)
    
    plt.title("pie chart")
    plt.tight_layout()
    plt.show()

function1()