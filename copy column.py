import pandas as pd

# Load the datasets
file1_path = '/Users/marsguy/Desktop/Research/CH HEI/CH_food_nutrients.csv'
file2_path = '/Users/marsguy/Desktop/Research/CH HEI/FPED_CH_KCAL.csv'

df1 = pd.read_csv(file1_path)
df2 = pd.read_csv(file2_path)

# Ensure 'SEQN' column exists in both dataframes
if 'SEQN' not in df1.columns:
    print(f"Error: 'SEQN' column not found in {file1_path}")
    exit()

if 'SEQN' not in df2.columns:
    print(f"Error: 'SEQN' column not found in {file2_path}")
    exit()

# Define the column to copy
column_to_copy = 'Sodium' # Assuming this is the column you want to copy

if column_to_copy not in df1.columns:
    print(f"Error: '{column_to_copy}' column not found in {file1_path}")
    exit()

# Merge df1 into df2 based on 'SEQN' to copy the column
# This will add 'HEI2015_Total_Score' from df1 to df2, matching on 'SEQN'
df2_updated = pd.merge(df2, df1[['SEQN', column_to_copy]], on='SEQN', how='left')

# Save the updated df2 to a new CSV file or overwrite the existing one
output_file_path = '/Users/marsguy/Desktop/Research/CH HEI/FPED_CH_KCAL.csv'
df2_updated.to_csv(output_file_path, index=False)

print(f"Column '{column_to_copy}' copied from '{file1_path}' to '{file2_path}' based on 'SEQN'.")
print(f"Updated data saved to '{output_file_path}'.")
