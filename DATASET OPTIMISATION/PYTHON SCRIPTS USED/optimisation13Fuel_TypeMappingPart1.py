import pandas as pd

# === INPUT / OUTPUT PATHS ===
input_csv_path = r'D:\COURSES\PBEL AI INTERNSHIP\OTHER STUFF\ML DATA SET WITH AUTOAI\Car Price Prediction\dataset optimisation\testfile13.csv'
output_csv_path = r'D:\COURSES\PBEL AI INTERNSHIP\OTHER STUFF\ML DATA SET WITH AUTOAI\Car Price Prediction\dataset optimisation\testfile14.csv'

# === READ DATA ===
df = pd.read_csv(input_csv_path, encoding='utf-8')

# === DEFINE MAPPING FOR Fuel_Type ===
fuel_mapping = {
    'P': 0,     # Petrol
    'D': 1,     # Diesel
    'H': 2,     # Hybrid
    'E': 3,     # Electric
    'PH': 4,    # Plug-in Hybrid
    'HD': 5     # Hydrogen
}

# === APPLY MAPPING ===
df['Fuel_Type'] = df['Fuel_Type'].map(fuel_mapping)

# === SAVE UPDATED CSV ===
df.to_csv(output_csv_path, index=False)
print("✅ Fuel_Type column mapped and file saved successfully.")
