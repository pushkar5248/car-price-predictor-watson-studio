import pandas as pd
import random

# Input file path
input_csv_path = r"D:\COURSES\PBEL AI INTERNSHIP\OTHER STUFF\ML DATA SET WITH AUTOAI\Car Price Prediction\dataset optimisation\FINAL STUFF\car_price_prediction_MLoptimisedDataSet.csv"

# Output file paths
train_csv_path = r"D:\COURSES\PBEL AI INTERNSHIP\OTHER STUFF\ML DATA SET WITH AUTOAI\Car Price Prediction\dataset optimisation\FINAL STUFF\car_price_prediction_training_data.csv"
test_csv_path = r"D:\COURSES\PBEL AI INTERNSHIP\OTHER STUFF\ML DATA SET WITH AUTOAI\Car Price Prediction\dataset optimisation\FINAL STUFF\car_price_prediction_testing_data.csv"

# Read the dataset
df = pd.read_csv(input_csv_path)

# Shuffle the data randomly
df_shuffled = df.sample(frac=1, random_state=42).reset_index(drop=True)

# Split the dataset
train_data = df_shuffled.iloc[:1000]
test_data = df_shuffled.iloc[1000:]  # Remaining 219 rows

# Save to CSV files
train_data.to_csv(train_csv_path, index=False)
test_data.to_csv(test_csv_path, index=False)

print(f"✅ Split completed.\n→ Training data saved to: {train_csv_path}\n→ Testing data saved to: {test_csv_path}")
