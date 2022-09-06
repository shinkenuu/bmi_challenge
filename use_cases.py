import services
from models import Patient


def label_patient_bmi(patient: Patient):
    if not patient.bmi:
        patient.bmi = services.calculate_bmi(
            height=patient.height * 0.01,
            weight=patient.weight,
        )

    patient.bmi_label = services.label_bmi(
        bmi=patient.bmi,
    )


def count_patients_in_category(patients: list[Patient], category: str) -> int:
    # sum([1 for patient in patients if patient.bmi_label.category == category])

    counter = 0

    for patient in patients:
        if patient.bmi_label.category == category:
            counter += 1

    return counter
