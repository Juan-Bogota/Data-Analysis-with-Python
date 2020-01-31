#!/usr/bin/python3
"""Import the library Panda for Data Structure"""
import pandas as pd

"""Read the online file by the URL provides above, and assign it to variable (df)"""
other_path = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/auto.csv"
df = pd.read_csv(other_path, header=None)

""" Create Header list"""
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]

df.columns = headers
"""Drop missing values along the column "price" as follows"""
df.dropna(subset=["price"], axis=0)
print("Types")
print("-" * 80)
print(df.dtypes)
print("-" * 80)
print(df.describe())
print("-" * 80)
print(df.describe(include = "all"))
