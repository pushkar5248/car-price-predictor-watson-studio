import pandas as pd
import numpy as np
import re

# ==== CONFIG ====
input_csv_path = r"D:\COURSES\PBEL AI INTERNSHIP\OTHER STUFF\ML DATA SET WITH AUTOAI\Car Price Prediction\dataset optimisation\testfile11.csv"
output_csv_path = r"D:\COURSES\PBEL AI INTERNSHIP\OTHER STUFF\ML DATA SET WITH AUTOAI\Car Price Prediction\dataset optimisation\testfile12.csv"
# ================

def clean_price(value):
    if pd.isna(value) or "N/A" in str(value).upper() or "CONCEPT" in str(value).upper():
        return np.nan

    # Remove $ and commas
    value = re.sub(r"[^0-9\-/.\s]", "", str(value))

    # Handle range with dash or slash
    if "-" in value or "/" in value:
        parts = re.findall(r"\d+\.?\d*", value)
        if len(parts) >= 2:
            return round((float(parts[0]) + float(parts[1])) / 2)

    # Single number case
    numbers = re.findall(r"\d+\.?\d*", value)
    if numbers:
        return round(float(numbers[0]))

    return np.nan

# Use ISO-8859-1 encoding to avoid UnicodeDecodeError
df = pd.read_csv(input_csv_path, encoding='ISO-8859-1')

# Apply cleaning
df['Price ($)'] = df['Cars_Prices'].apply(clean_price)

# Save cleaned file
df.to_csv(output_csv_path, index=False)

print("✔ Price ($) column optimized and saved.")
