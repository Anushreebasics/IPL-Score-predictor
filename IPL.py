import streamlit as st
import pandas as pd
import pickle
import joblib
import numpy as np

def load_model():
    model = joblib.load("first-innings-score-lr-model.joblib")
    return model





def main():
    st.title("IPL Score Predictor")

    batteam = st.selectbox('-----Select batting team-----',['Kolkata Knight Riders', 'Chennai Super Kings', 'Rajasthan Royals',
       'Mumbai Indians', 'Kings XI Punjab',
       'Royal Challengers Bangalore', 'Delhi Daredevils', 'Sunrisers Hyderabad'])
    
    bowlteam = st.selectbox('-----Select bowling team-----',['Kolkata Knight Riders', 'Chennai Super Kings', 'Rajasthan Royals',
       'Mumbai Indians', 'Kings XI Punjab',
       'Royal Challengers Bangalore', 'Delhi Daredevils', 'Sunrisers Hyderabad'])
    
    overs = st.text_input("Overs (>= 5.0)")

    runs = st.text_input("Runs scored")

    wickets = st.text_input("Wickets")

    previous_runs = st.text_input("Runs scored in previous 5 overs")

    previous_wickets = st.text_input("Wickets taken in previous 5 overs")

    model = load_model()

    if st.button('Predict'):
        temp_array = list()
            
        if batteam == 'Chennai Super Kings':
            temp_array = temp_array + [1,0,0,0,0,0,0,0]
        elif batteam == 'Delhi Daredevils':
            temp_array = temp_array + [0,1,0,0,0,0,0,0]
        elif batteam == 'Kings XI Punjab':
            temp_array = temp_array + [0,0,1,0,0,0,0,0]
        elif batteam == 'Kolkata Knight Riders':
            temp_array = temp_array + [0,0,0,1,0,0,0,0]
        elif batteam == 'Mumbai Indians':
            temp_array = temp_array + [0,0,0,0,1,0,0,0]
        elif batteam == 'Rajasthan Royals':
            temp_array = temp_array + [0,0,0,0,0,1,0,0]
        elif batteam == 'Royal Challengers Bangalore':
            temp_array = temp_array + [0,0,0,0,0,0,1,0]
        elif batteam == 'Sunrisers Hyderabad':
            temp_array = temp_array + [0,0,0,0,0,0,0,1]
                
                
            
        if bowlteam == 'Chennai Super Kings':
            temp_array = temp_array + [1,0,0,0,0,0,0,0]
        elif bowlteam == 'Delhi Daredevils':
            temp_array = temp_array + [0,1,0,0,0,0,0,0]
        elif bowlteam == 'Kings XI Punjab':
            temp_array = temp_array + [0,0,1,0,0,0,0,0]
        elif bowlteam == 'Kolkata Knight Riders':
            temp_array = temp_array + [0,0,0,1,0,0,0,0]
        elif bowlteam == 'Mumbai Indians':
            temp_array = temp_array + [0,0,0,0,1,0,0,0]
        elif bowlteam == 'Rajasthan Royals':
            temp_array = temp_array + [0,0,0,0,0,1,0,0]
        elif bowlteam == 'Royal Challengers Bangalore':
            temp_array = temp_array + [0,0,0,0,0,0,1,0]
        elif bowlteam == 'Sunrisers Hyderabad':
            temp_array = temp_array + [0,0,0,0,0,0,0,1]

        temp_array = temp_array + [float(overs), int(runs), int(wickets), int(previous_runs), int(previous_wickets)]

        inp_features = np.array([temp_array])

        my_prediction = int(model.predict(inp_features)[0])
              
            

        # displaying the prediction on web app
        st.write(f'The predicted score for {batteam} vs {bowlteam} is between {my_prediction-10} and {my_prediction+5}')


    
    
    

if __name__ == '__main__':
    main()
    
        