"""
PRACTICAL 09: Missing Value Imputation with SimpleImputer & Categorical Encoding
[UNIT 3: Preparing Big Data for Machine Learning]

Problem Statement:
Write a Python program using Scikit-Learn to preprocess a machine learning dataset: handle missing numerical values using SimpleImputer with the mean strategy, transform categorical text labels into ordinal integers using LabelEncoder, and convert nominal variables to binary dummy indicators using One-Hot Encoding.

Expected Reference Output:
--- ORIGINAL DATASET ---
   Applicant_ID  Credit_Score  Income_k  Education Loan_Approved
0           101         710.0      55.0  Bachelors           Yes
1           102           NaN      62.0    Masters            No
2           103         680.0       NaN        PhD           Yes
3           104         750.0      80.0  Bachelors           Yes
4           105           NaN      48.0    Masters            No
5           106         620.0      50.0  Bachelors            No

--- PROCESSED & ENCODED MACHINE LEARNING READY DATASET ---
   Applicant_ID  Credit_Score   Income_k  Loan_Approved_Encoded  Edu_Bachelors  Edu_Masters  Edu_PhD
0           101         710.0  55.000000                      1           True        False    False
1           102         690.0  62.000000                      0          False         True    False
2           103         680.0  59.000000                      1          False        False     True
3           104         750.0  80.000000                      1           True        False    False
4           105         690.0  48.000000                      0          False         True    False
5           106         620.0  50.000000                      0           True        False    False

LabelEncoder Mapping: {'No': 0, 'Yes': 1}
"""

import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder

# Step 1: Create raw dataset with missing values and categorical features
raw_data = {
    'Applicant_ID': [101, 102, 103, 104, 105, 106],
    'Credit_Score': [710, np.nan, 680, 750, np.nan, 620],
    'Income_k': [55.0, 62.0, np.nan, 80.0, 48.0, 50.0],
    'Education': ['Bachelors', 'Masters', 'PhD', 'Bachelors', 'Masters', 'Bachelors'],
    'Loan_Approved': ['Yes', 'No', 'Yes', 'Yes', 'No', 'No']
}
df = pd.DataFrame(raw_data)
print("--- ORIGINAL DATASET ---")
print(df)

# Step 2: Handle Missing Numerical Values with SimpleImputer
imputer = SimpleImputer(strategy='mean')
df[['Credit_Score', 'Income_k']] = imputer.fit_transform(df[['Credit_Score', 'Income_k']])

# Step 3: Encode Target Variable using LabelEncoder
le = LabelEncoder()
df['Loan_Approved_Encoded'] = le.fit_transform(df['Loan_Approved'])

# Step 4: One-Hot Encode 'Education' category
df_encoded = pd.get_dummies(df, columns=['Education'], prefix='Edu', drop_first=False)

print("\n--- PROCESSED & ENCODED MACHINE LEARNING READY DATASET ---")
print(df_encoded.drop(columns=['Loan_Approved']))
print(f"\nLabelEncoder Mapping: {dict(zip(le.classes_, le.transform(le.classes_)))}")
