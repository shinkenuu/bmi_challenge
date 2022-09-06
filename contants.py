from models import BMILabel

BMI_LABELS = (
    BMILabel(
        category="Underweight", range=(float("-inf"), 18.4), risk="Malnutrition risk"
    ),
    BMILabel(category="Normal weight", range=(18.5, 24.9), risk="Low risk"),
    BMILabel(category="Overweight", range=(25.0, 29.9), risk="Enhanced risk"),
    BMILabel(category="Moderately obese", range=(30.0, 34.9), risk="Medium risk"),
    BMILabel(category="Severely obese", range=(35.0, 39.9), risk="High risk"),
    BMILabel(
        category="Very severely obese",
        range=(40.0, float("inf")),
        risk="Very high risk",
    ),
)

BMI_LABEL_RANGES_MAP = {label.range: label for label in BMI_LABELS}
