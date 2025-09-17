# 11. Refer the dataset "Salaries.csv" and perform following tasks.
# i) Read the dataset in dataframe.
# ii) display first five records.
# iii) display first ten records.
# iv) display last five records.
# v) display last ten records.
# vi) display the columns inside the dataset.
# vii) display shape of data.
# viii) describe the dataset.
# ix) display the information about the dataset.
# x) display types of each columns.
# xi) Find out maximum,minimum,mean,median,standard deviation value of each column.
# xii) check for null values in the dataset and display the sum of null values inside the column.
# xiii) Replace all null values by mean or mode acoording to the type of column.

import pandas as pd

def function():
    #i) Read the dataset in dataframe.
    df=pd.read_csv("Salaries .csv")
    #print(df)
    # ii) display first five records.
    print(df.head(5))
    # v) display last ten records.
    print(df.head(10))
    # vi) display the columns inside the dataset.
    print(df.columns)
    # vii) display shape of data.
    rows,columns=df.shape
    print(f"rows={rows},columns={columns}")
    # viii) describe the dataset.
    print("describe the dataset")
    print(df.describe())
    print("Info:")
    print(df.info())
    # x) display types of each columns.
    print("types of each columns:")
    print(df.dtypes)
    # xi) Find out maximum,minimum,mean,median,standard deviation value of each column.
    #print(df)
    print("Mean")
    print(df.mean)

    print("Maximum value:")
    maximum_value=df.max(numeric_only=True)
    print(maximum_value)

    print("Manimum value:")
    manimum_value=df.max(numeric_only=True)
    print(manimum_value)

    print("Mean value:")
    mean_value=df.mean(numeric_only=True)
    print(mean_value)

    print("Median value:")
    median_value=df.median(numeric_only=True)
    print(median_value)

    print("std value:")
    std_value=df.std(numeric_only=True)
    print(std_value)

    



function()

