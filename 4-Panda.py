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

print(df.head())
print("-" * 80)

"""In the car dataset, missing data comes with the question mark "?". We replace "?" with NaN (Not a Number), which is Python's default missing value marker, for reasons of computational speed and convenience"""
import numpy as np
df.replace("?", np.nan, inplace = True)
print(df.head(5))
