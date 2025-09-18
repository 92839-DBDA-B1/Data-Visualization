import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("tips.csv",index_col=0)
plt.style.use('ggplot')
#print(df)
plt.grid(visible=True)

columnes_to_drom=['sex','smoker','day','time']
df_mod=df.drop(columns=columnes_to_drom,axis=1)
#print(df_mod)


def function1():
    

    plt.boxplot(df_mod,
                tick_labels=df_mod.columns,
                patch_artist=True,
                boxprops={"facecolor":'lightblue',"alpha":0.7},
                medianprops={"color":'red',"linewidth":2})
    plt.title("Box plot of tips data",fontsize=14,fontweight='bold')
    plt.tight_layout()
    plt.show()           

function1()