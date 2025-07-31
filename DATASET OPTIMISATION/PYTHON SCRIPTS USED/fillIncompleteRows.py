import pandas as pd
import numpy as np

# Input and Output Paths
input_csv = r"D:\COURSES\PBEL AI INTERNSHIP\OTHER STUFF\ML DATA SET WITH AUTOAI\Car Price Prediction\CarPricePredictionModelTrainingDatasetMLoptimisedFinal.csv"
output_csv = r"D:\COURSES\PBEL AI INTERNSHIP\OTHER STUFF\ML DATA SET WITH AUTOAI\Car Price Prediction\testfile2.csv"

# Load CSV
df = pd.read_csv(input_csv)

# Function to convert string ranges like '6.0 – 8.1' into average values
def clean_range_values(val):
    try:
        if isinstance(val, str) and ('-' in val or '\x96' in val):
            val = val.replace('\x96', '-')
            parts = val.split('-')
            nums = [float(p.strip()) for p in parts if p.strip()]
            if len(nums) == 2:
                return np.mean(nums)
        return float(val)
    except:
        return np.nan

# Convert string ranges and non-numeric garbage in numeric columns
for col in df.columns:
    if df[col].dtype == 'object':
        try:
            df[col] = df[col].apply(clean_range_values)
            df[col] = pd.to_numeric(df[col], errors='ignore')
        except:
            continue

# Identify numeric and categorical columns
numeric_cols = df.select_dtypes(include=['number']).columns
categorical_cols = df.select_dtypes(include=['object', 'category']).columns

# Fill numeric columns with median
for col in numeric_cols:
    df[col] = df[col].fillna(df[col].median())

# Fill categorical columns with mode
for col in categorical_cols:
    if not df[col].mode().empty:
        mode_val = df[col].mode()[0]
        df[col] = df[col].fillna(mode_val)
    else:
        df[col] = df[col].fillna("Unknown")

# Save the cleaned DataFrame
df.to_csv(output_csv, index=False)
print(f"✅ Cleaned dataset saved as: {output_csv}")
