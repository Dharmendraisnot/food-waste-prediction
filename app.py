import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

st.title("🍽️ Food Demand Prediction App")

# Load dataset
data = pd.read_csv("accessories.csv")

# Keep only numeric data
data = data.select_dtypes(include=['number'])

# 🔥 VERY IMPORTANT FIX (NaN handling)
data = data.fillna(data.mean())

# Check if still NaN exists
if data.isnull().sum().sum() > 0:
    st.error("Still contains missing values ❌")
    st.stop()

# Split data
X = data.iloc[:, :-1]
y = data.iloc[:, -1]

# Train model
model = LinearRegression()
model.fit(X, y)

st.success("Model trained successfully ✅")