import pandas as pd

# Input and output file paths
input_csv_path = r"D:\COURSES\PBEL AI INTERNSHIP\OTHER STUFF\ML DATA SET WITH AUTOAI\Car Price Prediction\dataset optimisation\FINAL STUFF\car_price_prediction_MLoptimisedDataSet.csv"
output_csv_path = r"D:\COURSES\PBEL AI INTERNSHIP\OTHER STUFF\ML DATA SET WITH AUTOAI\Car Price Prediction\dataset optimisation\FINAL STUFF\testfile69.csv"

# Load the CSV file
df = pd.read_csv(input_csv_path)

# Convert all values in 'Company/Brand' column to uppercase
df['Company/Brand'] = df['Company/Brand'].str.upper()

# Save the updated DataFrame to a new CSV
df.to_csv(output_csv_path, index=False)

print("Company/Brand column values converted to uppercase and saved to:", output_csv_path)
