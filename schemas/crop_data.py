from pydantic import BaseModel

class CropData(BaseModel):
    nitrogen: int
    phosphorus: int
    potassium: int
    temperature: float
    humidity: float
    ph: float
    rainfall: float
    model_prediction: int = 0