
## =============================== GROUPING DATA & PERFORMING OPERATIONS - PANDAS =================================================== ##

import pandas as pd

# Sample data
data  = {
    "Player": ["Pandora", "John", "Dave", "Pandora", "Mich"],
    "Rank": [1,4,3,2,5],
    "Year": [2025, 2024, 2023, 2022, 2021]
}

# Creating the dataframe
df = pd.DataFrame(data)
print("\nThe sample dataframe:\n", df)

## 1. SPLITTING THE OBJECT & COMBINING THE RESULT, USING groupby().
# - Group the data by 'Player' column. .first() is used to return the first non-empty entries of the df
grouped_data = df.groupby('Player')
print("\n1. Data Grouped by Player:\n", grouped_data.first())


## 2. ITERATE THE GROUP.
# - We can iterate and loop through groups with 'groupby()' by using the 'for-in' loop.
for name, group in grouped_data:
    print("\n2. Looping through the groups:\n", name)
    print(group)


## 3. VIEW THE GROUP
# - The 'groups' property is used to view the group.
view_group = df.groupby('Player').groups
print("\nViewing the groups:\n", view_group)


## 4. AGGREGATE OPERATIONS
# - We can perform aggregate operations on grouped data using the 'agg()' method with 'numpy.mean()'.

# import numpy as np

# Sample data
data2  = {
    "Player": ["Pandora", "John", "Dave", "Jane", "Mich"],
    "Rank": [1,4,3,2,5],
    "Points": [99, 68, 85, 92, 43],
    "Year": [2025, 2024, 2023, 2022, 2023]
}

# Creating the dataframe
df2 = pd.DataFrame(data2)
print("\nThe second sample dataframe:\n", df)

# grouping
second_group = df2.groupby('Year')

# Performing mean aggregation using agg("mean")
aggregated_points = second_group['Points'].agg("mean")
print("\nThe aggregated points using agg('mean'):\n", aggregated_points)


# Performing size aggregation using agg("size")
aggregated_size = second_group['Points'].agg("size")
print("\nThe aggregated size using agg('size'):\n", aggregated_size)






