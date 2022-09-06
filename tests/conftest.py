import pytest

from models import Patient


@pytest.fixture()
def patient():
    patient = Patient(
        height=170.0,
        weight=76,
    )

    return patient
