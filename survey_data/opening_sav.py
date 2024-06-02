import pandas as pd
import pyreadstat

# Read the .sav file
file_path = 'SPSS data file for computations 2023-24-1.sav'
df, meta = pyreadstat.read_sav(file_path)

# Display the first few rows of the dataframe
print("First few rows of the data:")
print(df.head())

# Display the column labels
print("\nColumn labels:")
print(meta.column_labels)

# Save the data to a CSV file for better readability
csv_file_path = 'output.csv'
df.to_csv(csv_file_path, index=False)
print(f"\nData has been saved to {csv_file_path}")