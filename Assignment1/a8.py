# 9.  i) Create a list of empids and names (10 employees).
#    ii) Convert list into Series.
#    iii) Convert Series into DataFrame.
#    iv) a) Display all records.
#       b) Display first five records.
#       c) Display last five records.
#    v) Save the record in csv file (MyRecord.csv)


import numpy as np
import pandas as pd

def function():
    emp_id=[1,2,3,4,5,6,7,8,9,10]
    emp_name=["Neha","Krishna","Vaibhav","Pranju","Shantanu","Niraj","Ashvini","Sakshi","Viashnavi","Durgesh"]
    ser_id=pd.Series(emp_id,name="EmpId")
    ser_name=pd.Series(emp_name,name="emp_name")

    df=pd.DataFrame({"EmpId":ser_id,"Name":ser_name})
    print("All record:")
    print(df)
    print("first Five record")
    print(df.head(5))
    print("last five records")
    print(df.tail(5))
    df.to_csv("mycsv.csv",index=False)
function()