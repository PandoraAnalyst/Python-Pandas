## ACCESSING A GROUP OF ROWS OR COLUMNS IN A PANDAS DATAFRAME

import pandas as pd

## Dataset

data = {
    'student': ["Pandora", "John", "Dave", "Mich", "Jane"],
    'ranks': [1,2,3,4,5],
    'scores': [90, 84,92,23,83]
}

## 'index' is used to remove the default '0-1' labels df attaches to records

df = pd.DataFrame(data, index = ['RowA', 'RowB', 'RowC', 'RowD', 'RowE'])

print(df)

## Accessing a particular value using 'loc' attribute

print("\n\nValue = ", df.loc['RowA', 'student'])