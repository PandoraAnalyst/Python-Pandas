
## JOINING DATAFRAMES TOGETHER - This is used to merge two or more datasets together.

import  pandas as pd

## Sample Datasets
data1 = {
    'Id' : ["S01", "S02", "S03", "S04", "S05" ],
    'Student': ["Pandora", "John", "Dave", "Mich", "Jane"],
    'Roll': [101, 102, 103, 104, 105]
}

data2 = {
    'ranks': [1,4,3,5,2],
    'scores': [90, 84,92,23,83]
}

## Creating the dataframes
dataframe1 = pd.DataFrame(data1)
dataframe2 = pd.DataFrame(data2)

## Joining the dataframes
joined_dataframe = dataframe1.join(dataframe2)
print("\nJoined Dataframe:\n ", joined_dataframe)
