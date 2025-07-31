import pandas as pd

# === STEP 1: Input your CSV file path here ===
input_csv = r'D:\COURSES\PBEL AI INTERNSHIP\OTHER STUFF\ML DATA SET WITH AUTOAI\Car Price Prediction\dataset optimisation\FINAL STUFF\car_price_prediction_MLoptimisedDataSet.csv'
output_csv = r'D:\COURSES\PBEL AI INTERNSHIP\OTHER STUFF\ML DATA SET WITH AUTOAI\Car Price Prediction\dataset optimisation\FINAL STUFF\cleaned_final_dataset.csv'

# === STEP 2: Load the CSV file ===
df = pd.read_csv(input_csv)

# === STEP 3: Ensure target column is numeric ===
target_column = 'Price ($)'
df[target_column] = pd.to_numeric(df[target_column], errors='coerce')

# === STEP 4: Handle missing values in the target column ===
if df[target_column].isnull().sum() > 0:
    median_price = df[target_column].median()
    df[target_column] = df[target_column].fillna(median_price)

# === STEP 5: Capitalize relevant text/categorical columns (example: Company, Fuel_Type) ===
columns_to_capitalize = ['Company', 'Fuel_Type']  # Add more if needed
for col in columns_to_capitalize:
    if col in df.columns:
        df[col] = df[col].astype(str).str.upper()

# === STEP 6: Handle missing values in all other categorical columns ===
# You can replace NaNs in object columns with 'UNKNOWN' or mode
for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].fillna('UNKNOWN')

# === STEP 7: Export cleaned file ===
df.to_csv(output_csv, index=False)
print(f"✅ Cleaned dataset saved to:\n{output_csv}")
