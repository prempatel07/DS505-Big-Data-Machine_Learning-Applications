"""
PRACTICAL 10: Feature Scaling (StandardScaler vs MinMaxScaler) & Train-Test Split
[UNIT 3: Preparing Big Data for Machine Learning]

Problem Statement:
Write a Python program to perform feature scaling and dataset partitioning. Apply StandardScaler (Z-score normalization) and MinMaxScaler to numerical features, compare their transformed distributions, and split the dataset into training (80%) and testing (20%) sets using train_test_split(..., test_size=0.2, random_state=42).

Expected Reference Output:
--- STANDARDIZED FEATURES (StandardScaler: mu=0, sigma=1) ---
   Feature_Age  Feature_Salary
0       -1.567          -1.353
1       -1.219          -1.137
2       -0.870          -0.643
3       -0.522          -0.427

--- NORMALIZED FEATURES (MinMaxScaler: [0, 1]) ---
   Feature_Age  Feature_Salary
0        0.000           0.000
1        0.111           0.067
2        0.222           0.219
3        0.333           0.286

--- PARTITION SIZES ---
Training Features Shape : (8, 2) | Training Labels: 8
Testing Features Shape  : (2, 2)  | Testing Labels : 2
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.model_selection import train_test_split

# Step 1: Create feature matrix X and target y
np.random.seed(42)
X = pd.DataFrame({
    'Feature_Age': [20, 25, 30, 35, 40, 45, 50, 55, 60, 65],
    'Feature_Salary': [25000, 32000, 48000, 55000, 62000, 71000, 85000, 92000, 110000, 130000]
})
y = np.array([0, 0, 0, 1, 0, 1, 1, 1, 1, 1])

print("--- ORIGINAL FEATURE VALUES ---")
print(X)

# Step 2: Apply StandardScaler (Mean=0, Std=1)
std_scaler = StandardScaler()
X_standardized = std_scaler.fit_transform(X)

# Step 3: Apply MinMaxScaler (Range [0, 1])
minmax_scaler = MinMaxScaler()
X_normalized = minmax_scaler.fit_transform(X)

print("\n--- STANDARDIZED FEATURES (StandardScaler: mu=0, sigma=1) ---")
print(pd.DataFrame(X_standardized, columns=X.columns).round(3).head(4))

print("\n--- NORMALIZED FEATURES (MinMaxScaler: [0, 1]) ---")
print(pd.DataFrame(X_normalized, columns=X.columns).round(3).head(4))

# Step 4: Partition dataset into Train (80%) and Test (20%)
X_train, X_test, y_train, y_test = train_test_split(
    X_standardized, y, test_size=0.20, random_state=42, stratify=y
)

print(f"\n--- PARTITION SIZES ---")
print(f"Training Features Shape : {X_train.shape} | Training Labels: {len(y_train)}")
print(f"Testing Features Shape  : {X_test.shape}  | Testing Labels : {len(y_test)}")
