import pytest

from services import calculate_bmi


@pytest.mark.parametrize(
    "height, weight, expected_bmi",
    ([1.75, 75.0, 24.49],),
)
def test_calculate_bmi_results(height: float, weight: float, expected_bmi: float):
    # ACT
    actual_bmi = calculate_bmi(height=height, weight=weight)

    # ASSERT
    assert actual_bmi == pytest.approx(expected_bmi, 0.001)


@pytest.mark.parametrize(
    "height, weight",
    (
        [-123.2, 3.1],
        [123.65, -3.4],
        [123.65, None],
        [None, 34.9],
    ),
)
def test_calculate_bmi_raises_value_error(height: float, weight: float):
    # ACT / ASSERT
    with pytest.raises(ValueError):
        calculate_bmi(height=height, weight=weight)
