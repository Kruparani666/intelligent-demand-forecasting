from prophet import Prophet
import joblib

def train_prophet(df):
    model = Prophet()
    model.fit(df)
    joblib.dump(model, "models/prophet_model.pkl")
    return model
