# import os
# import pandas as pd
# from random import shuffle

# # Directory containing CSV files
# directory = './Prompt injection Prevention/Datasets/'

# # Initialize an empty list to store dataframes
# dfs = []

# # Iterate over each file in the directory
# for filename in os.listdir(directory):
#     if filename.endswith(".csv"):
#         filepath = os.path.join(directory, filename)
        
#         # Read CSV file into a dataframe
#         df = pd.read_csv(filepath)
        
#         # Shuffle rows of the dataframe
#         df = df.sample(frac=1).reset_index(drop=True)
        
#         # Append the shuffled dataframe to the list
#         dfs.append(df)

# # Merge all dataframes into one
# merged_df = pd.concat(dfs, ignore_index=True)

# # Write merged dataframe to a new CSV file
# merged_csv_path = './Prompt injection Prevention/Final Dataset/Dataset.csv'
# merged_df.to_csv(merged_csv_path, index=False)

# print(f'Merged CSV saved to: {merged_csv_path}')

# Replace with your actual CSV file path
# csv_file = './Prompt injection Prevention/Final Dataset/Dataset.csv'

# # Read CSV file into a DataFrame
# df = pd.read_csv(csv_file)

# # Drop rows where all columns are NaN (empty rows)
# df.dropna(how='all', inplace=True)

# # Reset index after dropping rows
# df.reset_index(drop=True, inplace=True)

# # Save cleaned DataFrame back to CSV
# cleaned_csv_file = './Prompt injection Prevention/Final Dataset/cleaned_Dataset.csv'
# df.to_csv(cleaned_csv_file, index=False)

# print(f'Cleaned CSV saved to: {cleaned_csv_file}')

import pandas as pd

# Read the CSV file
df = pd.read_csv('./Final Dataset/cDataset.csv')

# Drop empty rows
df.dropna(inplace=True)
# Replace values in 'Value' column that are not 0 or 1 with 1
df['Value'] = df['Value'].apply(lambda x: 1 if x != 0 and x != 1 else x)

# Write back to CSV
df.to_csv('cleaned_dataset.csv', index=False)
