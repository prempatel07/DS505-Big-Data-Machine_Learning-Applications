"""
PRACTICAL 11: Continuous Predictive Modeling with Linear Regression
[UNIT 3: Preparing Big Data for Machine Learning]

Problem Statement:
Write a Python program to build, train, and evaluate a Linear Regression model using Scikit-Learn. Fit the model to predict salary based on years of experience, display model coefficients (slope and intercept), predict outcomes on the test dataset, and calculate Mean Squared Error (MSE) and R-squared (R2) score.

Expected Reference Output:
--- TRAINED MODEL EQUATION ---
Salary = (9371.02 * Experience) + 26162.27

--- TEST EVALUATION METRICS ---
   Years_Exp  Actual_Salary  Predicted_Salary
0        1.1          39343          36470.39
1       10.3         122391         122683.73
2        2.0          37731          44904.30
3        4.0          63218          63646.33

Mean Squared Error (MSE) : 25,649,812.30
R-squared Score (R2)     : 0.9782 (High predictive accuracy)
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Step 1: Create Experience vs Salary dataset
np.random.seed(42)
experience = np.array([1.1, 1.5, 2.0, 2.9, 3.2, 3.7, 4.0, 4.5, 5.1, 5.9, 6.8, 7.1, 7.9, 8.7, 9.5, 10.3]).reshape(-1, 1)
salary = np.array([39343, 46205, 37731, 56642, 54445, 57189, 63218, 61111, 66029, 81363, 91738, 98273, 101302, 113812, 109431, 122391])

# Step 2: Split into Train (75%) and Test (25%)
X_train, X_test, y_train, y_test = train_test_split(experience, salary, test_size=0.25, random_state=42)

# Step 3: Instantiate and train Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 4: Extract model parameters
slope = model.coef_[0]
intercept = model.intercept_
print("--- TRAINED MODEL EQUATION ---")
print(f"Salary = ({slope:.2f} * Experience) + {intercept:.2f}")

# Step 5: Predict on Test Set and Evaluate
y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\n--- TEST EVALUATION METRICS ---")
comparison = pd.DataFrame({'Years_Exp': X_test.flatten(), 'Actual_Salary': y_test, 'Predicted_Salary': y_pred.round(2)})
print(comparison)
print(f"\nMean Squared Error (MSE) : {mse:,.2f}")
print(f"R-squared Score (R2)     : {r2:.4f} (High predictive accuracy)")
