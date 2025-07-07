
## =============================== READING CSV FILES IN PANDAS =================================================== ##
# This is achieved using the 'read_csv()' method.

import pandas as pd

# LOADING CSV IN A DATFRAME
# - There are 2 ways to specify the path:
# /* 1. Add 'r' first before the file path (r stands for "raw"); e.g instead of:
# "C:\Users\Beattris\Documents\Book1.csv", USE r"C:\Users\Beattris\Documents\Book1.csv"
# 2. Use double slashes e.g instead:
# "C:\Users\Beattris\Documents\Book1.csv", USE "C:\\Users\\Beattris\\Documents\\Book1.csv"
# */

df = pd.read_csv(r"C:\Users\Beattris\Documents\Book1.csv")

# Displaying the CSV
print("\nDisplaying the CSV:\n", df)

# Displaying the top 3 rows
print("\nTop 3 records:\n", df.head(3))

# Displaying the last 3 rows
print("\nLast 3 records:\n", df.tail(3))



## =============================== READING EXCEL FILES IN PANDAS =================================================== ##
# This is achieved using the 'read_excel()' method.
# NOTE: The 'openpyxl' package must be installed for excel files to be read

df2 = pd.read_excel(r"C:\Users\Beattris\Documents\Book2.xlsx")

# Displaying the xlsx
print("\nDisplaying the xlsx file:\n", df2)

# Displaying the top 3 rows
print("\nTop 3 records:\n", df2.head(3))

# Displaying the last 3 rows
print("\nLast 3 records:\n", df2.tail(3))













