import pandas as pd
import re
import numpy as np

# Load file
file_path = r'D:\COURSES\PBEL AI INTERNSHIP\OTHER STUFF\ML DATA SET WITH AUTOAI\Car Price Prediction\dataset optimisation\testfile8.csv'
df = pd.read_csv(file_path)

def clean_battery_cc(value):
    text = str(value).replace(',', '').lower()
    
    # Extract CC
    cc_match = re.search(r'(\d{3,5})\s*cc', text)
    cc = int(cc_match.group(1)) if cc_match else None

    # Extract kWh values
    range_match = re.findall(r'(\d+(?:\.\d+)?)\s*[-/]\s*(\d+(?:\.\d+)?)\s*kwh', text)
    if range_match:
        nums = [float(x) for x in range_match[0]]
        kwh = round(sum(nums) / len(nums), 2)
    else:
        all_kwh = re.findall(r'(\d+(?:\.\d+)?)\s*kwh', text)
        kwh = round(sum([float(x) for x in all_kwh]) / len(all_kwh), 2) if all_kwh else None

    # Build final string
    if cc and kwh:
        return f"{cc} cc / {kwh} kWh"
    elif cc:
        return f"{cc} cc"
    elif kwh:
        return f"{kwh} kWh"
    else:
        return ""

# Apply to same column
df['Battery Capacity (CC)'] = df['Battery Capacity (CC)'].apply(clean_battery_cc)


# Save updated file
output_path = r'D:\COURSES\PBEL AI INTERNSHIP\OTHER STUFF\ML DATA SET WITH AUTOAI\Car Price Prediction\dataset optimisation\testfile9.csv'
df.to_csv(output_path, index=False)

print("Column cleaned and overwritten successfully.")
