import sys

import models
import repositories
import use_cases


def calculate_overweight_patients(file_path: str = None):
    patient_dicts = repositories.load_patients(file_path=file_path)
    patients = [models.Patient(**patient_dict) for patient_dict in patient_dicts]

    for patient in patients:
        use_cases.label_patient_bmi(patient)

    total_overweight_patients = use_cases.count_patients_in_category(
        patients=patients,
        category="Overweight",
    )

    print("Total overweight patients: ", total_overweight_patients)
    repositories.dump_patients([p.dict() for p in patients])


if __name__ == "__main__":
    file_path = sys.argv[1] if len(sys.argv) > 1 else None
    calculate_overweight_patients(file_path=file_path)
