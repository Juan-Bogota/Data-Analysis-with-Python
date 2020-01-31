# Data-Analysis-with-Python

## Introduction

The Pandas Library is a useful tool that enables us to read various datasets into a data frame; our Jupyter notebook platforms have a built-in Pandas Library so that all we need to do is import Pandas without installing

Install Ubuntu or Debian

```
sudo apt-get install python3-pandas
```

> ## 1-PANDA

### Read Data
We use ```pandas.read_csv()``` function to read the csv file. In the bracket, we put the file path along with a quotation mark, so that pandas will read the file into a data frame from that address. The file path can be either an URL or your local file address.
Because the data does not include headers, we can add an argument ```headers = None``` inside the read_csv() method, so that pandas will not automatically set the first row as a header.
You can also assign the dataset to any variable you create.

