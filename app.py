import sys
import os
sys.path.append(os.path.abspath("src"))
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


from data_loader import load_data
from preprocess import prepare_prophet_data
from train_model import train_prophet
from forecast import make_forecast

st.set_page_config(page_title="Demand Forecasting System", layout="wide")

st.title("📦 Intelligent Demand Forecasting System")

# Upload dataset
uploaded_file = st.file_uploader("Upload Sales CSV", type=["csv"])

if uploaded_file:
    data = load_data(uploaded_file)
    st.subheader("Raw Data")
    st.dataframe(data.head())

    df = prepare_prophet_data(data)

    if st.button("Train Model"):
        model = train_prophet(df)
        st.success("Model Trained Successfully!")

    if st.button("Generate Forecast"):
        forecast = make_forecast(periods=30)

        st.subheader("Forecast Results")
        st.dataframe(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail())

        fig = plt.figure()
        plt.plot(forecast['ds'], forecast['yhat'])
        plt.title("Demand Forecast")
        plt.xticks(rotation=45)
        st.pyplot(fig)
