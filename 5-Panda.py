#!/usr/bin/python3
"""Import the library Panda for Data Structure"""
import pandas as pd
"""
Data Wrangling is the process of converting data from the initial
format to a format that may be better for analysis."""
import matplotlib.pylab as plt

filename = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/auto.csv"

headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]

df = pd.read_csv(filename, names = headers)

print("-" * 80)

"""In the car dataset, missing data comes with the question mark "?". We replace "?" with NaN
(Not a Number), which is Python's default missing value marker, for reasons of computational
speed and convenience"""
import numpy as np
df.replace("?", np.nan, inplace = True)
print(df.head(5))
print("-" * 80)

missing_data = df.isnull()
print(missing_data.head(5))
print("-" * 80)
print("Count missing values in each column")

for column in missing_data.columns.values.tolist():
    print(column)
    print (missing_data[column].value_counts())
    print("")

print("-" * 80)

"""calculate the average in normalized-losses and replace in NaN"""

avg_norm_loss = df["normalized-losses"].astype("float").mean(axis=0)
print("Average of normalized-losses:", avg_norm_loss)
df["normalized-losses"].replace(np.nan, avg_norm_loss, inplace=True)

"""calculate the average in bore and replace in NaN"""

avg_bore=df['bore'].astype('float').mean(axis=0)
print("Average of bore:", avg_bore)
df["bore"].replace(np.nan, avg_bore, inplace=True)

"""calculate the average in stroke and replace in NaN"""

avg_stroke=df['stroke'].astype('float').mean(axis=0)
print("Average of stroke:", avg_stroke)
df["stroke"].replace(np.nan, avg_stroke, inplace=True)

"""calculate the average in horsepower and replace in NaN"""

avg_horsepower = df['horsepower'].astype('float').mean(axis=0)
print("Average horsepower:", avg_horsepower)
df['horsepower'].replace(np.nan, avg_horsepower, inplace=True)

"""calculate the average in peak-rpm and replace in NaN"""

avg_peakrpm=df['peak-rpm'].astype('float').mean(axis=0)
print("Average peak rpm:", avg_peakrpm)
df['peak-rpm'].replace(np.nan, avg_peakrpm, inplace=True)

print("-" * 80)

"""calculate the name more frequently in num of dors and replace in NaN"""

print(df['num-of-doors'].value_counts())
print(df['num-of-doors'].value_counts().idxmax())
df["num-of-doors"].replace(np.nan, "four", inplace=True)

print("-" * 80)

"""simply drop whole row with NaN in "price" column"""
df.dropna(subset=["price"], axis=0, inplace=True)

"""reset index, because we droped two rows"""
df.reset_index(drop=True, inplace=True)

"""We obtain the dataset with no missing values."""
print(df.head())
