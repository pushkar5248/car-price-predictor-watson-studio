import pandas as pd

# ✅ Original file paths
input_csv = r"D:\COURSES\PBEL AI INTERNSHIP\OTHER STUFF\ML DATA SET WITH AUTOAI\Car Price Prediction\dataset optimisation\testfile5.csv"
output_csv = r"D:\COURSES\PBEL AI INTERNSHIP\OTHER STUFF\ML DATA SET WITH AUTOAI\Car Price Prediction\dataset optimisation\testfile6.csv"

# 🔄 Load the dataset
df = pd.read_csv(input_csv)

# 🔧 Normalize strings: lowercase, strip spaces
df['Fuel Type'] = df['Fuel Type'].astype(str).str.strip().str.lower()

# 🧠 Define fuel type cleaning function
def clean_fuel_type(value):
    if 'plug-in' in value or 'plug in' in value:
        return 'Plug-in Hybrid'
    elif 'hybrid' in value or 'ev' in value:
        return 'Hybrid'
    elif 'electric' in value:
        return 'Electric'
    elif 'hydrogen' in value:
        return 'Hydrogen'
    elif 'diesel' in value and 'petrol' in value:
        return 'Petrol'  # Choose dominant type if both are present
    elif 'diesel' in value:
        return 'Diesel'
    elif 'petrol' in value:
        return 'Petrol'
    elif 'cng' in value:
        return 'CNG'
    elif 'lpg' in value:
        return 'LPG'
    else:
        return 'Other'  # fallback for unknown cases

# ⚙️ Apply the cleaning function
df['Fuel Type'] = df['Fuel Type'].apply(clean_fuel_type)

# 💾 Save the cleaned dataset
df.to_csv(output_csv, index=False)

print("✅ Fuel Type column cleaned and saved successfully.")
