# 1. Write a NumPy program to create an array with the values 1, 7, 13, 105 and determine the size of the memory occupied by the array.
import numpy as np

def function():
    array=np.array([1,7,13,105])
    print(array)

    print(f"array size=",{array.size})
    print(f"array itemsize",{array.itemsize})
    print(f"the size of the memory occupied by the array=",{array.size*array.itemsize})

function()