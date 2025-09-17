# 10. Refer the dataset "Advertising.csv" and perform following tasks.
# i) Read the dataset "Advertising.csv" in data frame.
# ii) Print first five records of dataset.
# iii) print last five records from dataset.
# iv) display the column names of the dataset.
# v) display last three records from dataset.
# vi) display the information about the dataset.
# vii) display data types of each columns.
# viii) check for null values in the dataset and display the sum of null values inside the column.
# ix) drop all null values.
# x) drop a column 'radio' from a dataset and display first ten records.
# xi) increase the sales by 10% and add a new column "updated_sales" in dataframe.
# xii) display shape of data.

import pandas as pd

def function():
    df=pd.read_csv("Advertising.csv")
    print(df.head(5))
    print(df.tail(5))
    print(df.columns)
    print(df.tail(3))
    print(df.info())
    print("-"*60)
    print(df.dtypes)
    print("-"*60)
    print(df.isna().sum())
    no_null=df.dropna()
    print(no_null.head())
    # x) drop a column 'radio' from a dataset and display first ten records.
    df.drop(["radio"],axis=1,inplace=True)
    print(df.head(10))
    # xi) increase the sales by 10% and add a new column "updated_sales" in dataframe.
    print("increase the sales by 10%")
    df['Updated_sale']=df['sales']*1.10
    print(df.head())
    # xii) display shape of data.
    print("shape of df:")
    rows,columns=df.shape
    print(f"rows={rows},columns={columns}")


function()