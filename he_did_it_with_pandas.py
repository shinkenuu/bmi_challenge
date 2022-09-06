import numpy as np
import pandas as pd

from repositories import load_bmi_labels, load_patients

# Load Patients
patients = load_patients()
patients = pd.DataFrame(patients).drop("Gender", axis=1)

# Calculate BMI
patients["BMI"] = patients.apply(
    lambda patient: patient["WeightKg"] / (patient["HeightCm"] * 0.01) ** 2, axis=1
)

# Load BMI Labels
bmi_labels = load_bmi_labels()
bmi_labels = pd.DataFrame(bmi_labels)

# Label patients BMI category
patients["Category"] = patients["BMI"].apply(
    lambda bmi: bmi_labels[
        (bmi_labels["BMI Range Min"] <= bmi) & (bmi_labels["BMI Range Max"] >= bmi)
    ]["BMI Category"].values[0]
)

# Count overweight patients
overweight_count = np.sum(patients["Category"] == "Overweight")
print("Overweight patients: ", overweight_count)

patients.to_csv("./labeled_patients.csv")
