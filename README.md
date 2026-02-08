# Heart Failure Risk Prediction using Machine Learning

##  Project Overview
This project focuses on predicting the risk of death in patients with heart failure using Machine Learning techniques.  
The dataset contains clinical records of patients, including demographic details, medical conditions, and lifestyle factors.  
The goal is to analyze these features and determine whether a patient is at risk of heart failure-related death.


##  Problem Statement
Heart failure is a serious medical condition, and early prediction of risk can help doctors take preventive actions.  
Manual analysis of patient data is time-consuming and error-prone. This project uses machine learning models to automate and improve heart failure risk prediction.



##  Dataset Description
- Total Rows: 299
- Total Columns: 13
- Source: Clinical records of heart failure patients from Kaggle


### Features:
- **Age** – Age of the patient  
- **Sex** – Gender (Male = 1, Female = 0)  
- **Diabetes** – 0 = No, 1 = Yes  
- **Anaemia** – 0 = No, 1 = Yes  
- **High_blood_pressure** – 0 = No, 1 = Yes  
- **Smoking** – 0 = No, 1 = Yes  
- **Cholesterol** – Serum cholesterol level  
- **Blood Pressure** – Systolic/diastolic values  
- **Creatinine Phosphokinase (CPK)** – Enzyme level in blood  
- **Ejection Fraction** – Percentage of blood leaving the heart per contraction  
- **Serum Creatinine** – Kidney health indicator  
- **Time** – Follow-up period (days)


### Target Variable:
- **DEATH_EVENT**
  - 0 = No (Patient survived)
  - 1 = Yes (Patient died)



##  Machine Learning Models Used
The following models were trained and evaluated:

- **K-Nearest Neighbors (KNN)**
- **Logistic Regression**
- **Support Vector Classifier (SVC)**



##  Model Performance Comparison
| Model               | Accuracy |
|--------------------|----------|
| Logistic Regression | **0.80** |
| KNN                | 0.73     |
| SVC                | 0.58     |

✅ **Logistic Regression performed the best and was selected as the final model.**



##  Final Model
- **Selected Model:** Logistic Regression  
- **Reason:** Highest accuracy and better interpretability for medical data  



##  Technologies Used
- Python  
- NumPy  
- Pandas  
- Scikit-learn  
- Jupyter Notebook  
- Matplotlib / Seaborn  
- Git & GitHub  



##  Conclusion
Logistic Regression proved to be the most accurate and reliable model for predicting heart failure risk in this dataset.  
This project demonstrates how machine learning can assist in medical decision-making and early risk detection.



##  Author
**Fatima Shafique**  
Machine Learning & UI/UX Enthusiast 
