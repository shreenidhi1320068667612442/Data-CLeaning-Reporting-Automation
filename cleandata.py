import pandas as pd

# Load dataset
df = pd.read_csv(r"C:\Users\acer\Downloads\projects\amazon_sales_data 2025.csv")

# Remove duplicates
df.drop_duplicates(inplace=True)

# Fill missing values
df.fillna("Unknown", inplace=True)

# Remove extra spaces
df.columns = df.columns.str.strip()

# Save cleaned file
df.to_csv("cleaned_sales_data.csv", index=False)

print("Data Cleaning Completed")
