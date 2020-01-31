#!/usr/bin/python3
"""Import the library Panda for Data Structure"""
import pandas as pd

"""Read the online file by the URL provides above, and assign it to variable (df)"""
other_path = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/auto.csv"
df = pd.read_csv(other_path, header=None)
print("The first 5 rows of the dataframe")
print(df.head())
print("-" * 80)
print("The LAST 10 rows of the dataframe")
print(df.tail(10))
