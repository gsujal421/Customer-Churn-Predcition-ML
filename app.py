import streamlit as st
import joblib
import numpy as np

scaler=joblib.load('scaler.pkl')
model=joblib.load('best_model.pkl')

st.title('Customer Churn Prediction')
st.divider()

st.write('This app predicts customer churn using a support vector machine model.')
st.divider()

gender=st.selectbox("Select Gender *", ['Select','Male','Female'])

age=st.number_input('Enter Age *', min_value=10, max_value=100, value=10)

tenure=st.number_input('Enter Tenure *', min_value=0, max_value=125, value=10)

monthly_charges=st.number_input('Enter Monthly Charges *', min_value=0, max_value=10000, value=100)

st.divider()

button=st.button("Predict")

if button:
    if gender=='Select':
        st.error("Please select a gender.")
    else:
        gender_encoded= 1 if gender=='Male' else 0
        X=[gender_encoded,age,tenure,monthly_charges]
        X_arr=np.array([X])
        X_scaler= scaler.transform(X_arr)
        pred=model.predict(X_scaler)[0]
        prediction='Churn' if pred==1 else 'Stay'
        st.write(f"Prediction: {prediction}")
        if prediction=='Churn':
            st.warning("The model predicts that the customer will leave.")
        else:
            st.success("The model predicts that the customer will stay.")
            st.balloons()
else:
    st.write('Please enter the required information.')

st.divider()

st.write("Developed by Sujal Gupta")
st.write("Source Code: [GitHub Repository](https://github.com/gsujal421/Customer-Churn-Prediction-ML.git)")

