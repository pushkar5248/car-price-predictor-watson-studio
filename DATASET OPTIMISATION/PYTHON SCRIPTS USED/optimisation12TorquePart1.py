
import pandas as pd
import numpy as np
import re

# ==== CONFIG ====
input_csv_path = r"D:\COURSES\PBEL AI INTERNSHIP\OTHER STUFF\ML DATA SET WITH AUTOAI\Car Price Prediction\dataset optimisation\testfile12.csv"
output_csv_path = r"D:\COURSES\PBEL AI INTERNSHIP\OTHER STUFF\ML DATA SET WITH AUTOAI\Car Price Prediction\dataset optimisation\testfile13.csv"
# ================

def clean_torque(value):
    if pd.isna(value):
        return np.nan

    value = str(value)

    # Remove units, + signs, brackets, text like (GT Model)
    value = re.sub(r"\(.*?\)", "", value)
    value = value.replace('+', '')
    value = re.sub(r"[^\d\-/.\s]", "", value)

    # Handle ranges or slashes (e.g., 100 - 140 or 190 / 140)
    if '-' in value or '/' in value:
        parts = re.findall(r"\d+\.?\d*", value)
        if len(parts) >= 2:
            avg = (float(parts[0]) + float(parts[1])) / 2
            return round(avg)

    # Single number case
    numbers = re.findall(r"\d+\.?\d*", value)
    if numbers:
        return round(float(numbers[0]))

    return np.nan

# Load CSV
df = pd.read_csv(input_csv_path, encoding='ISO-8859-1')

# Apply cleaning
df['Torque (Nm)'] = df['Torque'].apply(clean_torque)

# Save updated dataset
df.to_csv(output_csv_path, index=False)

print("✔ Torque (Nm) column optimized and saved.")
