import pytest

from services import label_bmi


@pytest.mark.parametrize(
    "bmi, expected_label_risk, expected_label_category, ",
    (
        [0, "Malnutrition risk", "Underweight"],
        [21.345, "Low risk", "Normal weight"],
        [29.899, "Enhanced risk", "Overweight"],
        [31.230, "Medium risk", "Moderately obese"],
        [35, "High risk", "Severely obese"],
        [3123123123.32, "Very high risk", "Very severely obese"],
    ),
)
def test_label_bmi(
    bmi: float,
    expected_label_risk: str,
    expected_label_category: str,
):
    # ACT
    actual_label = label_bmi(bmi=bmi)

    # ASSERT
    assert actual_label.category == expected_label_category
    assert actual_label.risk == expected_label_risk
