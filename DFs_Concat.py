
## CONCATENATING DATAFRAMES  - This is used to concat the contents of the Dataframes.
## Achieved using 'concat()' method

import  pandas as pd

## Sample Datasets
data1 = {
    'Id' : ["S01", "S02", "S03", "S04", "S05" ],
    'Student': ["Pandora", "John", "Dave", "Mich", "Jane"],
    'Roll': [101, 102, 103, 104, 105]
}

data2 = {
    'Id' : ["S06", "S07", "S08"],
    'Student': ["Kate", "Eve", "David"],
    'Roll': [106, 107, 108],
}

## Creating the dataframes
dataframe1 = pd.DataFrame(data1)
dataframe2 = pd.DataFrame(data2)

## Concatenating the dataframes
concatenated_dataframe = pd.concat([dataframe1, dataframe2])
print("\nConcatenated Dataframe:\n ", concatenated_dataframe)
