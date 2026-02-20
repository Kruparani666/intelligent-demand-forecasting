import sys, os
sys.path.append(os.path.abspath("src"))

import streamlit as st
from data_loader import load_data
from preprocess import prepare_prophet_data
from train_model import train_prophet

st.title("🚀 Model Training")

uploaded_file = st.file_uploader("Upload Sales CSV", type=["csv"])

if uploaded_file:
    data = load_data(uploaded_file)
    df = prepare_prophet_data(data)

    if st.button("Train Prophet Model"):
        train_prophet(df)
        st.success("Model trained and saved successfully.")
