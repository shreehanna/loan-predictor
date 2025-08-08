# predictor_utils.py

import pandas as pd
import joblib

def load_model(path="model.pkl"):
    """
    Load the trained ML model from the given path.
    """
    return joblib.load(path)

def process_input(input_data: dict) -> pd.DataFrame:
    """
    Convert user input dictionary into a preprocessed DataFrame.
    Must match training-time preprocessing!
    """
    df = pd.DataFrame([input_data])

    # Manual encoding
    gender_map = {'Male': 1, 'Female': 0}
    married_map = {'Yes': 1, 'No': 0}
    education_map = {'Graduate': 1, 'Not Graduate': 0}
    self_employed_map = {'Yes': 1, 'No': 0}
    property_map = {'Urban': 2, 'Semiurban': 1, 'Rural': 0}
    dependents_map = {'0': 0, '1': 1, '2': 2, '3+': 3}

    df['Gender'] = df['Gender'].map(gender_map)
    df['Married'] = df['Married'].map(married_map)
    df['Education'] = df['Education'].map(education_map)
    df['Self_Employed'] = df['Self_Employed'].map(self_employed_map)
    df['Property_Area'] = df['Property_Area'].map(property_map)
    df['Dependents'] = df['Dependents'].map(dependents_map)

    return df

def predict_loan_approval(model, input_data: dict) -> str:
    """
    Predict loan approval status (returns Approved or Rejected emoji string).
    """
    df = process_input(input_data)
    prediction = model.predict(df)[0]
    return '✅ Approved' if prediction == 1 else '❌ Rejected'


