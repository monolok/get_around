from joblib import load
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd

app = FastAPI()

class InputData(BaseModel):
    data: list

@app.post("/predict")
def predict(data: InputData):
    preprocessor = load('./preprocessor.joblib')
    model = load('./model.joblib')
    #user_test = ['Renault', 186382, 120, 'diesel', 'silver', 'estate', 1, 1, 0, 0,0, 0, 1]
    user_test = data.data[0]
    print('######################MSG###########')
    print(user_test)
    features = ['model_key', 'mileage', 'engine_power', 'fuel', 'paint_color', 'car_type', 'private_parking_available', 'has_gps', 'has_air_conditioning', 'automatic_car', 'has_getaround_connect', 'has_speed_regulator', 'winter_tires']
    data = pd.DataFrame([user_test], columns=features)
    transformed_data = preprocessor.transform(data)
    prediction = model.predict(transformed_data)
    return {'prediction': prediction.tolist()}

# curl -X 'POST' \
#   'http://127.0.0.1:8000/predict' \
#   -H 'accept: application/json' \
#   -H 'Content-Type: application/json' \
#   -d '{
#   "data": [["Renault", 186382, 120, "diesel", "silver", "estate", 1, 1, 0, 0, 0, 0, 1]]
# }'