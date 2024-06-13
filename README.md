# A word on eda.ipynb

The EDA here was mostly used to understand the data and check what features will be the most helpful for me to build the model (`model.ipynb`) that is later saved (joblib) to be used by the Streamlit app via the API deployed. The focus was mostly centered on building a dashboard to answer the following questions:
- Which share of our owner’s revenue would potentially be affected by the feature?
- How many rentals would be affected by the feature depending on the threshold and scope we choose?
```

# Documentation and API Reference

- **API Documentation**: [API DOC](https://get-around.onrender.com/docs)
- **Live APP**: [Dashboard App](https://getaround-c55xfqh3nuxfkd9c9kjf9b.streamlit.app/)

## API Usage

### Predict Endpoint

To make predictions using the API, you can send a POST request with JSON data formatted as follows:

```bash
curl -X 'POST' \
  'https://get-around.onrender.com/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "data": [
      ["Renault", 186382, 120, "diesel", "silver", "estate", 1, 1, 0, 0, 0, 0, 1]
    ]
  }'
```

# Code Repositories

- **API Code**: Check the `api` branch.
- **Frontend App Code**: Check the `main` branch.

# Features

The following features are used in the prediction model:

```python
features = ['model_key', 'mileage', 'engine_power', 'fuel', 'paint_color', 'car_type', 
            'private_parking_available', 'has_gps', 'has_air_conditioning', 'automatic_car', 
            'has_getaround_connect', 'has_speed_regulator', 'winter_tires']
```

## Pydantic Data Validation

The class `InputData(BaseModel)` defines the expected structure of the JSON payload for the `/predict` endpoint as a list:

```python
from pydantic import BaseModel

class InputData(BaseModel):
    data: list
```

This ensures that the API expects JSON data with a `data` key containing a list of input values.

```