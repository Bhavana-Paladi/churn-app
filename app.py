import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load trained model and scaler
try:
    model = pickle.load(open('rf_model.pkl', 'rb'))
    # Uncomment if you used a scaler during training
    scaler = pickle.load(open('scaler.pkl', 'rb'))  
except FileNotFoundError:
    st.error("Model or scaler file not found. Ensure the files are in the correct directory.")

st.title("Churn Prediction App")

# UI inputs (match these to your dataset features)
age = st.slider("Age", 18, 100, 30)
gender = st.selectbox("Gender", ['Male', 'Female'])
tenure = st.slider("Tenure", 0, 72, 12)
usage_freq = st.slider("Usage Frequency", 0, 100, 20)
support_calls = st.slider("Support Calls", 0, 30, 2)
payment_delay = st.slider("Payment Delay (days)", 0, 60, 5)
subscription_type = st.selectbox("Subscription Type", ['Basic', 'Standard', 'Premium'])
contract_length = st.selectbox("Contract Length", ['Monthly', 'Quarterly', 'Annual'])
total_spend = st.number_input("Total Spend", min_value=0.0, step=10.0)
last_interaction = st.slider("Last Interaction (days ago)", 0, 365, 30)

# Encode values like you did in training
gender = 1 if gender == 'Male' else 0
subscription_map = {'Basic': 0, 'Standard': 1, 'Premium': 2}
subscription_type = subscription_map[subscription_type]
contract_length_map = {'Monthly': 0, 'Quarterly': 1, 'Annual': 2}
contract_length = contract_length_map[contract_length]

# Create a DataFrame for prediction
input_df = pd.DataFrame([[age, gender, tenure, usage_freq, support_calls, payment_delay,
                          subscription_type, contract_length, total_spend, last_interaction]],
                        columns=['Age', 'Gender', 'Tenure', 'Usage Frequency', 'Support Calls',
                                 'Payment Delay', 'Subscription Type', 'Contract Length',
                                 'Total Spend', 'Last Interaction'])

# Scale if necessary
if 'scaler' in locals():  # Only scale if the scaler was loaded
    input_df = scaler.transform(input_df)

# Predict
pred = model.predict(input_df)[0]
prob = model.predict_proba(input_df)[0][1]

st.subheader("Prediction Result:")
if pred == 1:
    st.error(f"⚠️ Customer likely to churn (probability: {prob:.2f})")
else:
    st.success(f"✅ Customer likely to stay (probability: {prob:.2f})")
