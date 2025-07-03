## CREATING A PANDAS DATAFRAME

## Sample Dataset
data = {
    'student': ["Pandora", "John", "Dave", "Mich", "Jane"],
    'ranks': [1,2,3,4,5],
    'scores': [90, 84,92,23,83]
}

## Importing Pandas
import  pandas as pd

df = pd.DataFrame(data)

print("student Records: \n\n", df)