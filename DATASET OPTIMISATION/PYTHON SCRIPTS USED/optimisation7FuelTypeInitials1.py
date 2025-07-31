import pandas as pd

# Load the CSV file
input_file = r'D:\COURSES\PBEL AI INTERNSHIP\OTHER STUFF\ML DATA SET WITH AUTOAI\Car Price Prediction\dataset optimisation\final11.csv'
output_file = r'D:\COURSES\PBEL AI INTERNSHIP\OTHER STUFF\ML DATA SET WITH AUTOAI\Car Price Prediction\dataset optimisation\testfile7.csv'

# Read the dataset
df = pd.read_csv(input_file)

# Define fuel type mapping
fuel_map = {
    'petrol': 'P',
    'diesel': 'D',
    'hybrid': 'H',
    'plug-in hybrid': 'PH',
    'electric': 'E',
    'hydrogen': 'HD'
}

# Function to clean and map fuel type
def clean_fuel_type(ftype):
    # Convert to lowercase, split by comma or slash or space
    parts = [p.strip().lower() for p in str(ftype).replace('/', ',').replace('-', ' ').split(',')]
    short = [fuel_map.get(p, '') for p in parts if p in fuel_map]
    return ' '.join(sorted(set(short)))  # remove duplicates, sort for consistency

# Apply cleaning
df['Fuel Type'] = df['Fuel Type'].apply(clean_fuel_type)

# Save cleaned data
df.to_csv(output_file, index=False)

print(f"✅ Fuel Type standardized and saved to:\n{output_file}")
