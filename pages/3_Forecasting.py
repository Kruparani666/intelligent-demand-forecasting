import sys, os
sys.path.append(os.path.abspath("src"))

import streamlit as st
import pandas as pd
from forecast import make_forecast

st.title("📈 Forecasting")

periods = st.slider("Forecast Horizon (Days)", 7, 180, 30)

if st.button("Generate Forecast"):

    forecast = make_forecast(periods=periods)

    st.dataframe(forecast.tail())

    csv = forecast.to_csv(index=False).encode("utf-8")

    st.download_button(
        "Download Forecast",
        csv,
        "forecast.csv",
        "text/csv"
    )
