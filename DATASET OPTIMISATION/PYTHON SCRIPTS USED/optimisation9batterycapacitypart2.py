import pandas as pd
import re
import numpy as np

# Load file
file_path = r'D:\COURSES\PBEL AI INTERNSHIP\OTHER STUFF\ML DATA SET WITH AUTOAI\Car Price Prediction\dataset optimisation\testfile8.csv'
df = pd.read_csv(file_path)

def extract_battery_features(text):
    text = str(text).lower().replace(",", "")
    
    # --- Extract CC values ---
    cc_matches = re.findall(r'(\d{3,5})\s*cc', text)
    cc_values = [int(cc) for cc in cc_matches]
    avg_cc = round(sum(cc_values)/len(cc_values), 2) if cc_values else np.nan

    # --- Extract kWh values (ranges or list) ---
    range_matches = re.findall(r'(\d+(?:\.\d+)?)\s*[-/]\s*(\d+(?:\.\d+)?)\s*kwh', text)
    kwh_values = []
    
    if range_matches:
        for r in range_matches:
            nums = [float(r[0]), float(r[1])]
            kwh_values.append(sum(nums)/2)
    else:
        kwh_matches = re.findall(r'(\d+(?:\.\d+)?)\s*kwh', text)
        kwh_values = [float(k) for k in kwh_matches]
    
    avg_kwh = round(sum(kwh_values)/len(kwh_values), 2) if kwh_values else np.nan
    
    return pd.Series([avg_cc, avg_kwh])

# Apply to dataframe
df[['Battery_CC', 'Battery_kWh']] = df['Battery Capacity (CC)'].apply(extract_battery_features)

# Save new file
output_path = r'D:\COURSES\PBEL AI INTERNSHIP\OTHER STUFF\ML DATA SET WITH AUTOAI\Car Price Prediction\dataset optimisation\testfile10.csv'
df.to_csv(output_path, index=False)

print("Battery_CC and Battery_kWh extracted successfully.")
