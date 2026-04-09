# CLEANING:
# - empty cells
# - data in wrong format
# - wrong data
# - duplicates

import pandas as pd

df = pd.read_csv("data.csv")
#print(df.info())

####################### EMPTY CELLS #######################

## Remove Rows
new_df = df.dropna() #inplace=True (to change origin)

## Replace Values
new_df_all_130 = df.fillna(130)

## Replace in Particular Column
df.fillna({"Calories": 130}, inplace=True)

## Mean (average), Medial (middle val when sorted), Mode (most frequente)
x = df["Calories"].mean()
y = df["Calories"].median()
z = df["Calories"].mode()[0]

print(f"average: {x}, median= {y}, most frequent: {z}")

####################### WRONG FORMAT #######################

data = pd.read_csv("data.csv")

## Convert all data to specif. Format

data['Date'] = pd.to_datetime(data['Date'], format='mixed') # convert every value to Date

## Remove Rows

data.dropna(subset=['Date'], inplace = True)

#print(data.to_string())

####################### WRONG DATA #######################

## Replacing

data.loc[7, 'Duration'] = 45 # set value to 1 particular cell

for x in data.index: # check the boundaries
    if data.loc[x, 'Duration'] > 120:
        data.loc[x, 'Duration'] = 120

       

## Removing

for x in data.index:
    if data.loc[x, 'Duration'] > 59:
        data.drop(x, inplace=True)

#print(data.to_string()) 


####################### DUPLICATES #######################

row_data = pd.read_csv("data.csv")

print(row_data.duplicated()) # index & Boolen if it's duplicated

row_data.drop_duplicates(inplace = True) # remove duplicates

print(row_data.to_string())