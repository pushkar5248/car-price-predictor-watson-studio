import pandas as pd

# File paths
input_csv = r"D:\COURSES\PBEL AI INTERNSHIP\OTHER STUFF\ML DATA SET WITH AUTOAI\Car Price Prediction\dataset optimisation\testfile4.csv"
output_csv = r"D:\COURSES\PBEL AI INTERNSHIP\OTHER STUFF\ML DATA SET WITH AUTOAI\Car Price Prediction\dataset optimisation\testfile5.csv"

# Load CSV
df = pd.read_csv(input_csv)

# Normalize
df['Fuel Type'] = df['Fuel Type'].astype(str).str.strip().str.lower()

# Replace compound and inconsistent strings with clean categories
df['Fuel Type'] = df['Fuel Type'].replace({
    'plug in hybrid': 'Plug-in Hybrid',
    'plug-in hybrid': 'Plug-in Hybrid',
    'hybrid/petrol': 'Hybrid',
    'petrol/hybrid': 'Hybrid',
    'hybrid/electric': 'Hybrid',
    'hybrid / electric': 'Hybrid',
    'hybrid': 'Hybrid',
    'electric': 'Electric',
    'petrol': 'Petrol',
    'diesel': 'Diesel',
    'cng': 'CNG',
    'lpg': 'LPG'
})

# Save the cleaned file
df.to_csv(output_csv, index=False)
print("✅ Fuel Type values cleaned and standardized.")
