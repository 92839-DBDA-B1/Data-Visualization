import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def function():
    df=pd.read_csv("mtcars.csv")
    print(df)
    print(df.corr())
    fig, axes=plt.subplots(2,2)

    axes[0,0].scatter(df['mpg'],df['hp'],label="Plot1",color="#a4e29e")
    axes[0,0].set_xlabel("mpg")
    axes[0,0].set_ylabel("hp")
    axes[0,0].set_title("mpg vs hp")
    axes[0,0].legend(loc="upper right")
    axes[0,0].grid(visible=True)

    axes[0,1].scatter(df['disp'],df['drat'],label="Plot2",color="#e29ec0",marker="*")
    axes[0,1].set_xlabel('disp')
    axes[0,1].set_ylabel('drat')
    axes[0,1].set_title("disp vs drat")
    axes[0,1].legend(loc="upper right")
    axes[0,1].grid(visible=True)


    axes[1,0].scatter(df['qsec'],df['wt'],label="Plot3",marker="o",color="red",cmap='viridis')
    axes[1,0].set_xlabel('qsec')
    axes[1,0].set_ylabel('wt')
    axes[1,0].set_title("qsec vs wt")
    axes[1,0].legend(loc="upper right")
    axes[1,0].grid(visible=True)

    axes[1,1].scatter(df['cyl'],df['qsec'],c=df['am'],label="Plot4")
    axes[1,1].set_xlabel('cyl')
    axes[1,1].set_ylabel('qsec')
    axes[1,1].set_title("cyl vs qsec")
    axes[1,1].legend(loc="upper right")
    axes[1,1].grid(visible=True)

    fig.set_facecolor("#a7fdfd")
    fig.suptitle('Car Performance Analysis',fontsize=20)
    fig.tight_layout()
    plt.tight_layout()
    plt.show()



function()