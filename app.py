import pickle
import streamlit as st
import pandas as pd
import numpy as np

# Load saved model, scaler, and encoder
model = pickle.load(open(r"C:\Users\Admin\Downloads\app.py\random_forest_model (1).pkl", "rb"))
scaler = pickle.load(open(r"C:\Users\Admin\Downloads\app.py\scaler.pkl", "rb"))
encoder = pickle.load(open(r"C:\Users\Admin\Downloads\app.py\encoder.pkl", "rb"))

# Streamlit App Title
st.title("Telecom Churn Prediction")
st.write("Enter customer details to predict churn")

# Sidebar for user input
st.sidebar.header('Customer Input Features')

def user_input_features():
    voice_plan = st.sidebar.selectbox("Voice Plan", ["No", "Yes"])
    intl_plan = st.sidebar.selectbox("International Plan", ["No", "Yes"])
    account_length = st.sidebar.slider("Account Length", min_value=0, max_value=250, step=1)
    day_mins = st.sidebar.slider("Day Minutes", min_value=0.0, max_value=350.0, step=0.1)
    day_calls = st.sidebar.slider("Day Calls", min_value=0, max_value=150, step=1)
    day_charge = st.sidebar.slider("Day Charge", min_value=0.0, max_value=60.0, step=0.1)
    eve_mins = st.sidebar.slider("Evening Minutes", min_value=0.0, max_value=350.0, step=0.1)
    eve_calls = st.sidebar.slider("Evening Calls", min_value=0, max_value=150, step=1)
    eve_charge = st.sidebar.slider("Evening Charge", min_value=0.0, max_value=50.0, step=0.1)
    night_mins = st.sidebar.slider("Night Minutes", min_value=0.0, max_value=350.0, step=0.1)
    night_calls = st.sidebar.slider("Night Calls", min_value=0, max_value=50, step=1)
    night_charge = st.sidebar.slider("Night Charge", min_value=0.0, max_value=30.0, step=0.1)
    intl_mins = st.sidebar.slider("International Minutes", min_value=0.0, max_value=20.0, step=0.1)
    intl_calls = st.sidebar.slider("International Calls", min_value=0, max_value=20, step=1)
    intl_charge = st.sidebar.slider("International Charge", min_value=0.0, max_value=10.0, step=0.1)
    customer_calls = st.sidebar.slider("Customer Service Calls", min_value=0, max_value=10, step=1)

    # Create DataFrame
    data = pd.DataFrame({
        "voice.plan": [voice_plan],
        "intl.plan": [intl_plan],
        "account.length": [account_length],
        "day.mins": [day_mins],
        "day.calls": [day_calls],
        "day.charge": [day_charge],
        "eve.mins": [eve_mins],
        "eve.calls": [eve_calls],
        "eve.charge": [eve_charge],
        "night.mins": [night_mins],
        "night.calls": [night_calls],
        "night.charge": [night_charge],
        "intl.mins": [intl_mins],
        "intl.calls": [intl_calls],
        "intl.charge": [intl_charge],
        "customer.calls": [customer_calls]
    })
    return data

# Collect user inputs
df = user_input_features()

# Display user inputs
st.subheader("User Input Parameters")
st.write(df)

# Encode categorical inputs
df["voice.plan"] = df["voice.plan"].str.lower()
df["intl.plan"] = df["intl.plan"].str.lower()
df["voice.plan"] = encoder.transform(df["voice.plan"])
df["intl.plan"] = encoder.transform(df["intl.plan"])

# Ensure missing features are handled
numerical_features = [
    "account.length", "voice.plan", "intl.plan", "day.mins", "day.calls", "day.charge",
    "eve.mins", "eve.calls", "eve.charge", "night.mins", "night.calls", "night.charge",
    "intl.mins", "intl.calls", "intl.charge", "customer.calls"
]
for feature in numerical_features:
    if feature not in df.columns:
        df[feature] = 0

# Scale numerical inputs
df[numerical_features] = scaler.transform(df[numerical_features])

# Prediction
prediction = model.predict(df)
prediction_proba = model.predict_proba(df)

# Display Prediction Result
st.subheader("Prediction Result")
if prediction[0] == 1:
    st.write("**Prediction: Customer Will Churn**")
else:
    st.write("**Prediction: Customer Will Not Churn**")

# Display Probability
st.subheader("Prediction Probabilities")
st.write(f"Probability of Churn: {prediction_proba[0][1]:.2f}")
st.write(f"Probability of Not Churn: {prediction_proba[0][0]:.2f}")
