# app.py

import streamlit as st
from predictor_utils import load_model, predict_loan_approval

# Load the trained model
model = load_model()

st.set_page_config(page_title="Loan Approval Predictor", page_icon="💰")
st.title("💸 Loan Approval Predictor")
st.markdown("Enter your details below to check if your loan is likely to be **Approved** or **Rejected**.")

# Sidebar with form
with st.form("loan_form"):
    gender = st.selectbox("Gender", ["Male", "Female"])
    married = st.selectbox("Married", ["Yes", "No"])
    dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
    education = st.selectbox("Education", ["Graduate", "Not Graduate"])
    self_employed = st.selectbox("Self Employed", ["No", "Yes"])
    applicant_income = st.number_input("Applicant Income", min_value=0)
    coapplicant_income = st.number_input("Coapplicant Income", min_value=0)
    loan_amount = st.number_input("Loan Amount (in thousands)", min_value=0)
    loan_term = st.number_input("Loan Term (in days)", min_value=0)
    credit_history = st.selectbox("Credit History", ["Yes (1)", "No (0)"])
    property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

    submit_btn = st.form_submit_button("Predict 💥")

# When button clicked
if submit_btn:
    # Map credit history to actual value
    credit_history_val = 1 if credit_history == "Yes (1)" else 0

    user_input = {
        "Gender": gender,
        "Married": married,
        "Dependents": dependents,
        "Education": education,
        "Self_Employed": self_employed,
        "ApplicantIncome": applicant_income,
        "CoapplicantIncome": coapplicant_income,
        "LoanAmount": loan_amount,
        "Loan_Amount_Term": loan_term,
        "Credit_History": credit_history_val,
        "Property_Area": property_area
    }

    result = predict_loan_approval(model, user_input)

    # Show result
    st.markdown("### Result:")
    st.success(result) if "Approved" in result else st.error(result)
