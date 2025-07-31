import pandas as pd
import re
import sys

def clean_horsepower(value):
    if pd.isnull(value):
        return None

    text = str(value).lower().replace(',', '').replace('estimated', '').replace('(est.)', '').replace('~', '')

    # Handle "up to" values like "Up to 830 hp"
    up_to_match = re.search(r'up to\s*(\d+)', text)
    if up_to_match:
        return int(up_to_match.group(1))

    # Handle ranges like "70-85 hp" or "86 / 89"
    range_match = re.findall(r'(\d+)\s*[-/]\s*(\d+)', text)
    if range_match:
        nums = [int(x) for x in range_match[0]]
        return int(round(sum(nums) / len(nums)))

    # Handle multiple numbers like "86 hp / 89 hp"
    multi_match = re.findall(r'(\d+)', text)
    if len(multi_match) > 1:
        nums = [int(x) for x in multi_match]
        return int(round(sum(nums) / len(nums)))

    # Handle single number
    num_match = re.search(r'(\d+)', text)
    if num_match:
        return int(num_match.group(1))

    return None

# ---------- MAIN PROGRAM ----------

# Input and Output file paths
input_csv_path = r'D:\COURSES\PBEL AI INTERNSHIP\OTHER STUFF\ML DATA SET WITH AUTOAI\Car Price Prediction\dataset optimisation\testfile10.csv'
output_csv_path = r'D:\COURSES\PBEL AI INTERNSHIP\OTHER STUFF\ML DATA SET WITH AUTOAI\Car Price Prediction\dataset optimisation\testfile11.csv'

# Load dataset
df = pd.read_csv(input_csv_path, encoding='ISO-8859-1')


# Clean and update Horsepower column
df['Horsepower (hp)'] = df['Horse_Power'].apply(clean_horsepower)

# Save updated dataset
df.to_csv(output_csv_path, index=False)

print(f"Cleaned data saved to:\n{output_csv_path}")
