import pandas as pd

# Load dataset
df = pd.read_csv("dataset/cleaned_Superstore_Sales_Dataset.csv")

print("First 5 Rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Remove duplicates
df = df.drop_duplicates()

# Save cleaned file
df.to_csv("dataset/final_Superstore_Sales_Dataset.csv", index=False)

print("\nData cleaned successfully!")