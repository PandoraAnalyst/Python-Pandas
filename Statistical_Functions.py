
## =============================== STATISTICAL FUNCTIONS - PANDAS =================================================== ##
## THERE ARE SEVERAL STATISTICAL FUNCTIONS AVAILABLE IN PANDAS FOR STATISTICAL OPERATIONS:
## 1. sum() - Used to return the sum of the values
## 2. count() - Used to return the count of non-empty values
## 3. max() - Used to return the maximum of the values
## 4. min() - Used to return the minimum of the values
## 5. mean() - Used to return the mean of the values
## 6. median() - Used to return the median of the values
## 7. std() - Used to return the standard deviation of the values
## 8. describe() - Used to return the summary statistics of each column


import pandas as pd

## Sample Dataset
marks = {
    "Maths": [56, 96, 43, 39, 96, 66],
    "Science": [86, 79, 93, 65, 38, 50],
    "English": [84, 70, 30, 69, 26, 69]
}

# creating a df
df = pd.DataFrame(marks)
print("\nThe Sample Dataframe:\n", df)


# USING THE 'sum()' FUNCTION -  to display the sum of marks in each column
summed = df.sum()
print("\n1. Summing each column:\n", summed)


# USING THE 'count()' FUNCTION -  to display the count of non-empty values
marks2 = {
    "Maths": [56, 96, None, 39, 96, 66],
    "Science": [86, None, 93, 65, None, 50],
    "English": [84, 70, 30, None, 26, None]
}
df2 = pd.DataFrame(marks2)
counted_vals = df2.count()
print("\n2. Count of non-empty data:\n", counted_vals)


# USING THE 'max()' FUNCTION    - to return the maximum mark in each column
max_val = df.max()
print("\n3. The max mark:\n", max_val)


# USING THE 'min()' FUNCTION    - to return the minimum mark in each column
min_val = df.min()
print("\n4. The min mark:\n", min_val)


## USING THE 'mean()' FUNCTION
mean_val = df.mean()
print("\n5. The mean value:\n", mean_val)


## USING THE 'median()' FUNCTION
median_val = df.median()
print("\n6. The median value:\n", median_val)


## USING THE 'std()' FUNCTION
std_val = df.std()
print("\n7. The standard deviation value:\n", std_val)


## USING THE 'describe()' FUNCTION
des_cols = df.describe()
print("\n7. The summary stat of each column:\n", des_cols)










