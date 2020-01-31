# Data-Analysis-with-Python

## Introduction

The Pandas Library is a useful tool that enables us to read various datasets into a data frame.

### Install Ubuntu or Debian

```
sudo apt-get install python3-pandas
```

## 1-PANDA

### Read Data
We use ```pandas.read_csv()``` function to read the csv file. In the bracket, we put the file path along with a quotation mark, so that pandas will read the file into a data frame from that address. 
The file path can be either an URL or your local file address.
Because the data does not include headers, we can add an argument ```headers = None``` inside the read_csv() method, so that pandas will not automatically set the first row as a header.
You can also assign the dataset to any variable you create.

* ```import pandas as pd``` => import the library Panda
* ```df = pd.read_csv(other_path, header=None)``` => Read the file other_path and Not include the headers
* ```df.head(n)``` => show the first n rows using dataframe.head() method
* ```df.tail(n)``` => show the last n rows using dataframe.tail() method
* ```df.columns = headers``` => create a list "headers" that include all column names in order. Then, we use dataframe.columns = headers to replace the headers by the list we created.
* ```df.dropna(subset=["price"], axis=0)```=> drop missing values along the column "price"
* ```df.to_csv("automobile.csv", index=False)``` => Save the database
* ```df.dtypes``` => The main types stored in Pandas dataframes are object, float, int, bool and datetime64.
* ```dataframe.describe()``` => If we would like to get a statistical summary of each column, such as count, column mean value, column standard deviation, etc.
* ```df.describe(include = "all")``` =>it provides the statistical summary of all the columns, including object-typed attributes. We can now see how many unique values, which is the top value and the frequency of top value in the object-typed columns.
* ```df.info``` => Another method you can use to check your dataset
* ```dataframe[[' column 1 ',column 2', 'column 3'] ]``` => You can select the columns of a data frame by indicating the name of each column
* ```avg_norm_loss = df["normalized-losses"].astype("float").mean(axis=0)``` => average of a parameter or attribute
* ```df['num-of-doors'].value_counts()``` =>  To see which values are present in a particular column
* ```df['num-of-doors'].value_counts().idxmax()``` => We can see that four doors are the most common type. We can also use the ".idxmax()" method to calculate for us the most common type automatically:
* ```df.dtypes```=> Lets list the data types for each column
* ```df[["bore", "stroke"]] = df[["bore", "stroke"]].astype("float")``` => Convert data types to proper format
* ```df['city-L/100km'] = 235/df["city-mpg"]``` => create a new column city-L/100km with a value of mpg to L/100km
* ```df[`"city-mpg"] = 235/df["city-mpg"]``` => update the column with a new value
* ```df.rename(columns={'highway-mpg':'highway-L/100km'}, inplace=True)``` => rename the column
* ```df['height'] = df['height']/ df['height'].max()``` Normalization originalValue/maxValue


## BINNING

### Why binning?

Binning is a process of transforming continuous numerical variables into discrete categorical 'bins', for grouped analysis.