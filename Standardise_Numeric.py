'''Standardizing numeric fields (also known as feature scaling or normalization) is a crucial step in many data science workflows, especially when preparing data for machine learning models. Standardization typically refers to scaling a numeric field to have a mean of 0 and a standard deviation of 1, which is achieved by subtracting the mean and dividing by the standard deviation.
In Python, the most common library for this task is scikit-learn, but you can also perform standardization using pandas and NumPy if you prefer a more manual approach.

1. Standardizing with scikit-learn's StandardScaler
The most common and reliable way to standardize numeric data is by using scikit-learn's StandardScaler. This standardizes data by subtracting the mean and dividing by the standard deviation.

Steps: Install scikit-learn (if not already installed):'''

'pip install scikit-learn
'Use StandardScaler to standardize your numeric fields.

'Example: Standardization with StandardScaler

import pandas as pd
from sklearn.preprocessing import StandardScaler

# Sample DataFrame
df = pd.DataFrame({
    'Age': [25, 30, 35, 40, 45],
    'Salary': [50000, 60000, 70000, 80000, 90000]
})

# Initialize StandardScaler
scaler = StandardScaler()

# Fit the scaler to the data and transform it (standardization)
df[['Age', 'Salary']] = scaler.fit_transform(df[['Age', 'Salary']])

print(df)
#Output:
'''        Age    Salary
0 -1.414214 -1.414214
1 -0.707107 -0.707107
2  0.000000  0.000000
3  0.707107  0.707107
4  1.414214  1.414214'''

'2. Manual Standardization Using pandas and NumPy
'If you want to manually standardize your data, you can use basic pandas and NumPy operations. This is useful when you want more control over the process or don't want to install extra libraries.

'Steps:Standardization formula:Standardized Value = Value − Mean
#Example: Manual Standardization
import pandas as pd
import numpy as np

# Sample DataFrame
df = pd.DataFrame({
    'Age': [25, 30, 35, 40, 45],
    'Salary': [50000, 60000, 70000, 80000, 90000]
})

# Standardize 'Age' and 'Salary' manually
df['Age'] = (df['Age'] - df['Age'].mean()) / df['Age'].std()
df['Salary'] = (df['Salary'] - df['Salary'].mean()) / df['Salary'].std()

print(df)
'''Output:
        Age    Salary
0 -1.414214 -1.414214
1 -0.707107 -0.707107
2  0.000000  0.000000
3  0.707107  0.707107
4  1.414214  1.414214'''

'''3. Standardizing Using MinMaxScaler for Scaling Between a Specific Range
Sometimes, instead of standardizing to have a mean of 0 and a standard deviation of 1, you might want to scale the numeric values to a specific range (e.g., 0 to 1). You can use the MinMaxScaler from scikit-learn to scale data within a given range.

Example: Standardization with MinMaxScaler'''
from sklearn.preprocessing import MinMaxScaler

# Sample DataFrame
df = pd.DataFrame({
    'Age': [25, 30, 35, 40, 45],
    'Salary': [50000, 60000, 70000, 80000, 90000]
})

# Initialize MinMaxScaler
scaler = MinMaxScaler()

# Fit and transform data to scale between 0 and 1
df[['Age', 'Salary']] = scaler.fit_transform(df[['Age', 'Salary']])

print(df)
'''Output:
   Age  Salary
0  0.00     0.0
1  0.25     0.25
2  0.50     0.50
3  0.75     0.75
4  1.00     1.0'''

'''4. Handling Categorical Variables Before Standardization
If you have categorical variables that need to be standardized numerically (for example, ordinal categories), you may need to convert these to numeric values first. You can do this using LabelEncoder or get_dummies (one-hot encoding).

Example: Handling Categorical Fields with LabelEncoder'''
from sklearn.preprocessing import LabelEncoder

# Sample DataFrame with categorical column
df = pd.DataFrame({
    'Category': ['Low', 'Medium', 'High', 'Low', 'High'],
    'Salary': [50000, 60000, 70000, 80000, 90000]
})

# Initialize LabelEncoder
encoder = LabelEncoder()

# Convert categorical 'Category' to numeric
df['Category'] = encoder.fit_transform(df['Category'])

# Now standardize 'Salary'
scaler = StandardScaler()
df['Salary'] = scaler.fit_transform(df[['Salary']])

print(df)
'''Output:
   Category    Salary
0         1 -1.414214
1         2 -0.707107
2         0  0.000000
3         1  0.707107
4         0  1.414214'''

'''5. Standardizing Only Specific Columns
If you want to standardize only specific numeric columns in a larger DataFrame, you can select those columns and apply the standardization.

Example: Standardizing Only Specific Columns'''

# Sample DataFrame
df = pd.DataFrame({
    'Age': [25, 30, 35, 40, 45],
    'Salary': [50000, 60000, 70000, 80000, 90000],
    'Category': ['Low', 'Medium', 'High', 'Low', 'High']
})

# Initialize StandardScaler
scaler = StandardScaler()

# Standardize only 'Age' and 'Salary' columns
df[['Age', 'Salary']] = scaler.fit_transform(df[['Age', 'Salary']])

print(df)
'''Output:
        Age    Salary Category
0 -1.414214 -1.414214      Low
1 -0.707107 -0.707107   Medium
2  0.000000  0.000000     High
3  0.707107  0.707107      Low
4  1.414214  1.414214     High '''
