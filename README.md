# 🏦 Loan Risk Analyzer – ML Powered Web App

A lightweight Flask-based web application that predicts the **risk of loan default** using a machine learning model. Designed for ease of use and cloud deployment on platforms like **Render**.

---

## 🚀 Live Demo

🟢 Coming soon after deployment to [Render.com](https://render.com)

---

## 📦 Features

- ✅ Web form to input loan applicant details
- ✅ Real-time ML prediction using a trained scikit-learn model
- ✅ Prediction logging with timestamp and input data
- ✅ Responsive and modern UI (VR-style)
- ✅ Ready for cloud deployment using `render.yaml`

---

## 🧾 Project Structure

loan-risk-analyzer/
│
├── app.py # Flask main app
├── requirements.txt # Python dependencies
├── render.yaml # Deployment config for Render
│
├── model/
│ └── loan_model.pkl # Pre-trained ML model
│
├── data/
│ ├── loan_data.csv # Sample data (optional)
│ └── prediction_log.csv # Log of predictions
│
├── utils/
│ └── predict.py # ML prediction helper
│
├── templates/
│ ├── index.html # Main form page
│ └── logs.html # Log viewer page
│
├── static/
│ └── style.css # Custom styling
│
└── notebooks/
└── model_training.ipynb # Notebook for training and saving model


---

## 🛠️ Local Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/<your-username>/loan-risk-analyzer.git
cd loan-risk-analyzer
```

### 2. Create a virtual environment
```bash
Copy
Edit
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
```
### 3. Install dependencies
```bash
Copy
Edit
pip install -r requirements.txt
```
### 4. Run the app locally
```bash
Copy
Edit
python app.py
Open http://localhost:5000 in your browser.
```
---

## 🧠 Model Training
The model is trained using scikit-learn. To retrain or modify the model:

Open notebooks/model_training.ipynb

Modify or retrain as needed

Export the model as loan_model.pkl to the model/ folder

---

## 🤝 Contributing
1) Fork the project & create your branch: git checkout -b feature/awesome.

2) Commit your changes: git commit -m 'Add some awesome'.

3) Push to the branch: git push origin feature/awesome.

4) Open a Pull Request.

## 📜 License
Released under the MIT License – see LICENSE for details.

Built with ❤️ by Bhavesh Kusakiya.
Feel free to reach out on LinkedIn for questions or collaborations!

---
