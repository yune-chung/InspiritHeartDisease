import streamlit as st

def get_app_response(prediction):
  if prediction == 1: # CHANGE THIS!
    st.write("It is likely you have heart disease")
  # ADD MORE IF / ELIF STATEMENTS HERE
  else:
    st.write("It is unlikely you have heart disease")
