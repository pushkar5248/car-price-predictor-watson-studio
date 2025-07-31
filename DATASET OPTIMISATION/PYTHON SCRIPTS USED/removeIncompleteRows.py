import pandas as pd
import os

def remove_incomplete_rows():
    try:
        # Input CSV path
        input_csv_path = r"D:\COURSES\PBEL AI INTERNSHIP\OTHER STUFF\ML DATA SET WITH AUTOAI\Car Price Prediction\CarPricePredictionModelTrainingDatasetMLoptimisedFinal.csv"

        # Output CSV path
        output_csv_path = r"D:\COURSES\PBEL AI INTERNSHIP\OTHER STUFF\ML DATA SET WITH AUTOAI\Car Price Prediction\CarPricePredictionModelTrainingDatasetMLoptimisedFinal_complete_rows_only.csv"

        # Read the CSV file
        df = pd.read_csv(input_csv_path)

        # Drop rows that have ANY missing value
        cleaned_df = df.dropna(how='any')

        # Save the cleaned CSV
        cleaned_df.to_csv(output_csv_path, index=False)
        print(f"✅ Cleaned CSV saved as: {output_csv_path}")

    except Exception as e:
        print(f"❌ Error: {e}")

# Run the function
if __name__ == "__main__":
    remove_incomplete_rows()
