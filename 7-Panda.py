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
print("-" * 80)

"""calculate the average in normalized-losses and replace in NaN"""

avg_norm_loss = df["normalized-losses"].astype("float").mean(axis=0)
df["normalized-losses"].replace(np.nan, avg_norm_loss, inplace=True)

"""calculate the average in bore and replace in NaN"""

avg_bore=df['bore'].astype('float').mean(axis=0)
df["bore"].replace(np.nan, avg_bore, inplace=True)

"""calculate the average in stroke and replace in NaN"""

avg_stroke=df['stroke'].astype('float').mean(axis=0)
df["stroke"].replace(np.nan, avg_stroke, inplace=True)

"""calculate the average in horsepower and replace in NaN"""

avg_horsepower = df['horsepower'].astype('float').mean(axis=0)
df['horsepower'].replace(np.nan, avg_horsepower, inplace=True)

"""calculate the average in peak-rpm and replace in NaN"""

avg_peakrpm=df['peak-rpm'].astype('float').mean(axis=0)
df['peak-rpm'].replace(np.nan, avg_peakrpm, inplace=True)


"""calculate the name more frequently in num of dors and replace in NaN"""

df["num-of-doors"].replace(np.nan, "four", inplace=True)


"""simply drop whole row with NaN in "price" column"""
df.dropna(subset=["price"], axis=0, inplace=True)

"""reset index, because we droped two rows"""
df.reset_index(drop=True, inplace=True)


"""Convert data types to proper format"""
df[["bore", "stroke"]] = df[["bore", "stroke"]].astype("float")
df[["normalized-losses"]] = df[["normalized-losses"]].astype("int")
df[["price"]] = df[["price"]].astype("float")
df[["peak-rpm"]] = df[["peak-rpm"]].astype("float")

"""Data Standardization"""
df["city-mpg"] = 235/df["city-mpg"]
df.rename(columns={'city-mpg':'city-L/100km'}, inplace=True)
df["highway-mpg"] = 235/df["highway-mpg"]
df.rename(columns={'highway-mpg':'highway-L/100km'}, inplace=True)

"""Normalization
Normalization is the process of transforming values of several variables into a similar range. 
Typical normalizations include scaling the variable so the variable average is 0,
scaling the variable so the variance is 1, or scaling variable so the variable values range from 0 to 1
"""
df['length'] = df['length']/df['length'].max()
df['width'] = df['width']/df['width'].max()
df['height'] = df['height']/ df['height'].max()

df["horsepower"]=df["horsepower"].astype(int, copy=True)
"""Draw in a histogram of horspower """
#%matplotlib inline
import matplotlib as plt
from matplotlib import pyplot
plt.pyplot.hist(df["horsepower"])

# set x/y labels and plot title
plt.pyplot.xlabel("horsepower")
plt.pyplot.ylabel("count")
plt.pyplot.title("horsepower bins")


"""We would like 3 bins of equal size bandwidth so we use numpy's
 linspace(start_value, end_value, numbers_generated function)"""
bins = np.linspace(min(df["horsepower"]), max(df["horsepower"]), 4)
print(bins)

group_names = ['Low', 'Medium', 'High']

df['horsepower-binned'] = pd.cut(df['horsepower'], bins, labels=group_names, include_lowest=True )
print('-' * 80)
print(df[['horsepower','horsepower-binned']].head(20))
print('-' * 80)
print(df["horsepower-binned"].value_counts())


""" Check the dataframe above carefully, you will find the last column provides
 the bins for "horsepower" with 3 categories ("Low","Medium" and "High"). """
#%matplotlib inline
import matplotlib as plt
from matplotlib import pyplot
pyplot.bar(group_names, df["horsepower-binned"].value_counts())

# set x/y labels and plot title
plt.pyplot.xlabel("horsepower")
plt.pyplot.ylabel("count")
plt.pyplot.title("horsepower bins")

dummy_variable_1 = pd.get_dummies(df["fuel-type"])
dummy_variable_1.head()

dummy_variable_1.rename(columns={'fuel-type-diesel':'gas', 'fuel-type-diesel':'diesel'}, inplace=True)
dummy_variable_1.head()

# merge data frame "df" and "dummy_variable_1" 
df = pd.concat([df, dummy_variable_1], axis=1)

# drop original column "fuel-type" from "df"
df.drop("fuel-type", axis = 1, inplace=True)
print("UPDATE"+"."*80)
print(df.head())
print("UPDATE2"+"."*80)
dummy_variable_2 = pd.get_dummies(df["aspiration"])
dummy_variable_2.rename(columns={'aspiration':'std', 'aspiration':'turbo'}, inplace=True)
df = pd.concat([df, dummy_variable_2], axis=1)
df.drop("aspiration", axis = 1, inplace=True)
print(df.head())
