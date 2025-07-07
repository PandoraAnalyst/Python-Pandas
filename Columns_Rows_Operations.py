
## =============================== ADDING NEW COLUMNS IN PANDAS =================================================== ##
# THERE ARE 2 METHODS USED IN ADDING NEW COLUMNS IN A PANDAS DATAFRAME; THE 'insert()' AND THE 'assign()' METHODS

import pandas as pd

# Sample Dataset
data1 = {
    'Id' : ["S01", "S02", "S03", "S04", "S05" ],
    'Student': ["Pandora", "John", "Dave", "Mich", "Jane"],
    'Roll': [101, 102, 103, 104, 105],
    'Marks': [23, 85, 69, 38, 37]
}

# Creating the dataframe
df = pd.DataFrame(data1)
print("\n the sample dataset:\n" ,df)

## USING THE 'insert()' Method
# - This method allows us to set the location, name, and values of the new column as parameters 1,2, & 3, respectively.
# - Below is an example to insert a new column named "Rank" to the 2nd index of the dataframe
df.insert(2, "Rank", [1, 2, 3, 4, 5])
print("\n Added column using 'insert()':\n", df )


## USING THE 'assign()' Method
# - This method allows us to add a new column to the end of a df. The name of the new column will be a param of the assign().
# - Below is an example to assign a new column named "Gender" to the end of the dataframe
assigned_df = df.assign(Gender = ["F", "M", "M", "M", "F"])
print("\n Added column using 'assign()':\n", assigned_df )



## =============================== DELETING COLUMNS & ROWS IN PANDAS =================================================== ##
## ROWS AND COLUMNS ARE DELETED USING THE 'drop()' METHOD. THE COLUMN TO BE DELETED IS MENTIONED
# - ALONG WITH THE AXIS AS AN ARG OF THE METHOD.

# Dropping a column - Specify the column name, then the 'axis' param must be set to either 'columns' or '1'.

dropped_Col = df.drop("Roll", axis="columns")
print("\n Dropped a column using 'drop()':\n", dropped_Col )


# Dropping a row - Specify the row index number, then the 'axis' param must be set to either 'index' or '0'.

dropped_row = df.drop(2, axis="index")
print("\n Dropped a row using 'drop()':\n", dropped_row )



## =============================== ITERATING OVER COLUMNS & ROWS IN PANDAS =================================================== ##
## ITERATING OVER ROWS.
# - TO ITERATE OVER ROWS, THE 'iterrows()' AND 'itertuples()' METHODS ARE USED.

#Sample dataset
data2 = {
    'Id' : ["S01", "S02", "S03", "S04", "S05" ],
    'Student': ["Pandora", "John", "Dave", "Mich", "Jane"],
    'Roll': [101, 102, 103, 104, 105],
    'Marks': [23, 85, 69, 38, 37]
}

# Creating the dataframe
df2 = pd.DataFrame(data2)

# Iterating over rows using the iterrow()
print("\n iterrow() printing rows:")
for row in df2.iterrows():
    print("\n", row)


# Iterating over rows using the itertuples()    - Here, each row is returned as a tuple object.
print("\n itertuples() printing rows:")
for row in df2.itertuples():
    print("\n", row)


## ITERATING OVER COLUMNS.
# - TO ITERATE OVER COLUMNS, THE 'items()' METHOD IS USED.

#Sample dataset
data3 = {
    'Id' : ["S01", "S02", "S03", "S04", "S05" ],
    'Student': ["Pandora", "John", "Dave", "Mich", "Jane"],
    'Roll': [101, 102, 103, 104, 105],
    'Marks': [23, 85, 69, 38, 37]
}

# Creating the dataframe
df3 = pd.DataFrame(data3)

# Iterating over columns using the items() method
print("\n iterating over each column using items():")
for a,b in df2.items():
    print(a)
    print(b, "\n")






