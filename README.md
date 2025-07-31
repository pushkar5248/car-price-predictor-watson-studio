# car-price-predictor-watson-studio
# 🚗 Car Price Prediction using IBM Watson AutoAI

This project aims to build a machine learning model that predicts car prices based on technical and performance specifications using **IBM Watson AutoAI**. The dataset includes a wide range of cars from different manufacturers with attributes like engine capacity, horsepower, acceleration, fuel type, torque, and more.

---

## 🛠️ Project Workflow

1. **Dataset Preparation**
   - Original CSV file had inconsistent formats (e.g., `Torque`, `Fuel Type`, etc.)
   - Cleaned and optimized using Python scripts (handled missing values, removed symbols like `Nm`, `/`, `+`, etc.)
   - Converted `Fuel_Type` from string codes (`P`, `D`, `H`, etc.) into numeric mappings
   - Final dataset had columns like:
     ```
     Company/Brand, Battery_CC, Battery_kWh, Horsepower (hp), Top Speed (km/h),
     Acceleration, Price ($), Fuel Type, Seats, Torque (Nm)
     ```

2. **Model Training**
   - IBM Watson AutoAI was used to automatically:
     - Analyze dataset
     - Select features
     - Run experiments
     - Build pipelines
     - Evaluate performance
   - Trained on 1000 random rows
   - Tested on remaining ~219 rows

3. **Prediction and Evaluation**
   - Model deployed through AutoAI
   - Predictions extracted from JSON output
   - Evaluation done using:
     - Mean Absolute Error (MAE)
     - Root Mean Squared Error (RMSE)
     - R² Score

---

## 📊 Example Features Used

| Feature         | Type        |
|----------------|-------------|
| Company/Brand  | Categorical |
| Battery_CC     | Numerical   |
| Battery_kWh    | Numerical   |
| Horsepower     | Numerical   |
| Top Speed      | Numerical   |
| Acceleration   | Numerical   |
| Fuel Type      | Categorical (Encoded) |
| Seats          | Numerical   |
| Torque         | Numerical   |

---

## 🔄 Fuel_Type Mapping

| Encoded Value | Meaning           |
|---------------|-------------------|
| 0             | P   (Petrol)      |
| 1             | D   (Diesel)      |
| 2             | H   (Hybrid)      |
| 3             | E   (Electric)    |
| 4             | PH  (Plug-in Hybrid) |
| 5             | HD  (Hydrogen)    |

---

## 🧩 Challenges Faced

- Inconsistent and messy data formats (e.g., `"100 - 140 Nm"`, `"800 Nm"`, `"GT Model"`, etc.)
- Missing values in numerical and categorical columns
- AutoAI model failure due to unsupported imputation on categorical missing values
- Limited CUH (Compute Units Hours) in IBM Watson Studio (only 0.08 left)
- Had to preprocess everything manually to ensure AutoAI could work smoothly

---

## 📂 File Structure

