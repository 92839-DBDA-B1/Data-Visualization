import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns

def function1():
    df=pd.read_csv("tips.csv",index_col=0)
    #print(df)

    colums_to_del=['day','time','sex','smoker']
    df_mod=df.drop(columns=colums_to_del,axis=1)
    #print(df_mod)
    correlation_matrix=df_mod.corr()
    print(correlation_matrix)

    sns.heatmap(correlation_matrix,annot=True)
    plt.show()




function1()