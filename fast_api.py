from joblib import load
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd

app = FastAPI()

class InputData(BaseModel):
    data: list

@app.post("/predict")
def predict(data: InputData):
    preprocessor = load('/Users/antoinebertin/Documents/jedha/full_stack/projects_full_stack/deploy_ml/preprocessor.joblib')
    model = load('/Users/antoinebertin/Documents/jedha/full_stack/projects_full_stack/deploy_ml/model.joblib')
    transformed_data = preprocessor.transform(pd.DataFrame(data.data))
    prediction = model.predict(transformed_data)
    return {'prediction': prediction.tolist()}

# Index(['model_key', 'mileage', 'engine_power', 'fuel', 'paint_color',
#        'car_type', 'private_parking_available', 'has_gps',
#        'has_air_conditioning', 'automatic_car', 'has_getaround_connect',
#        'has_speed_regulator', 'winter_tires'],
#       dtype='object')