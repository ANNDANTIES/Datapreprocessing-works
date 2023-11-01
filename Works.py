!pip install pandas
##Remove row duplicates

import pandas as pd

# Replace 'input.csv' with the path to your CSV file
input_file = '/content/final_before.csv'

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(input_file)

# Remove duplicate rows based on all columns
df = df.drop_duplicates()

# Save the DataFrame back to a new CSV file or overwrite the original file
output_file = '/content/output.csv'
df.to_csv(output_file, index=False)
## REMOVE DUPLICATE ROWS WITHOT CONSIDERING ANY COLUMN
import pandas as pd

# Replace 'input.csv' with the path to your CSV file
input_file = '/content/output.csv'

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(input_file)

# Define the columns to consider when checking for duplicates
# Replace 'column_to_ignore' with the actual column name(s) to exclude
columns_to_ignore = ['soilmoist_at15cm']

# Remove duplicate rows based on all columns except the specified ones
df = df.drop_duplicates(subset=[col for col in df.columns if col not in columns_to_ignore])

# Save the DataFrame back to a new CSV file or overwrite the original file
output_file = '/content/final.csv'
df.to_csv(output_file, index=False)
### FILES MERGING


import pandas as pd
import glob

# Define the directory where your CSV files are located
csv_files = glob.glob('path_to_csv_directory/*.csv')

# Create an empty DataFrame to store the merged data
merged_data = pd.DataFrame()

# Loop through the CSV files and append them to the merged_data DataFrame
for file in csv_files:
    df = pd.read_csv(file)
    merged_data = merged_data.append(df, ignore_index=True)

# Specify the path and name for the merged CSV file
merged_file = 'merged_data.csv'

# Save the merged DataFrame to a CSV file
merged_data.to_csv(merged_file, index=False)
