import streamlit as st

def get_user_input():
  blood_pressure = st.number_input("Enter your blood pressure here")
  heart_rate = st.number_input("Enter your heart rate")
  age = st.number_input("Enter your age")
  exercise_pain = st.number_input("Enter 1 if you have exercise pain and 0 if you dont")
  chest_pain = st.number_input("Enter 1 if you have chest pain and 0 if you dont")
  high_blood_sugar = st.number_input("Enter 1 if you have over 100 and 0 if it is under 100")
  input_features = [[blood_pressure, heart_rate, age, exercise_pain, chest_pain, high_blood_sugar]] # put your features in here!
  return input_features
