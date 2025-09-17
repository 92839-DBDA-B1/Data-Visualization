# 7. Write a Pandas program to add, subtract, multiple and divide two Pandas Series.
#    Sample Series: [2, 4, 6, 8, 10], [1, 3, 5, 7, 9]

import pandas as pd

def function():
    n1=pd.array([2, 4, 6, 8, 10])
    n2=pd.array([1, 3, 5, 7, 9])

    print(f"n1+n2={n1+n2}")
    print(f"n1-n2={n1-n2}")
    print(f"n1*n2={n1*n2}")
    print(f"n1/n2={n1/n2}")

function()
