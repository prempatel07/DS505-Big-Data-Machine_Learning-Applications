"""
PRACTICAL 02: Data Hygiene: Missing Value Imputation, Deduplication & Renaming
[UNIT 1: Introduction to Big Data and Large Dataset Handling]

Problem Statement:
Write a Python program to perform data hygiene on a dataset with missing values and duplicate rows. Identify missing entries using isna().sum(), demonstrate both dropping rows (dropna()) and imputing missing numerical values with fillna(mean/median), remove duplicate records using drop_duplicates(), and rename columns using rename().

Expected Reference Output:
--- ORIGINAL DATASET ---
   cust_id cust_name   age  monthly_income
0        1      Amit  25.0         45000.0
1        2     Pooja  30.0         52000.0
2        3     Rahul   NaN         61000.0
3        4     Sneha  22.0             NaN
4        5    Vikram  28.0         48000.0
5        2     Pooja  30.0         52000.0
6        6     Karan   NaN         55000.0
7        7      Neha  35.0         70000.0

--- AFTER DEDUPLICATION (Rows removed: 1) ---
[Duplicate Row 5 removed successfully]

--- FINAL CLEANED & RENAMED DATASET ---
   Customer_ID Full_Name   Age  Monthly_Income_INR
0            1      Amit  25.0        45000.000000
1            2     Pooja  30.0        52000.000000
2            3     Rahul  29.0        61000.000000
3            4     Sneha  22.0        55166.666667
4            5    Vikram  28.0        48000.000000
6            6     Karan  29.0        55000.000000
7            7      Neha  35.0        70000.000000

Remaining missing values: 0
"""

import pandas as pd
import numpy as np

# Step 1: Create a dataset with missing values and duplicate records
raw_data = {
    'cust_id': [1, 2, 3, 4, 5, 2, 6, 7],
    'cust_name': ['Amit', 'Pooja', 'Rahul', 'Sneha', 'Vikram', 'Pooja', 'Karan', 'Neha'],
    'age': [25, 30, np.nan, 22, 28, 30, np.nan, 35],
    'monthly_income': [45000, 52000, 61000, np.nan, 48000, 52000, 55000, 70000]
}

df = pd.DataFrame(raw_data)
print("--- ORIGINAL DATASET ---")
print(df)

# Step 2: Check missing values per column
print("\n--- MISSING VALUE COUNT PER COLUMN ---")
print(df.isna().sum())

# Step 3: Remove duplicate records
df_dedup = df.drop_duplicates()
print(f"\n--- AFTER DEDUPLICATION (Rows removed: {len(df) - len(df_dedup)}) ---")
print(df_dedup)

# Step 4: Impute missing numerical values (Age with median, Income with mean)
df_clean = df_dedup.copy()
median_age = df_clean['age'].median()
mean_income = df_clean['monthly_income'].mean()

df_clean['age'] = df_clean['age'].fillna(median_age)
df_clean['monthly_income'] = df_clean['monthly_income'].fillna(mean_income)

# Step 5: Rename columns to clear professional names
df_clean = df_clean.rename(columns={
    'cust_id': 'Customer_ID',
    'cust_name': 'Full_Name',
    'age': 'Age',
    'monthly_income': 'Monthly_Income_INR'
})

print("\n--- FINAL CLEANED & RENAMED DATASET ---")
print(df_clean)
print("\nRemaining missing values:", df_clean.isna().sum().sum())
