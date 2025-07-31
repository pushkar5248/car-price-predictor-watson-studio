import pandas as pd
import re

# File paths
input_csv = r"D:\COURSES\PBEL AI INTERNSHIP\OTHER STUFF\ML DATA SET WITH AUTOAI\Car Price Prediction\dataset optimisation\testfile6.csv"
output_csv = r"D:\COURSES\PBEL AI INTERNSHIP\OTHER STUFF\ML DATA SET WITH AUTOAI\Car Price Prediction\dataset optimisation\testfile7.csv"

# Load dataset
df = pd.read_csv(input_csv)

# Function to extract engine displacement in liters
def extract_engine_size(engine_str):
    match = re.search(r'(\d\.\d)\s*[Ll]', str(engine_str))
    if match:
        return float(match.group(1))
    return None

# Function to extract cylinder configuration (V6, I4, etc.)
def extract_engine_cylinders(engine_str):
    engine_str = str(engine_str).upper().replace("-", "").replace(" ", "")
    patterns = ["V6", "V8", "V12", "V10", "I4", "I3", "I5", "I6", "BOXER4", "BOXER6", "W12"]
    for pattern in patterns:
        if pattern in engine_str:
            return pattern
    return None

# Apply functions
df["Engine_Size_L"] = df["Engine"].apply(extract_engine_size)
df["Engine_Cylinders"] = df["Engine"].apply(extract_engine_cylinders)

# Save the cleaned dataset
df.to_csv(output_csv, index=False)

print("✅ Engine column cleaned and new features added successfully.")
