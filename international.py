import pandas as pd
import numpy as np
import re
import nltk
import os
from collections import Counter

# Class for financial planning data handling
class FinancialPlanning:
    # Check whether the file exists
    def file_exists(self, file_path):
        return os.path.isfile(file_path)
    
    def load_dataset(self, file_path):
        # Ensure only CSV files are accepted
        if not file_path.endswith(".csv"):
            raise ValueError("SORRY! You Provided an Unsupported File Format.")

        if not self.file_exists(file_path):
            raise FileNotFoundError(f"OOOOPS! Your file '{file_path}' does not exist.")

        return pd.read_csv(file_path)

# Initialize the class
finance = FinancialPlanning()
file_path = "/home/mikey/Simba/CSVs/financial_planning_data.csv"

try:
    df = finance.load_dataset(file_path)
    print(df.head())
except Exception as e:
    print(e)

# Display dataset info
df.info()

# Checking for missing values
missing_values = df.isnull()
missing_values.head()

# List columns with missing values
for column in missing_values.columns.values.tolist():
    print(column)
    print(missing_values[column].value_counts())
    print("")

# Drop rows where both 'content' and 'summary' are empty
df.dropna(subset=['content', 'summary'], how='all', inplace=True)

# Drop all rows with any NaN values
df.dropna(inplace=True)

# Verify that missing values have been removed
print("Missing values after cleaning:")
print(df.isna().sum())
