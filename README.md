Project Overview
This project focuses on predicting the presence of heart disease in patients using the UCI Heart Disease dataset. We explore multiple machine learning models including Linear Regression, Random Forest, and XGBoost to build classifiers that predict heart disease risk based on clinical features.

Dataset
Source: UCI Heart Disease Dataset

Description: Contains patient data with attributes such as age, sex, chest pain type, blood pressure, cholesterol, and more.

Target Variable: num — indicating presence (1) or absence (0) of heart disease.

Features Used
Feature	Description
age	Age in years
sex	Sex (1 = male; 0 = female)
cp	Chest pain type (0–3)
trestbps	Resting blood pressure (mm Hg)
chol	Serum cholesterol (mg/dl)
fbs	Fasting blood sugar > 120 mg/dl (1 = true; 0 = false)
restecg	Resting ECG results (values 0,1,2)
thalach	Maximum heart rate achieved
exang	Exercise induced angina (1 = yes; 0 = no)
oldpeak	ST depression induced by exercise relative to rest
slope	Slope of the peak exercise ST segment
ca	Number of major vessels colored by fluoroscopy (0–3)
thal	Thalassemia (3 = normal; 6 = fixed defect; 7 = reversible defect)

Models Implemented
Linear Regression — baseline regression model

Random Forest Regressor — ensemble method using decision trees

XGBoost Classifier — gradient boosting classifier with superior performance

Results
XGBoost achieved the highest accuracy of approximately XX% (replace with your actual result).

Confusion matrix, ROC curve, and feature importance plots are included in the notebook for detailed evaluation.
