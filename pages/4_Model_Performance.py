import sys, os
sys.path.append(os.path.abspath("src"))

import streamlit as st
from sklearn.metrics import mean_absolute_error
from forecast import make_forecast
from data_loader import load_data
from preprocess import prepare_prophet_data

st.title("📉 Model Performance")

uploaded_file = st.file_uploader("Upload Sales CSV", type=["csv"])

if uploaded_file:

    data = load_data(uploaded_file)
    df = prepare_prophet_data(data)

    forecast = make_forecast(periods=0)

    actual = df["y"]
    predicted = forecast["yhat"][:len(actual)]

    mae = mean_absolute_error(actual, predicted)

    st.metric("Mean Absolute Error (MAE)", round(mae,2))
