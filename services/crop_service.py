from pyexpat import features
from schemas.crop_data import CropData
import pickle
import numpy as np

with open("./resources/RFCropv132.pkl",'rb') as file:
    model_rf = pickle.load(file)

with open("./resources/SVMCropv132.pkl",'rb') as file:
    model_svm = pickle.load(file)

labels = ['rice' 'maize' 'chickpea' 'kidneybeans' 'pigeonpeas' 'mothbeans'
 'mungbean' 'blackgram' 'lentil' 'pomegranate' 'banana' 'mango' 'grapes'
 'watermelon' 'muskmelon' 'apple' 'orange' 'papaya' 'coconut' 'cotton'
 'jute' 'coffee']

class PredictionCrop():

    def get_recommendation(data: CropData):

        features = {
            "N": data.nitrogen,
            "P": data.phosphorus,
            "K": data.potassium,
            "temperature": data.temperature,
            "humidity": data.humidity,
            "ph": data.ph,
            "rainfall": data.rainfall
        }

        input_data = np.array(list(features.values())).reshape(1, 7)

        if data.model_prediction == 0:
            prediction = model_rf.predict(input_data)
        else:
            prediction = model_svm.predict(input_data)

        return prediction[0]