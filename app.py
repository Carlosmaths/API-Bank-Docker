import pandas as pd
import joblib
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# 1. Load the Trained Model
model_filename = "bank_pipeline.pkl"

try:
    model = joblib.load(model_filename)
    print(f"--> SUCCESS! Model '{model_filename}' loaded successfully.")
except FileNotFoundError:
    print(f"--> CRITICAL ERROR: File '{model_filename}' not found.")
    print("    Ensure the .pkl file is in the same directory as app.py")

# 2. Initialize the API Application
app = FastAPI(title="Bank Marketing Prediction API", version="1.0")


# 3. Define Data Model (Input Validation)
# We keep field names identical to the training dataset (e.g., 'age', 'job')
# so the model can recognize them.
class ClientData(BaseModel):
    age: int
    duration: int
    campaign: int
    pdays: int
    previous: int
    job: str
    marital: str
    education: str
    default: str
    housing: str
    loan: str
    contact: str
    month: str
    day_of_week: str
    poutcome: str


# 4. Prediction Endpoint
@app.post("/predict")
def predict(data: ClientData):
    try:
        # Convert input data to a Pandas DataFrame
        input_df = pd.DataFrame([data.dict()])

        # Make prediction
        # [0] is used to get the first element of the array
        prediction = model.predict(input_df)[0]

        # Get probability (confidence score)
        probability = model.predict_proba(input_df)[0].tolist()

        # Return response in JSON format
        return {
            "prediction": int(prediction),
            "outcome": "SUBSCRIBED" if prediction == 1 else "NOT_SUBSCRIBED",
            "confidence_score": probability
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 5. Health Check Endpoint
@app.get("/")
def home():
    return {"message": "Bank Marketing AI API is ONLINE"}