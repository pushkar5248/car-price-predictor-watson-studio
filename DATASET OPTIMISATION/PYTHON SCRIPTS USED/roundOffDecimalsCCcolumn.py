import pandas as pd

# Updated file paths
input_csv = r"D:\COURSES\PBEL AI INTERNSHIP\OTHER STUFF\ML DATA SET WITH AUTOAI\Car Price Prediction\dataset optimisation\fillIncompleteRows1.csv"
output_csv = r"D:\COURSES\PBEL AI INTERNSHIP\OTHER STUFF\ML DATA SET WITH AUTOAI\Car Price Prediction\dataset optimisation\testfile3.csv"

try:
    # Load CSV
    df = pd.read_csv(input_csv)

    # Round float values in 'CC' column to nearest integer
    if 'CC' in df.columns:
        df['CC'] = pd.to_numeric(df['CC'], errors='coerce')  # Convert to numeric (NaN if not possible)
        df['CC'] = df['CC'].apply(lambda x: round(x) if pd.notnull(x) else x)

    # Save updated DataFrame
    df.to_csv(output_csv, index=False)
    print(f"✅ 'CC' values rounded and saved to: {output_csv}")

except Exception as e:
    print(f"❌ Error: {e}")
