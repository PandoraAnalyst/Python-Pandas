
## =============================== REMOVE WHITESPACE OR SPECIAL CHARACTERS - PANDAS =================================================== ##
## TO REMOVE WHITESPACES (INCLUDING NEWLINES) OR SET(s) OF SPECIAL CHARACTERS ON TEXT DATA IN A SERIES OR DATAFRAME, USE THESE:
## 1. strip() - Strips whitespaces or special characters from the left and right sides.
## 2. lstrip() - Strips whitespaces or special characters from the left side.
## 3. rstrip() - Strips whitespaces or special characters from the right side.

import  pandas as pd

# Sample dataset
dataset = ["@@Pandora ", " John!", "!Dave\n\n", "$Mich", "Jane@"]

# COnverting to series
dataset_series = pd.Series(dataset)
print("\nThe sample dataset:\n", dataset_series)

# 1. USING 'strip()' method
stripped_both = dataset_series.str.strip(" !\n@")
print("\nStripping both sides:\n", stripped_both)


# 2. USING 'lstrip()' method
stripped_left = dataset_series.str.lstrip(" @!$")
print("\nStripping left side:\n", stripped_left)


# 3. USING 'rstrip()' method
stripped_right = dataset_series.str.rstrip(" @!\n")
print("\nStripping right side:\n", stripped_right)

