"""
PRACTICAL 03: In-Memory Optimization via Dtype Downcasting & Deep Profiling
[UNIT 1: Introduction to Big Data and Large Dataset Handling]

Problem Statement:
Write a Python program to demonstrate in-memory optimization of large datasets. Profile baseline memory usage using memory_usage(deep=True), downcast integer columns (int64 -> int32/int16), downcast float columns (float64 -> float32), and convert repetitive string columns to category type. Report the total percentage reduction in RAM footprint.

Expected Reference Output:
--- BASELINE MEMORY PROFILING ---
User_ID               int64
Age                   int64
Account_Balance     float64
Subscription_Type    object
Active_Status        object
dtype: object
Initial Memory Usage: 13.78 MB

--- OPTIMIZED MEMORY PROFILING ---
User_ID                int16
Age                     int8
Account_Balance      float32
Subscription_Type   category
Active_Status       category
dtype: object
Optimized Memory Usage: 1.05 MB
Memory Footprint Reduction: 92.38% RAM Saved!
"""

import pandas as pd
import numpy as np

# Step 1: Synthesize a 100,000-row dataset with unoptimized default types
np.random.seed(42)
n_rows = 100_000

df = pd.DataFrame({
    'User_ID': np.random.randint(1000, 9999, size=n_rows, dtype='int64'),
    'Age': np.random.randint(18, 70, size=n_rows, dtype='int64'),
    'Account_Balance': np.random.uniform(500.0, 50000.0, size=n_rows),
    'Subscription_Type': np.random.choice(['Basic', 'Standard', 'Premium', 'VIP'], size=n_rows),
    'Active_Status': np.random.choice(['Active', 'Inactive'], size=n_rows)
})

# Step 2: Measure baseline deep memory footprint
baseline_mem = df.memory_usage(deep=True).sum() / (1024 * 1024)
print("--- BASELINE MEMORY PROFILING ---")
print(df.dtypes)
print(f"Initial Memory Usage: {baseline_mem:.2f} MB")

# Step 3: Perform intelligent dtype optimization
df_opt = df.copy()

# Downcast integers
df_opt['User_ID'] = pd.to_numeric(df_opt['User_ID'], downcast='integer')
df_opt['Age'] = pd.to_numeric(df_opt['Age'], downcast='integer')

# Downcast floats
df_opt['Account_Balance'] = pd.to_numeric(df_opt['Account_Balance'], downcast='float')

# Convert repetitive object strings to category
df_opt['Subscription_Type'] = df_opt['Subscription_Type'].astype('category')
df_opt['Active_Status'] = df_opt['Active_Status'].astype('category')

# Step 4: Measure optimized memory usage
opt_mem = df_opt.memory_usage(deep=True).sum() / (1024 * 1024)
savings_pct = ((baseline_mem - opt_mem) / baseline_mem) * 100

print("\n--- OPTIMIZED MEMORY PROFILING ---")
print(df_opt.dtypes)
print(f"Optimized Memory Usage: {opt_mem:.2f} MB")
print(f"Memory Footprint Reduction: {savings_pct:.2f}% RAM Saved!")
