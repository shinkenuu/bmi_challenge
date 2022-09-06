from typing import Optional

from contants import BMI_LABEL_RANGES_MAP
from models import BMILabel


def label_bmi(bmi: float) -> Optional[BMILabel]:
    if bmi is None or bmi < 0:
        raise ValueError("BMI must be zero or a positive float")

    for min_bmi, max_bmi in BMI_LABEL_RANGES_MAP.keys():
        if min_bmi <= bmi <= max_bmi:
            bmi_range = (min_bmi, max_bmi)
            bmi_label = BMI_LABEL_RANGES_MAP[bmi_range]
            return bmi_label


def calculate_bmi(height: float, weight: float) -> float:
    """
    Calculates Body Mass Index
    :param height: in meters
    :param weight: in kilograms
    :return: BMI
    """
    if not height or height < 0:
        raise ValueError("height must be zero or a positive float")

    if weight is None or weight <= 0:
        raise ValueError("weight must be a positive float")

    bmi = weight / (height * height)
    return bmi
