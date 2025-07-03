
## ACCESSING A GROUP OF ROWS OR COLUMNS BY INTEGER POSITIONS  IN A PANDAS DATAFRAME

import pandas as pd

## Dataset

data = {
    'student': ["Pandora", "John", "Dave", "Mich", "Jane"],
    'ranks': [1,2,3,4,5],
    'scores': [90, 84,92,23,83]
}

df = pd.DataFrame(data, index = ['RowA', 'RowB', 'RowC', 'RowD', 'RowE'])

print(df)

## Accessing rows or columns by integer position using 'iloc' attribute.
## NOTE: The 'iloc' attribute uses zero indexing.

print("\n\nValue = ", df.iloc[[0,4]])