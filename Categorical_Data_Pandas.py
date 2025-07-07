
## =============================== CATEGORICAL DATE IN PANDAS =================================================== ##
## CATEGORICAL DATE IS A TYPE OF DATA/VARIABLE THAT TAKES ON A LIMITED NUMBER OF POSSIBLE VALUES.
# - EXAMPLES INCLUDE: GENDER, BLOOD TYPE, RATING, ETC.

import  pandas as pd

## 1. Creating a Categorical Series
## To create a categorical series, we need to assign the 'dtype' arg = 'category'
cat_series = pd.Series(["p", "q", "r", "s", "q"], dtype= "category")
print("\n Categorical Series: \n", cat_series)


## 2. Creating a Categorical DataFrame
## To create a categorical Dataframe, we need to assign the 'dtype' arg = 'category'
cat_df = pd.DataFrame({"cat1": list("pqrs"), "cat2": list("abcd"), "cat3": list("ghij")}, dtype= "category")
print("\n Categorical DataFrame: \n", cat_df)


## APPENDING NEW CATEGORIES - To achieve this, we use the 'add_categories()' method.
cat_series2 = pd.Series(["p", "q", "r", "s", "q", "z", "a"], dtype= "category")

# Appending new category    - using '.cat.add_categories()'
cat_series2 = cat_series2.cat.add_categories("v")
print("\n Appended category:\n", cat_series2)

# Adding a list of categories
cat_series2 = cat_series2.cat.add_categories(list("mno"))
print("\n Added list of categories:\n", cat_series2)



## REMOVING NEW CATEGORIES - To achieve this, we use the 'remove_categories()' method.
cat_series2 = pd.Series(["p", "q", "r", "s", "q", "z", "a"], dtype= "category")

# Removing new category    - using '.cat.remove_categories()'
cat_series2 = cat_series2.cat.remove_categories("r")
print("\n Removed category:\n", cat_series2)

# Removing a list of categories
cat_series2 = cat_series2.cat.remove_categories(list("zas"))
print("\n Removed list of categories:\n", cat_series2)




















