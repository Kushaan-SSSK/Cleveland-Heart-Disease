
import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load('heart_disease_model.pkl')

st.title("Heart Disease Risk Predictor")
st.markdown("Enter your clinical information to assess heart disease risk.")

age = st.number_input("Age", min_value=20, max_value=100, value=50)
sex = st.selectbox("Sex", ["Female", "Male"])
cp = st.selectbox("Chest Pain Type (cp)", [0, 1, 2, 3])
trestbps = st.number_input("Resting Blood Pressure (mm Hg)", 80, 200, 120)
chol = st.number_input("Serum Cholesterol (mg/dl)", 100, 600, 200)
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", [0, 1])
restecg = st.selectbox("Resting ECG Result", [0, 1, 2])
thalach = st.number_input("Max Heart Rate Achieved", 70, 210, 150)
exang = st.selectbox("Exercise Induced Angina", [0, 1])
oldpeak = st.number_input("ST Depression (oldpeak)", 0.0, 6.0, 1.0)
slope = st.selectbox("Slope of Peak Exercise ST Segment", [0, 1, 2])
ca = st.selectbox("Number of Major Vessels Colored (ca)", [0, 1, 2, 3])
thal = st.selectbox("Thalassemia (thal)", [3, 6, 7])

sex_binary = 1 if sex == "Male" else 0

if st.button("Predict"):
    input_data = np.array([[age, sex_binary, cp, trestbps, chol, fbs, restecg,
                            thalach, exang, oldpeak, slope, ca, thal]])
    prediction = model.predict(input_data)[0]
    
    if prediction > 0:
        st.error("High risk of heart disease detected.")
    else:
        st.success("Low risk of heart disease detected.")
