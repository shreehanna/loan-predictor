# ​ Loan Approval Predictor

A web app that predicts loan approval based on applicant data—think credit history, income, and more.  
Built with **Python**, **scikit-learn**, and deployed using **Streamlit**.

🔗 **[Live Demo](https://loan-predictor-gekudvrz2wucjesdgbapqk.streamlit.app/)**

---

##  Project Overview
This ML app predicts if a loan application will be **Approved** or **Rejected** using features like:
- Employment status
- Income details
- Credit history
- Loan amount

It showcases:
- Data wrangling & feature engineering (numerical + categorical)
- Model training & comparative evaluation
- Real-time deployment via Streamlit

---

##  Models Used
- **Logistic Regression**
- **Random Forest Classifier**
- *(Optionally)* Gradient Boosting (e.g., XGBoost, LightGBM)

Models are compared based on:
- Accuracy
- Precision
- Recall
- F1-score

---

##  Repository Structure
├── app.py # Streamlit interface
├── train_model.py # Model training logic
├── model.py # Encapsulates training & evaluation methods
├── data_loader.py # Data preprocessing
├── loan_model.pkl # Serialized trained model
├── requirements.txt # Dependencies list
└── README.md # Project docs

yaml
Copy
Edit

---

##  Installation (Local Deployment)
Clone and set it up locally:
```bash
git clone https://github.com/shreehanna/loan-approval-predictor.git
cd loan-approval-predictor
pip install -r requirements.txt
Train the model:

bash
Copy
Edit
python train_model.py
Launch the app:

bash
Copy
Edit
streamlit run app.py
Results (Sample — update after training)
Model	Accuracy	Precision	Recall	F1-score
Logistic Regression	0.88	0.85	0.84	0.84
Random Forest	0.91	0.89	0.88	0.88

(Replace values with your real results once training is done)

Future Improvements
Advanced hyperparameter tuning (GridSearchCV / RandomizedSearchCV)

Explainability with SHAP or LIME

Docker containerization for cloud deployment

Optional: NVIDIA Clara integration for fintech data pipelines
