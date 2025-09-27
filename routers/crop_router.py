from fastapi import APIRouter
from schemas.crop_data import CropData
from services.crop_service import PredictionCrop
from utils.config import settings

router = APIRouter(
    prefix=settings.path_router,
)

@router.post("/crop/predict")
async def crop_predict(data: CropData):

    prediction = PredictionCrop.get_recommendation(data)

    return {"prediction": prediction}