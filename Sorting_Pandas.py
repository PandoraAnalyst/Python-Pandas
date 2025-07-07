
## =============================== SORTING IN PANDAS =================================================== ##
# SORTING DATA/VALUES IN A PANDAS DATAFRAME IS DONE USING THE 'sort_values()' METHOD

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

## USING THE 'sort_values()' METHOD - Here, a 'by' parameter specifies the column name we want to sort by
# Sorting in Ascending order
sorted_values = df.sort_values(by=['Marks'])
print("\n values sorted in ascending order by marks:\n", sorted_values)

# Sorting in Descending order
sorted_values_desc = df.sort_values(by=['Marks'], ascending=False)
print("\n values sorted in descending order by marks:\n", sorted_values_desc)