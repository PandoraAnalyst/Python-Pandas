
## =============================== STRING OPERATIONS - PANDAS =================================================== ##
## THERE ARE SOME METHODS USED TO PERFORM STRING OPERATIONS IN PANDAS. THESE METHODS ARE USED WITH A LEADING '.str'
# - (EXCEPT FOR 'count()') THEN THE METHOD NAME FOLLOWS. BELOW ARE SOME OF THE METHODS:
## 1. lower() - Used to transform a text to lowercase.
## 2. upper() - Used to transform a text to uppercase.
## 3. lower() - Used to transform a text to camel case.
## 4. len() - Used to get the length of each element.
## 5. count() - Used to count the non-empty cells for each column or row.
## 6. contains() - Used to search for a value in a column. contains() is case sensitive when checking for a value.
# - What you pass as a value into the contain() must match the exact way it appears in your data.

## STRING OPERATIONS EXAMPLE
import  pandas as pd

# Sample data
data = ["PaNdoRa", "John", "DAVE", "MiCh", "JanE"]

# Creating a Series for the data
data_series = pd.Series(data)

# Displaying the Series
print("\nThe data series:\n", data_series)


# 1. USING 'lower()'
lower_data = data_series.str.lower()
print("\nData Transformed to lowercase:\n", lower_data)


# 2. USING 'upper()'
upper_data = data_series.str.upper()
print("\nData Transformed to uppercase:\n", upper_data)


# 3. USING 'title()'
title_case_data = data_series.str.title()
print("\nData Transformed to title case:\n", title_case_data)


# 4. USING 'len()'
el_length = data_series.str.len()
print("\nRetrieved length of each element using 'len()':\n", el_length)


# 5. USING 'count()'
import numpy as np

count_dataset = [np.nan, "Pandora", "John", np.nan, "Dave", "Mich", np.nan, "Jane"]
count_dataset_series = pd.Series(count_dataset)

# using the count() method
count_non_empty = count_dataset_series.count()
print("\nUsed count() to count non empty data':\n", count_non_empty)


# 6. USING 'contains()'
check_val = data_series.str.contains("PaNdoRa")
print("\nCheck which index has the value 'Pando':\n", check_val)








