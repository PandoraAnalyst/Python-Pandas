
## =============================== INDEXING IN PANDAS =================================================== ##

import  pandas as pd

# 'index_col' is used to tell which column in the dataframe we want to include with the index
df = pd.read_excel(r"C:\Users\Beattris\Documents\Book2.xlsx", index_col="Student")

print(df)

# 1. Using the indexing operator '[]'
result = df["Mark"]

print("\n Indexed df:\n", result)



# 2. Using the loc operator
result2 = df.loc["Mich"]
print("\n Using loc:\n", result2)



# 2. Using the loc operator
result3 = df.iloc[2]
print("\n Using iloc:\n", result3)



## =============================== SELECTING TWO OR MORE COLUMNS IN PANDAS ========================================= ##
## Sample Dataset
data1 = {
    'Id' : ["S01", "S02", "S03", "S04", "S05" ],
    'Student': ["Pandora", "John", "Dave", "Mich", "Jane"],
    'Roll': [101, 102, 103, 104, 105]
}

df = pd.DataFrame(data1)

# Selecting 2 columns       - use the '[[]]'
print("\n Selecting 2 columns:\n", df[["Student", "Roll"]])


# Selecting multiple columns    - specify a range [start(includes the number specified):end(excludes the specified number)]
print("\n Selecting multiple columns:\n", df.columns[0:2])


