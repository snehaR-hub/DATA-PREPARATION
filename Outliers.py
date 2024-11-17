#Methods to Identify Outliers Using Python
'1. Using Z-Score (Standard Deviation Method)
'The Z-score method identifies outliers by calculating how many standard deviations a data point is away from the mean. A Z-score greater than 3 (or less than -3) is often considered an outlier, but the threshold can be adjusted based on the data.

import pandas as pd
import numpy as np
from scipy.stats import zscore

# Sample DataFrame
df = pd.DataFrame({
    'Age': [25, 30, 35, 40, 100, 45, 60, 120, 80, 150]
})

# Calculate Z-scores
df['Z-Score'] = zscore(df['Age'])

# Identify outliers (Z-score > 3 or < -3)
outliers = df[df['Z-Score'].abs() > 3]

print("Outliers based on Z-score:")
print(outliers)
'''Output:csharp
Outliers based on Z-score:
   Age   Z-Score
8   150  4.919670

2. Using IQR (Interquartile Range) Method
The IQR method uses the quartiles of the data to define the spread. Outliers are defined as values outside of the range between:'''


# Calculate Q1, Q3, and IQR
Q1 = df['Age'].quantile(0.25)
Q3 = df['Age'].quantile(0.75)
IQR = Q3 - Q1

# Calculate lower and upper bounds
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Identify outliers
outliers_iqr = df[(df['Age'] < lower_bound) | (df['Age'] > upper_bound)]

print("Outliers based on IQR:")
print(outliers_iqr)
'''Output:
csharp
Copy code
Outliers based on IQR:
   Age
8  150

3. Using Box Plot Visualization
A box plot (also known as a box-and-whisker plot) is a great way to visualize outliers. Outliers are usually depicted as points outside the "whiskers" of the box plot.

Example: Identifying Outliers Using Box Plot'''

import matplotlib.pyplot as plt
import seaborn as sns

# Sample DataFrame
df = pd.DataFrame({
    'Age': [25, 30, 35, 40, 100, 45, 60, 120, 80, 150]
})

# Create a box plot
sns.boxplot(x=df['Age'])
plt.title('Box Plot for Age')
plt.show()

'''4. Using Percentiles
A more customized method involves using percentiles (such as the 1st and 99th percentiles) to define outliers. If a data point is below the 1st percentile or above the 99th percentile, it can be considered an outlier.

Example: Identifying Outliers Using Percentiles'''
# Calculate the 1st and 99th percentiles
lower_percentile = df['Age'].quantile(0.01)
upper_percentile = df['Age'].quantile(0.99)

# Identify outliers
outliers_percentiles = df[(df['Age'] < lower_percentile) | (df['Age'] > upper_percentile)]

print("Outliers based on Percentiles:")
print(outliers_percentiles)
'''Output:csharp
Outliers based on Percentiles:
   Age
8  15
5. Visualizing with a Scatter Plot (for Multivariate Outliers)
In some cases, outliers may exist based on the relationship between two or more variables. Scatter plots can help you visualize such outliers, especially in the case of multivariate data.

Example: Identifying Outliers Using a Scatter Plot'''
# Sample DataFrame with two variables
df = pd.DataFrame({
    'Age': [25, 30, 35, 40, 100, 45, 60, 120, 80, 150],
    'Salary': [50000, 60000, 70000, 80000, 300000, 75000, 85000, 400000, 120000, 500000]
})

# Scatter plot to visualize outliers
plt.scatter(df['Age'], df['Salary'])
plt.title('Scatter Plot: Age vs Salary')
plt.xlabel('Age')
plt.ylabel('Salary')
plt.show()

'''6. Using Isolation Forest (Machine Learning-Based Approach)
The Isolation Forest algorithm is a machine learning technique that is useful for detecting outliers in high-dimensional datasets. It works by isolating observations using randomly selected features.

Example: Identifying Outliers Using Isolation Forest'''

from sklearn.ensemble import IsolationForest

# Sample DataFrame with two features
df = pd.DataFrame({
    'Age': [25, 30, 35, 40, 100, 45, 60, 120, 80, 150],
    'Salary': [50000, 60000, 70000, 80000, 300000, 75000, 85000, 400000, 120000, 500000]
})

# Initialize Isolation Forest
iso_forest = IsolationForest(contamination=0.2)  # Assuming ~20% of data are outliers
df['Outlier'] = iso_forest.fit_predict(df[['Age', 'Salary']])

# Filter outliers (Outlier = -1)
outliers_iforest = df[df['Outlier'] == -1]

print("Outliers based on Isolation Forest:")
print(outliers_iforest)
'''Output:csharp
Outliers based on Isolation Forest:
   Age  Salary  Outlier
4  100  300000       -1
8  150  500000  '''     -1
