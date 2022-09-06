import json


def load_patients(file_path: str = None):
    file_path = file_path or "./patients.json"

    with open(file_path) as file:
        return json.load(file)


def load_bmi_labels(file_path: str = None):
    file_path = file_path or "./bmi_labels.json"

    with open(file_path) as file:
        return json.load(file)


def dump_patients(patients_json: list[dict], file_path: str = None):
    file_path = file_path or "./_patients.json"

    with open(file_path, "w") as file:
        return json.dump(patients_json, file)
