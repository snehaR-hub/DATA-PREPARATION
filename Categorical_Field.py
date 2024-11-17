'''Re-expressing categorical field values in a dataset involves changing or transforming the categories of a field into a new set of labels or categories. This can be done for standardization, encoding, or simply for better readability. You can use Python’s pandas library to handle categorical data transformations effectively.

Here are several ways to re-express categorical field values in Python using pandas:

1. Replacing Specific Categorical Values
If you want to replace one or more categories in a categorical column with new labels, you can use the replace() method.'''

#Example: Replacing Specific Categories

import pandas as pd

# Sample DataFrame
data = {
    'Category': ['Low', 'Medium', 'High', 'Low', 'Medium']
}
df = pd.DataFrame(data)

# Re-express 'Low' to 'L', 'Medium' to 'M', 'High' to 'H'
df['Category'] = df['Category'].replace({'Low': 'L', 'Medium': 'M', 'High': 'H'})

print(df)
#Output:
  Category
0        L
1        M
2        H
3        L
4        M
'2. Using map() to Re-express Categorical Values
'The map() function is particularly useful when you want to map each category to a new value using a dictionary or a function. It's ideal for straightforward re-expression, especially when you're dealing with simple one-to-one mappings.

#Example: Re-expressing with map()

# Mapping categorical values with a dictionary
df['Category'] = df['Category'].map({'Low': 'L', 'Medium': 'M', 'High': 'H'})

print(df)
'''3. Standardizing Categorical Values Using String Operations
If the categorical values have inconsistent capitalization, extra spaces, or spelling mistakes, you can use string methods like str.lower(), str.strip(), or str.replace() to standardize the values.

Example: Standardizing Categories (Case & Space)'''

# Sample DataFrame with inconsistent categorical values
data = {
    'Category': ['low', '  Medium ', 'High', 'low ', 'MEDIUM']
}
df = pd.DataFrame(data)

# Standardizing the categories: lower case and strip extra spaces
df['Category'] = df['Category'].str.lower().str.strip()

# Re-express 'low' to 'L', 'medium' to 'M', 'high' to 'H'
df['Category'] = df['Category'].replace({'low': 'L', 'medium': 'M', 'high': 'H'})

print(df)
#Output:

  Category
0        L
1        M
2        H
3        L
4        M
'''4. Re-express Categorical Data Using pd.Categorical
You can convert the categorical field to pandas.Categorical to change the ordering of categories or handle them more efficiently. You can also use this to re-order or re-label categories.

Example: Re-Ordering Categorical Data'''

# Sample DataFrame
data = {
    'Category': ['Low', 'High', 'Medium', 'Low', 'High']
}
df = pd.DataFrame(data)

# Convert to pandas Categorical with custom order
df['Category'] = pd.Categorical(df['Category'], categories=['Low', 'Medium', 'High'], ordered=True)

print(df)
#Output:mathematica
  Category
0      Low
1     High
2   Medium
3      Low
4     High
'The ordered=True argument enables comparison between categories (e.g., <, >, ==) and changes the way they are stored in memory.

'''5. Using replace() for Complex Re-Expression
You can also use replace() for more complex scenarios where you need to apply a function or conditional transformations to your categorical values.

Example: Using replace() with Functions'''

# Sample DataFrame
df = pd.DataFrame({
    'Category': ['Low', 'Medium', 'High', 'Very High', 'Very Low']
})

# Replace categories using a function
def map_category(cat):
    if cat == 'Low':
        return 'L'
    elif cat == 'Medium':
        return 'M'
    elif cat == 'High':
        return 'H'
    else:
        return 'VH'

df['Category'] = df['Category'].replace(map_category)

print(df)
#Output:
  Category
0        L
1        M
2        H
3       VH
4        L
'''6. Using LabelEncoder for Numerical Encoding
If you need to convert categorical labels into numerical values (for machine learning purposes, for example), you can use the LabelEncoder from sklearn.

Example: Label Encoding Categorical Variables'''

from sklearn.preprocessing import LabelEncoder

# Sample DataFrame
df = pd.DataFrame({
    'Category': ['Low', 'Medium', 'High', 'Low', 'High']
})

# Initialize the encoder
encoder = LabelEncoder()

# Apply label encoding
df['Category_encoded'] = encoder.fit_transform(df['Category'])

print(df)
#Output:mathematica
  Category  Category_encoded
0      Low                 1
1    Medium                 2
2     High                 0
3      Low                 1
4     High                 0
'Here, the categories have been mapped to integers: High -> 0, Low -> 1, and Medium -> 2.

'''7. One-Hot Encoding Categorical Variables
For categorical variables that are not ordinal (i.e., have no meaningful order), one-hot encoding is a common technique to convert them into a binary matrix of 0s and 1s.

Example: One-Hot Encoding with pandas'''

# Sample DataFrame
df = pd.DataFrame({
    'Category': ['Low', 'Medium', 'High', 'Low', 'High']
})

# Perform one-hot encoding
df_one_hot = pd.get_dummies(df, columns=['Category'])

print(df_one_hot)
#Output:
   Category_High  Category_Low  Category_Medium
0              0             1                0
1              0             0                1
2              1             0                0
3              0             1                0
4              1             0                0
