# importing the necessary libraries
import pandas as pd
import json


# Part 1


df = pd.read_csv("data.csv") # reading in the dataframe
df_copy = df # making a copy of the dataframe so we don't overwrite the data

print(f"Number of rows in the original csv file: {len(df_copy)}") # prints the number of rows in the original dataframe


df_copy["Profit (in millions)"].tolist() # did a quick visual check and found that the non-numeric value was the string N.A.
numeric_filter = df_copy["Profit (in millions)"] != "N.A." # made a mask that only pulled the rows without the N.A. string
df_copy = df_copy[numeric_filter] # applied the mask so that the dataframe only contained the rows with numeric values

print(f"Number of rows after removing non-numeric values: {len(df_copy)}") # prints the number of rows of the modified dataframe without the non-numeric values


# Part 2


# following process takes the string values in the "profit" column and converts each value to a float
count = 0 
numbers = df_copy["Profit (in millions)"].tolist() #list of all numeric values as strings
while count < len(df_copy):
    df_copy.iloc[count,4] = float(numbers[count])
    count += 1


# making JSON file of our updated dataframe
df_copy.to_json(r'output\data2.json', orient="records",  indent = 2)


# sort the dataframe by the "profit" values in descending order (highest to lowest)
df_copy.sort_values(by=["Profit (in millions)"], inplace=True, ascending = False)


# will print the top 20 rows corresponding to the sorted "profit" column 
print(df_copy.iloc[0:20,:])

