"""
PRACTICAL 01: Dataset Ingestion, Inspection & Descriptive Statistics with Pandas
[UNIT 1: Introduction to Big Data and Large Dataset Handling]

Problem Statement:
Write a Python program using Pandas to load a structured dataset (CSV/JSON), display its first 5 rows, last 5 rows, dimensions (shape), column names, and data types with info(). Generate comprehensive summary statistics of all numeric and categorical attributes using describe(include='all').

Expected Reference Output:
--- FIRST 5 RECORDS (head) ---
   Transaction_ID Customer_Name  Age   Department  Purchase_Amount  Satisfaction_Score
0             101         Aarav   28  Electronics         12500.50                 4.5
1             102          Diya   34     Clothing          4200.00                 3.8
2             103         Rohan   22  Electronics         18900.75                 4.9
3             104        Ananya   45         Home          3100.25                 3.2
4             105        Vivaan   31     Clothing          6500.00                 4.0

--- DATASET SHAPE (Rows, Columns) ---
(10, 6)

--- COLUMN NAMES ---
['Transaction_ID', 'Customer_Name', 'Age', 'Department', 'Purchase_Amount', 'Satisfaction_Score']

--- DESCRIPTIVE SUMMARY STATISTICS ---
       Transaction_ID Customer_Name        Age   Department  Purchase_Amount  Satisfaction_Score
count       10.000000            10  10.000000           10        10.000000           10.000000
mean       105.500000           NaN  34.400000          NaN     10420.225000            4.150000
std          3.027650           NaN   9.418658          NaN      6669.940919            0.587367
min        101.000000           NaN  22.000000          NaN      3100.250000            3.200000
max        110.000000           NaN  52.000000          NaN     22400.000000            4.900000
"""

import pandas as pd
import numpy as np

# Step 1: Create a representative customer sales dataset
data = {
    'Transaction_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Customer_Name': ['Aarav', 'Diya', 'Rohan', 'Ananya', 'Vivaan', 'Isha', 'Kabir', 'Meera', 'Aditya', 'Sanya'],
    'Age': [28, 34, 22, 45, 31, 29, 52, 26, 38, 41],
    'Department': ['Electronics', 'Clothing', 'Electronics', 'Home', 'Clothing', 'Electronics', 'Home', 'Clothing', 'Electronics', 'Home'],
    'Purchase_Amount': [12500.50, 4200.00, 18900.75, 3100.25, 6500.00, 14200.00, 8900.50, 5100.00, 22400.00, 7800.25],
    'Satisfaction_Score': [4.5, 3.8, 4.9, 3.2, 4.0, 4.7, 3.5, 4.2, 4.8, 3.9]
}

df = pd.DataFrame(data)

# Step 2: Inspect DataFrame structure
print("--- FIRST 5 RECORDS (head) ---")
print(df.head())

print("\n--- LAST 5 RECORDS (tail) ---")
print(df.tail())

print("\n--- DATASET SHAPE (Rows, Columns) ---")
print(df.shape)

print("\n--- COLUMN NAMES ---")
print(df.columns.tolist())

print("\n--- DATASET INFORMATION & DTYPES ---")
df.info()

print("\n--- DESCRIPTIVE SUMMARY STATISTICS ---")
print(df.describe(include='all'))
