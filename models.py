from typing import Optional, Tuple

from pydantic import BaseModel, Field


class BMILabel(BaseModel):
    category: str
    range: Tuple[float, float]
    risk: str


class Patient(BaseModel):
    height: float = Field(alias="HeightCm", description="Height in centimeters")
    weight: float = Field(alias="WeightKg", description="Weight in kilograms")
    bmi: Optional[float]
    bmi_label: Optional[BMILabel]

    class Config:
        allow_population_by_field_name = True
