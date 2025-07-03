
## DATAFRAME ATTRIBUTES AND METHODS

import pandas as pd

## SAMPLE DATASET
data = {
    'student': ["Pandora", "John", "Dave", "Mich", "Jane"],
    'ranks': [1,4,3,5,2],
    'scores': [90, 84,92,23,83]
}

df = pd.DataFrame(data, index = ['Std1', 'Std2', 'Std3', 'Std4', 'Std5'])

## 1. 'dtypes' ATTRIBUTE        - used to return the datatypes in the df

print("\n Datatypes: \n", df.dtypes)


## 2. 'ndim' ATTRIBUTE      - used to return the number of dimensions of the df

print("\n Number of Dimensions: \n", df.ndim)


## 3. 'size' ATTRIBUTE      - used to find/count the elements(records) in the df

print("\n Number of elements in the dataframe: \n", df.size)


## 4. 'shape' ATTRIBUTE     - used to find out the dimensionality of the df

print("\n Dimensionality of the dataframe: \n", df.shape)


## 5. 'index' ATTRIBUTE     - used to return the index values assigned to the table records

print("\n Index of the dataframe: \n", df.index)



## 6. 'T' ATTRIBUTE     - Used to transpose the rows and columns; that is rows become columns and columns become rows
## NOTE: The 'T' attribute is case-sensitive.

print("\n Transposed dataframe: \n", df.T)


## 7. 'head()' METHOD     - used to return the first n number of records. The number you specify in the ( ) is how
# many records that will be returned to you. Without specifying a value, it will return the first 5  records.

print("\n head method: \n", df.head(2))



## 8. 'tail()' METHOD     - used to return the last n number of records. The number you specify in the ( ) is how
# many records that will be returned to you. Without specifying a value, it will return the last 5  records.

print("\n tail method: \n", df.tail(2))
