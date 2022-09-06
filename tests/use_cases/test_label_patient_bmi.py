import pytest

from contants import BMI_LABELS
from use_cases import label_patient_bmi


def test_calculates_bmi_when_patients_is_empty(patient):
    assert patient.bmi is None

    # ACT
    label_patient_bmi(patient)

    # ASSERT
    assert patient.bmi is not None


def test_do_not_calculates_bmi_when_patients_is_set(mocker, patient):
    # ARRANGE
    patient.bmi = 10.0
    calculate_bmi_mock = mocker.patch("use_cases.services.calculate_bmi")

    # ACT
    label_patient_bmi(patient)

    # ASSERT
    calculate_bmi_mock.assert_not_called()


@pytest.mark.parametrize(
    "bmi, expected_bmi_label",
    ([bmi_label.range[1] - 1, bmi_label] for bmi_label in BMI_LABELS),
)
def test_labels_patient_with_bmi_label(patient, bmi, expected_bmi_label):
    # ARRANGE
    patient.bmi = bmi

    # ACT
    label_patient_bmi(patient)

    # ASSERT
    assert patient.bmi_label == expected_bmi_label
