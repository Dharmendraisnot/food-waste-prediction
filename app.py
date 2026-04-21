import streamlit as st
st.markdown("### Smart Food Planning System for Local Vendors")

st.set_page_config(page_title="Food Demand Predictor", layout="centered")

st.title("🍽️ Street Food Demand Prediction System")
st.write("Predict how many items to prepare to reduce food waste")

# Select item
item = st.selectbox("Select Item", ["Samosa", "Kachori", "Pakoda", "Sweets"])

# Inputs
customers = st.number_input("Expected Customers", value=100)
weather = st.selectbox("Weather", ["Normal", "Rainy", "Hot"])
weekend = st.selectbox("Is it Weekend?", ["No", "Yes"])

# Base demand factor
base_factor = 1.2

# Adjust based on item
if item == "Samosa":
    base_factor = 1.3
elif item == "Kachori":
    base_factor = 1.1
elif item == "Pakoda":
    base_factor = 3
elif item == "Sweets":
    base_factor = 1.0

# Weather impact
if weather == "Rainy":
    base_factor += 0.3
elif weather == "Hot":
    base_factor -= 0.2

# Weekend impact
if weekend == "Yes":
    base_factor += 0.5

# Prediction
if st.button("Predict Food Quantity"):
    prediction = int(customers * base_factor)

    st.success(f"👉 Prepare approximately {prediction} {item.lower()}s")

    # Extra insight
    if weather == "Rainy":
        st.info("🌧️ Rain increases demand (especially pakoda)")
    if weekend == "Yes":
        st.info("🎉 Weekend increases customer flow")
