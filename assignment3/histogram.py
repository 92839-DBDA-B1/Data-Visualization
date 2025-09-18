import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def function():
    df=pd.read_csv("tips.csv")
    #print(df)
    plt.hist(df['total_bill'],
             bins=20,
             color='skyblue',
             alpha=0.7,
             edgecolor='black',
             density=True)
    
    mu,sigma=np.mean(df['total_bill']),np.std(df['total_bill'])
    x = np.linspace(df['total_bill'].min(), df['total_bill'].max(), 100)
    y = ((1/(sigma * np.sqrt(2 * np.pi))) *
        np.exp(-0.5 * ((x - mu) / sigma) ** 2))
    plt.plot(x, y, 'r-', linewidth=2, label=f'Normal Distribution\n(μ={mu:.1f}, σ={sigma:.1f})')


    plt.tight_layout()
    plt.show()

function()