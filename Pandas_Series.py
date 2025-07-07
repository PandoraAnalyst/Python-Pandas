## ===================================  SERIES IN PANDAS =================================================== ##
# THIS IS A ONE-DIMENSIONAL ARRAY, LIKE A COLUMN IN A TABLE. IT IS A LABELED
## ARRAY THAT CAN HOLD DATA OF ANY TYPE. THE 'Series()' METHOD IS USED TO CREATE A PANDAS SERIES.

import  pandas as pd

## Sample dataframe
data = [12, 45, 78, 99, 43]

## Creating a Series
s = pd.Series(data)

print("Pandas Series: \n", s)


## ACCESSING A VALUE FROM A PANDAS SERIES   - this is achieved by specifying the index of the value u want.
print("Accessing a value:\n", s[2])


## NAMING OUR OWN INDEXES (Labels/Custom indexes) A PANDAS SERIES   - this is achieved by adding the 'index' arg to the Series method.
## Sample dataframe
data2 = [123, 425, 478, 939, 442]
s2 = pd.Series(data2, index = ['Num1', 'Num2', 'Num3', 'Num4', 'Num5'])
print("\nNamed Indexes:\n", s2)


## ACCESSING VALUES FROM A PANDAS SERIES USING THEIR LABELS (Custom Index)
# - this is achieved by referring to the custom index name/label of the value we want to access

print("\nAccessing value through the label:\n", s2["Num3"])


## ======================== ATTRIBUTES & METHODS OF PANDAS SERIES  =================================== ##
## Sample dataset
sample_data = [12, 45, 78, 99, 43]

s3 = pd.Series(sample_data)

## 1. 'dtypes' Attribute    - Returns the datatype in the series
print("\n 1. The dtypes attribute:\n", s3.dtype)


## 2. 'ndim' Attribute    - Returns the number of dimensions of the series
print("\n 2. The ndim attribute:\n", s3.ndim)


## 3. 'size' Attribute    - Returns the number of elements in the series
print("\n 3. The size attribute:\n", s3.size)


## 4. 'name' Attribute    - Returns the name of the series
s4 = pd.Series(sample_data, name = "My sample_data series")
print("\n 4. The name attribute:\n", s4.name)


## 5. 'hasnans' Attribute    - Returns TRUE if NANS are in the series.
# NOTE: 'np.nan' is used to generate NaN value in the series
nan_data = [30, np.nan, 74, 930, 38,  np.nan]
s5 = pd.Series(nan_data)

print("\n 5. The hasnans attribute:\n", s5.hasnans)


## 6. 'index' Attribute    - Returns the indexes of elements in the series
print("\n 6. The index attribute:\n", s2.index)


## 7. 'head()' Method    - Returns the first n rows of the series
# - Specify a number in the ( ) of the method, to tell how many rows you want
print("\n 7. The head() method:\n", s2.head())


## 8. 'tail()' Method    - Returns the last n rows of the series
# - Specify a number in the ( ) of the method, to tell how many rows you want
print("\n 8. The tail() method:\n", s2.tail())


## 9. 'info()' Method    - Displays a summary of the series
# - Specify a number in the ( ) of the method, to tell how many rows you want
print("\n 8. The info() method:\n", s2.info())



## ======================== COMBINING TWO PANDAS SERIES  =================================== ##
## THE 'combine()' METHOD IS USED TO ACHIEVE THIS. THE FUNCTION WILL COMPARE EACH ELEMENT OF THE SERIES (both series)
# - THEN RETURN THE LARGEST VALUES FROM BOTH SERIES.
# - THAT IS, IT'LL CHECK THE ELEMENTS AT INDEX 0 IN BOTH SERIES, THEN RETURN THE LARGEST ELEMENT;
# - CHECK INDEX 1, THEN RETURN THE LARGEST ELEMENT, ETC.

## Sample datasets
com_data1 = [12, 45, 78, 99, 43]
com_data2 = [132, 44, 758, 99, 7, 433]

## creating series for both datasets
series1 = pd.Series(com_data1)
series2 = pd.Series(com_data2)

## Fxn to check which series is greater
def check_series(x1,x2):
    if x1 > x2:
        return x1
    else:
        return x2

## Combining the series together
combined_series = series1.combine(series2, check_series)

print("\n Combined Series: \n", combined_series)










