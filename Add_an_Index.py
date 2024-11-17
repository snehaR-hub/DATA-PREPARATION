Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
... '''In R, you can use the dplyr package or base R functions to add an index column to a data frame. Here's how:
... 
... Method 1: Using dplyr package
... Install and load the dplyr package if you haven't already:
... 
... install.packages("dplyr")
... library(dplyr)
... Add an index column using the mutate() function:'''
... 
... # Example data frame
... df <- data.frame(Name = c("Alice", "Bob", "Charlie"), Age = c(25, 30, 35))
... 
... # Add an index column
... df <- df %>%
...   mutate(Index = row_number())
... 
... print(df)
... '''Method 2: Using Base R
... You can also add an index using the seq_along() function from base R:'''
... 
... # Example data frame
... df <- data.frame(Name = c("Alice", "Bob", "Charlie"), Age = c(25, 30, 35))
... 
... # Add an index column
... df$Index <- seq_along(df$Name)
... 
... print(df)
... '''Both methods will result in a new column "Index" that holds the row numbers.
... In Python, you can use the pandas library to easily add an index column to a DataFrame.
... 
... Method 1: Using pandas
... pip install pandas
... Add an index column using pandas:'''
... 
... import pandas as pd
... 
... # Example DataFrame
... df = pd.DataFrame({
...     'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35]
})

# Add an index column
df['Index'] = df.index + 1  # You can add +1 to start from 1 instead of 0

print(df)
Method 2: Using reset_index()
If you already have an existing DataFrame and want to add the index as a column:

# Reset the index and add it as a column
df_reset = df.reset_index(drop=False)  # drop=False keeps the index column

