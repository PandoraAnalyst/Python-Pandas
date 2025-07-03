
## ITERATING A PANDAS DATAFRAME TO DISPLAY THE COLUMNS

import pandas as pd

## Dataset

data = {
    'student': ["Pandora", "John", "Dave", "Mich", "Jane"],
    'ranks': [1,2,3,4,5],
    'scores': [90, 84,92,23,83]
}

## USING THE 'index' ARG TO SET/NAME OUR OWN INDEXES

df = pd.DataFrame(data, index = ['Student1', 'Student2', 'Student3', 'Student4', 'Student5'])

print("student Records: \n\n", df)

## ITERATING

print("\n Displaying the columns")

for col in df:
    print(col)



