from flask import Flask, render_template, request
import pickle
import numpy as np
import csv
import os
from datetime import datetime
import pandas as pd

app = Flask(__name__)

# Load the trained model
model = pickle.load(open('model/loan_model.pkl', 'rb'))

# Load model accuracy from text file (optional)
try:
    with open('model/accuracy.txt') as f:
        model_accuracy = f.read()
except:
    model_accuracy = "N/A"

# Function to classify risk based on loan-to-income ratio
def classify_risk(income, loan_amount):
    ratio = loan_amount / income
    if ratio < 0.2:
        return "Low Risk"
    elif ratio < 0.4:
        return "Medium Risk"
    else:
        return "High Risk"

# Function to log prediction to CSV
def log_prediction(input_data, prediction, risk):
    log_file = 'data/prediction_log.csv'
    os.makedirs('data', exist_ok=True)
    file_exists = os.path.isfile(log_file)

    with open(log_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(['Timestamp'] + list(input_data.keys()) + ['Prediction', 'Risk'])
        clean_values = [str(v) for v in input_data.values()]
        row = [datetime.now()] + clean_values + [str(prediction), risk]
        writer.writerow(row)

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    risk = None
    proba = None

    if request.method == 'POST':
        try:
            # STEP 1: Collect form data
            income = float(request.form['income'])
            loan = float(request.form['loan'])
            loan_term = float(request.form['loan_term'])
            credit_history = float(request.form['credit_history'])

            gender = request.form['gender']
            married = request.form['married']
            dependents = request.form['dependents']
            education = request.form['education']
            self_employed = request.form['self_employed']
            property_area = request.form['property_area']

            # STEP 2: Encode form inputs into input_data dict
            input_data = {
                'ApplicantIncome': income,
                'LoanAmount': loan,
                'Loan_Amount_Term': loan_term,
                'Credit_History': credit_history,
                'Gender_Male': 1 if gender == 'Male' else 0,
                'Married_Yes': 1 if married == 'Yes' else 0,
                'Dependents_1': 1 if dependents == '1' else 0,
                'Dependents_2': 1 if dependents == '2' else 0,
                'Dependents_3+': 1 if dependents == '3+' else 0,
                'Education_Not Graduate': 1 if education == 'Not Graduate' else 0,
                'Self_Employed_Yes': 1 if self_employed == 'Yes' else 0,
                'Property_Area_Semiurban': 1 if property_area == 'Semiurban' else 0,
                'Property_Area_Urban': 1 if property_area == 'Urban' else 0,
            }

            # STEP 3: Match input order with model feature names
            final_input = [input_data.get(col, 0) for col in model.feature_names_in_]

            # STEP 4: Prediction and probability
            prediction = model.predict([final_input])[0]
            proba = model.predict_proba([final_input])[0][1]
            risk = classify_risk(income, loan)

            # STEP 5: Save to log
            log_prediction(input_data, prediction, risk)

        except Exception as e:
            prediction = False
            risk = f"Error: {e}"

    return render_template(
        'index.html',
        prediction=prediction,
        risk=risk,
        proba=proba,
        accuracy=model_accuracy
    )

@app.route('/logs')
def logs():
    try:
        df = pd.read_csv('data/prediction_log.csv')
        return render_template('logs.html', tables=[df.to_html(classes='data')])
    except Exception as e:
        return f"No logs found. Error: {e}"

if __name__ == '__main__':
    app.run(debug=True)
