
## =============================== DATETIME OPERATIONS - PANDAS =================================================== ##
## SOME METHODS USED FOR THIS OPERATION INCLUDE:
## 1. Timestamp.now() - Used to GET THE CURRENT DATE AND TIME in the local timezone.
## 2. Pandas.dayofweek - A Pandas attribute used to GET THE DAY OF THE WEEK.
## 3. Pandas.dayofyear - A Pandas attribute used to GET THE DAY OF THE YEAR.
## 4. Pandas.daysinmonth - A Pandas attribute used to GET THE NUMBER OF DAYS IN A MONTH.
## 5. Pandas.is_leap_year - A Pandas attribute used to CHECK IF THE YEAR IS A LEAP YEAR.
## 6. Pandas.is_month_end - A Pandas attribute used to CHECK IF DATE IS LAST DAY OF THE MONTH.
## 7. Pandas.is_month_start - A Pandas attribute used to CHECK IF DATE IS FIRST DAY OF THE MONTH.
## 8. Pandas.is_year_end - A Pandas attribute used to CHECK IF DATE IS LAST DAY OF THE YEAR.
## 9. Pandas.is_year_start - A Pandas attribute used to CHECK IF DATE IS FIRST DAY OF THE YEAR.


## DATETIME OPERATIONS EXAMPLE
import  pandas as pd
from pandas import Timestamp

# 1. USING 'Timestamp.now()'
print("\n1. The current date and time is:\n", pd.Timestamp.now())


# 2. USING 'Pandas.dayofweek'
# Creating a timestamp
time_stamp = pd.Timestamp(year=2025, month=7, day=8, hour=16)

# displaying the date
print("\n2. The current date is:\n", time_stamp)

# displaying the day of week
print("\n2. The day of the week is:\n", time_stamp.dayofweek)


# 3. USING 'Pandas.dayofyear'
print("\n3. The day of the year is:\n", time_stamp.dayofyear)


# 4. USING 'Pandas.daysinmonth'
print("\n4. The number of days in a month:\n", time_stamp.daysinmonth)


# 5. USING 'Pandas.is_leap_year'
print("\n5. Check if year is leap year:\n", time_stamp.is_leap_year)


# 6. USING 'Pandas.is_month_end'
print("\n6. Check if date is last day of the month:\n", time_stamp.is_month_end)


# 7. USING 'Pandas.is_month_start'
print("\n7. Check if date is first day of the month:\n", time_stamp.is_month_start)


# 8. USING 'Pandas.is_year_end'
print("\n8. Check if date is last day of the year:\n", time_stamp.is_year_end)


# 9. USING 'Pandas.is_year_start'
print("\n9. Check if date is first day of the year:\n", time_stamp.is_year_start)


















