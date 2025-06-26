# 📊 AI-ML Internship - Task 3: Linear Regression

# 📘 Task 3: Linear Regression - Internship Project

This project demonstrates the implementation and understanding of **Simple Linear Regression** using a real-world education dataset. The objective is to predict the **Total Number of Schools** based on the **Number of Senior Secondary Schools** in different regions.

---

## 📁 Dataset Information

- **File Name:** `EducationDataset_Preprocessed.csv`
- **Rows:** 16
- **Columns:** 37
- **Contents:** Educational data including number of schools, students, exam results, and encoded district-level features.

---

## 🧰 Tools & Libraries Used

- Python 3.x
- Pandas
- Matplotlib
- Scikit-learn (LinearRegression, Train-Test Split, Evaluation Metrics)

---

## 📌 Objective

> To build a **Simple Linear Regression** model that predicts:
>
> **`no_of_schools_total`** ← based on → **`no_of_schools_sr_sec`**

---

## 📊 Project Steps

1. ✅ Import Required Libraries  
2. ✅ Load and Explore the Dataset  
3. ✅ Select Features and Target Variable  
4. ✅ Split the Data into Train and Test Sets  
5. ✅ Train the Linear Regression Model  
6. ✅ Make Predictions on Test Data  
7. ✅ Evaluate the Model with MAE, MSE, and R²  
8. ✅ Plot the Regression Line  
9. ✅ Print Model Coefficient and Intercept  

---

## 📉 Model Evaluation

| Metric                         | Value (Example) |
|-------------------------------|-----------------|
Mean Absolute Error (MAE):    0.014743467219633363
Mean Squared Error (MSE):      0.0004191001643213589
R² Score:          0.9936673351188164

---

## 📈 Visualization

The scatter plot shows:
- 🔴 Actual test values (data points)
- 🔵 Regression line (predicted values)

You can find the plot image or generate it by running the code.

---

## 🧮 Model Equation

The linear regression model predicts:

y = (slope) * x + intercept


Where:
- `slope` = `model.coef_`
- `intercept` = `model.intercept_`

---

## 📂 Project Structure

📦 LinearRegression_Education
├── EducationDataset_Preprocessed.csv
├── Task3AI-ML3.py
└── README.md


---

## 🔐 Author & Internship Info

- 👨‍💻 **Name:** Subrav  
- 📅 **Date:** June 2025  
- 🏢 **Internship:** AI-ML Internship Task 3 - Linear Regression  
- 🎯 **Status:** ✅ Completed & Submission Ready

---

## ✅ Future Enhancements

- Implement **Multiple Linear Regression** using more features
- Add **Exploratory Data Analysis (EDA)** with Seaborn/Plotly
- Save the model using `joblib` for deployment
- Create an interactive dashboard using Streamlit

---

## 📌 How to Run

1. Clone or download this repository.
2. Make sure you have the required libraries installed:
   ```bash
   pip install pandas matplotlib scikit-learn


