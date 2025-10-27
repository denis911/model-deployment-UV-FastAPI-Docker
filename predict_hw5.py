import pickle
from typing import Literal
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn


class Customer(BaseModel):
    lead_source: Literal["organic_search", "ads", "referral", "social_media"]
    number_of_courses_viewed: int
    annual_income: float


class PredictResponse(BaseModel):
    conversion_probability: float
    convert: bool


app = FastAPI(title="lead-conversion-prediction")

with open("pipeline_v1.bin", "rb") as f:
    model = pickle.load(f)


def predict_single(data):
    return float(model.predict_proba([data])[0, 1])


@app.post("/predict", response_model=PredictResponse)
def predict(customer: Customer):
    prob = predict_single(customer.model_dump())
    return {"conversion_probability": prob, "convert": prob >= 0.5}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9696)
