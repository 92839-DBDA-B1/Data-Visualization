# 8. Write a Pandas program to convert a NumPy array to a Pandas series.
import numpy as np
import pandas as pd

def function():
    n1=np.array([1,2,3,4,5,6])
    print(f"n1 type={type(n1)}")
    p1=pd.Series(n1)
    print(f"p1 type={type(p1)}")

function()