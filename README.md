# Customer-Churn-Predcition-ML

An end-to-end Machine Learning + Streamlit App project to analyze customer behavior and predict churn. The project demonstrates the complete workflow of data preprocessing, model training, and deployment with Docker.

⚠️ Disclaimer: Predictions are for demonstration purposes only and not intended for real-world decision-making.
---

## Project Overview

🛠️ Built a machine learning pipeline to predict whether a customer is likely to churn.

🔍 Includes data preprocessing, feature engineering, model selection, and hyperparameter tuning.

🎛️ Developed an interactive Streamlit web app for predictions.      

📦 Containerized with Docker for easy deployment and reproducibility.

---

## Tech Stack

| Category      | Tools/Frameworks            |
| ------------- | --------------------------- |
| Language      | Python 3.13                 |
| ML Libraries  | Scikit-learn, Pandas, NumPy |
| Visualization | Matplotlib, Seaborn         |
| UI/Deployment | Streamlit, Docker           |
---

## Repository Structure
tree /F > structure.txt

customer-churn-prediction/
│── LICENSE
│── README.md
│── project-root/
│   ├── requirements.txt
│   └── Dockerfile
│
├── data/
│   └── customer_churn_data.csv
│
├── models/
│   ├── best_model.pkl
│   └── scaler.pkl
│
├── notebooks/
│   └── notebook.ipynb
│
└── src/
    └── app.py              # Streamlit app
    
---

## Run with Docker
Build the Docker image
docker build -t churn-app .
Run the container
docker run -p 8501:8501 churn-app

Open in browser: http://localhost:8501

---

## Results & Limitations

✅ The model achieved reasonable performance on the given dataset.
⚠️ Predictions are not fully reliable due to dataset limitations.

## Next Steps for Improvement:

Feature engineering with domain insights.

Expanding dataset (more balanced, diverse).

Trying advanced models (XGBoost, LightGBM).

---
## Learning Outcomes

Built an end-to-end ML pipeline.

Created a Streamlit UI for interactive predictions.

Learned Docker containerization for ML apps.

---
