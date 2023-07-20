import streamlit as st



st.title("Registration form.....")

with st.form("Registration form"):
    name = st.text_input("Enter your name")
    email = st.text_input("enter you email")
    password = st.text_input("enter your password",type="password")
    gender = st.radio("Select your gender",("male","female"))
    age = st.slider("enter you age",min_value=18,max_value=50)
    country = st.selectbox("Country",["India","China","USA","UK"])
    st.write(age)

    submit = st.form_submit_button("Register with us...")