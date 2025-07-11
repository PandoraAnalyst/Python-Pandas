
## =============================== DATA CLEANING - PANDAS =================================================== ##
## THERE ARE SOME METHODS THAT ARE USED IN DATA CLEANING:
## 1. isnull() - Used to find the NULL values and replace them with 'True'. For non-NULL values, 'False' is returned.
## 2. notnull() - Used to find the NOT NULL values and replace them with 'True'. For NULL values, 'False' is returned.
## 3. dropna() - Used to drop and remove rows with null values
## 4. fillna() - Used to replace NULL values with a specific value.

## DATA CLEANING EXAMPLE.
import pandas as pd

# Loading a CSV file
df = pd.read_csv(r"C:\Users\Beattris\Documents\Book1_data_cleaning.csv")
print("\n The raw data:\n", df)

# USING 'isnull()' TO FIND NULL VALUES
null_df = df.isnull()
print("\nChecked for null values:\n", null_df)


# USING 'notnull()' TO FIND NOT NULL VALUES
not_null_df = df.notnull()
print("\nChecked for not null values:\n", not_null_df)


# USING 'dropna()' TO DROP/REMOVE ROWS WITH NULL VALUES
dropna_df = df.dropna()
print("\nNew df after dropping rows with null values:\n", dropna_df)


# USING 'fillna()' TO DROP/REMOVE ROWS WITH NULL VALUES
fillna_df = df.fillna(99.9)
print("\nNew df after filling the rows with null values:\n", fillna_df)
