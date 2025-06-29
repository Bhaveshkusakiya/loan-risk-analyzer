def classify_risk(income, loan_amount):
    ratio = loan_amount / income
    if ratio < 0.2:
        return "Low Risk"
    elif ratio < 0.4:
        return "Medium Risk"
    else:
        return "High Risk"
