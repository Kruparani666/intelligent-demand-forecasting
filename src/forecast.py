import joblib
import os

MODEL_PATH = os.path.join("models", "prophet_model.pkl")

def make_forecast(periods=30):
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError("Model not trained yet. Please train first.")

    model = joblib.load(MODEL_PATH)
    future = model.make_future_dataframe(periods=periods)
    forecast = model.predict(future)
    return forecast
