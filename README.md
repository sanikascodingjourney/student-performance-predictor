# 🎓 Student Exam Score Predictor

A machine learning project that predicts student exam scores based on study habits, attendance, and other behavioral/socioeconomic factors, using Linear Regression.

## 📊 Project Overview

This project analyzes a dataset of 6,600+ student records to identify key factors influencing academic performance and builds a predictive model with an interactive web app for real-time predictions.

## 🔧 Tech Stack

- **Python**
- **Pandas, NumPy** – data cleaning and manipulation
- **Scikit-learn** – model building and evaluation
- **Matplotlib, Seaborn** – data visualization
- **Streamlit** – interactive web app
- **Google Colab** – development environment

## 🚀 Features

- Data cleaning (handled missing values in categorical columns)
- One-hot encoding of categorical features
- Exploratory Data Analysis (EDA)
- Linear Regression model for exam score prediction
- Model evaluation using R² Score and MAE
- Interactive Streamlit web app for live predictions

## 📈 Model Performance

- **R² Score:** 0.77
- **Mean Absolute Error (MAE):** 0.45

## 💡 Key Insights

- Tutoring sessions and hours studied had the strongest positive influence on exam scores
- Lower parental involvement was associated with a noticeable drop in scores

## 🖥️ How to Run Locally

```bash
pip install streamlit scikit-learn pandas
python -m streamlit run app.py
```

## 📁 Files

- `Student_Performance_Predictor.ipynb` – Full data analysis and model building notebook
- `app.py` – Streamlit web application
- `student_model.pkl` – Trained model file

## 🌐 Live Demo

[Add your Streamlit Cloud link here once deployed]

## 📌 Dataset

[Student Performance Factors – Kaggle](https://www.kaggle.com/datasets/lainguyn123/student-performance-factors)
