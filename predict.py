import joblib
import pandas as pd

# Load model
model = joblib.load("fraud_model.pkl")
feature_names = joblib.load("feature_names.pkl")

print("Enter values for the following features:\n")

values = []

for feature in feature_names:
    value = float(input(f"{feature}: "))
    values.append(value)

sample = pd.DataFrame([values], columns=feature_names)

prediction = model.predict(sample)

if prediction[0] == 0:
    print("\n✅ Legitimate Transaction")
else:
    print("\n🚨 Fraudulent Transaction")