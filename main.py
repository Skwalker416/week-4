from fastapi import FastAPI, HTTPException
import joblib
import pandas as pd

app = FastAPI()

# Load the trained model at startup
MODEL_PATH = "model/model.pkl"

@app.on_event("startup")
def load_model():
    global model
    try:
        model = joblib.load(MODEL_PATH)
        print("Model loaded successfully.")
    except Exception as e:
        print(f"Error loading model: {e}")
        raise RuntimeError("Could not load the trained model.")
    
@app.post("/predict/")
def predict(data: dict):
    try:
        # Convert input data to a DataFrame
        input_data = pd.DataFrame([data])
        
        # Ensure all required columns exist
        required_columns = ['CompetitionDistance', 'Feature1', 'Feature2']  # Update as per your model's features
        for col in required_columns:
            if col not in input_data.columns:
                raise HTTPException(status_code=400, detail=f"Missing column: {col}")

        # Make predictions
        prediction = model.predict(input_data)

        # Format the response
        return {"prediction": prediction.tolist()}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
