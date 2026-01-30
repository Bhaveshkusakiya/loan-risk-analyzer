import pickle
import pandas as pd

# Load trained model
model = pickle.load(open('model/loan_model.pkl', 'rb'))

# Expected feature order (must match training)
FEATURES = [
    'ApplicantIncome',
    'LoanAmount',
    'Loan_Amount_Term',
    'Credit_History',
    'Gender_Male',
    'Married_Yes',
    'Education_Not Graduate',
    'Self_Employed_Yes',
    'Property_Area_Semiurban',
    'Property_Area_Urban'
]

def predict_loan_risk(input_data: dict):
    """
    input_data: dictionary of user inputs
    """

    df = pd.DataFrame([input_data])
    df = pd.get_dummies(df)

    # Align columns with training
    df = df.reindex(columns=FEATURES, fill_value=0)

    prediction = model.predict(df)[0]
    probability = model.predict_proba(df)[0][1]

    return {
        "loan_approved": bool(prediction),
        "risk_probability": round(probability, 2)
    }
