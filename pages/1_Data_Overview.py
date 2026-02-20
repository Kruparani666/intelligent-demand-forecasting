import sys, os
sys.path.append(os.path.abspath("src"))

import streamlit as st
from data_loader import load_data

st.title("📊 Data Overview")

uploaded_file = st.file_uploader("Upload Sales CSV", type=["csv"])

if uploaded_file:
    data = load_data(uploaded_file)

    st.dataframe(data.head())

    col1, col2, col3 = st.columns(3)
    col1.metric("Records", len(data))
    col2.metric("Avg Sales", round(data["sales"].mean(),2))
    col3.metric("Max Sales", round(data["sales"].max(),2))
