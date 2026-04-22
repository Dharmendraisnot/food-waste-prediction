import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

st.set_page_config(page_title="Food Demand ML System", layout="centered")

st.title("📊 Food Demand Prediction (ML + Test Evaluation)")
st.write("Train model + evaluate using test data + predict new values")

# ==============================
# LOAD TRAIN DATA
# ==============================
train_data = pd.read_csv("train.csv")

# Keep only numeric columns
train_data = train_data.select_dtypes(include=['number'])

# Handle missing values
train_data = train_data.fillna(train_data.mean())

# Split train data
X_train = train_data.iloc[:, :-1]
y_train = train_data.iloc[:, -1]

# ==============================
# TRAIN MODEL
# ==============================
model = LinearRegression()
model.fit(X_train, y_train)

st.success("Model trained successfully ✅")

# ==============================
# LOAD TEST DATA
# ==============================
try:
    test_data = pd.read_csv("test.csv")

    test_data = test_data.select_dtypes(include=['number'])
    test_data = test_data.fillna(test_data.mean())

    # Make sure same columns
    X_test = test_data[X_train.columns]

    # Predict on test data
    test_predictions = model.predict(X_test)

    st.subheader("📊 Test Data Predictions")
    st.write(test_predictions[:10])

except:
    st.warning("Test file not found or format mismatch ⚠️")

# ==============================
# SELECT IMPORTANT FEATURES ONLY
# ==============================

X_train = train_data[['week', 'checkout_price', 'base_price']]
y_train = train_data['num_orders']

# Train model
model.fit(X_train, y_train)

st.subheader("🔮 Enter Details")

week = st.number_input("Week", value=50)
checkout_price = st.number_input("Checkout Price", value=100)
base_price = st.number_input("Base Price", value=120)

# Prediction
if st.button("Predict"):
    prediction = model.predict([[week, checkout_price, base_price]])
    st.success(f"Predicted Orders: {prediction[0]:.2f}")

