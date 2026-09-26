import streamlit as st
import pickle
import pandas as pd

# Load the saved model
with open('student_model.pkl', 'rb') as file:
    model = pickle.load(file)

st.title("Student Exam Score Predictor")
st.write("Enter student details to predict the exam score")

# Numeric inputs
hours_studied = st.slider("Hours Studied per week", 0, 40, 10)
attendance = st.slider("Attendance (%)", 0, 100, 75)
sleep_hours = st.slider("Sleep Hours per day", 0, 12, 7)
previous_scores = st.slider("Previous Scores", 0, 100, 70)
tutoring_sessions = st.slider("Tutoring Sessions per month", 0, 10, 2)
physical_activity = st.slider("Physical Activity Hours per week", 0, 10, 3)

# Categorical inputs
parental_involvement = st.selectbox("Parental Involvement", ["Low", "Medium", "High"])
access_to_resources = st.selectbox("Access to Resources", ["Low", "Medium", "High"])
extracurricular = st.selectbox("Extracurricular Activities", ["Yes", "No"])
motivation_level = st.selectbox("Motivation Level", ["Low", "Medium", "High"])
internet_access = st.selectbox("Internet Access", ["Yes", "No"])
family_income = st.selectbox("Family Income", ["Low", "Medium", "High"])
teacher_quality = st.selectbox("Teacher Quality", ["Low", "Medium", "High"])
school_type = st.selectbox("School Type", ["Public", "Private"])
peer_influence = st.selectbox("Peer Influence", ["Positive", "Neutral", "Negative"])
learning_disabilities = st.selectbox("Learning Disabilities", ["Yes", "No"])
parental_education = st.selectbox("Parental Education Level", ["High School", "College", "Postgraduate"])
distance_from_home = st.selectbox("Distance from Home", ["Near", "Moderate", "Far"])
gender = st.selectbox("Gender", ["Male", "Female"])

if st.button("Predict Exam Score"):
    # Build a dictionary with all raw inputs
    input_dict = {
        'Hours_Studied': hours_studied,
        'Attendance': attendance,
        'Sleep_Hours': sleep_hours,
        'Previous_Scores': previous_scores,
        'Tutoring_Sessions': tutoring_sessions,
        'Physical_Activity': physical_activity,
        'Parental_Involvement': parental_involvement,
        'Access_to_Resources': access_to_resources,
        'Extracurricular_Activities': extracurricular,
        'Motivation_Level': motivation_level,
        'Internet_Access': internet_access,
        'Family_Income': family_income,
        'Teacher_Quality': teacher_quality,
        'School_Type': school_type,
        'Peer_Influence': peer_influence,
        'Learning_Disabilities': learning_disabilities,
        'Parental_Education_Level': parental_education,
        'Distance_from_Home': distance_from_home,
        'Gender': gender
    }

    input_df = pd.DataFrame([input_dict])

    # One-hot encode same way as training
    input_encoded = pd.get_dummies(input_df)

    # Align columns with training data (fill missing columns with 0)
    model_columns = model.feature_names_in_
    input_final = input_encoded.reindex(columns=model_columns, fill_value=0)

    # Predict
    prediction = model.predict(input_final)[0]

    st.success(f"Predicted Exam Score: {prediction:.2f}")
