import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load the trained model and encoder
model = joblib.load('best_rf_model.joblib')
ohe = joblib.load('ohe.joblib')  # Load the saved OneHotEncoder

# Define team and city options (ensure these match training categories)
teams = [
    'Sunrisers Hyderabad', 'Mumbai Indians', 'Royal Challengers Bangalore',
    'Kolkata Knight Riders', 'Kings XI Punjab', 'Chennai Super Kings',
    'Rajasthan Royals', 'Delhi Capitals'
]
cities = [
    'Hyderabad', 'Pune', 'Indore', 'Bangalore', 'Mumbai',
    'Kolkata', 'Delhi', 'Chandigarh', 'Jaipur', 'Chennai', 'Cape Town',
    'Port Elizabeth', 'Durban', 'Centurion', 'East London', 'Johannesburg',
    'Kimberley', 'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
    'Visakhapatnam', 'Raipur', 'Ranchi', 'Abu Dhabi', 'Sharjah', 'Mohali',
    'Bengaluru'
]

# Streamlit UI
st.title("Cricket Match Outcome Predictor")

# Team selection
batting_team = st.selectbox("Select Batting Team", teams)
bowling_team = st.selectbox("Select Bowling Team", teams)
city = st.selectbox("Select City", cities)

# Match situation inputs
runs_left = st.number_input("Runs Left", min_value=0)
balls_left = st.number_input("Balls Left", min_value=1)
wickets = st.number_input("Wickets in Hand", min_value=0, max_value=10)
total_runs_x = st.number_input("Target Score", min_value=0)
crr = st.number_input("Current Run Rate", min_value=0.0)
rrr = st.number_input("Required Run Rate", min_value=0.0)

# Make Prediction
if st.button("Predict Outcome"):
    # Prepare input for model
    input_df = pd.DataFrame([[batting_team, bowling_team, city, runs_left, balls_left, wickets, total_runs_x, crr, rrr]],
                            columns=['batting_team', 'bowling_team', 'city', 'runs_left', 'balls_left', 'wickets', 'total_runs_x', 'crr', 'rrr'])

    # Encode categorical features with the loaded encoder
    encoded_input = ohe.transform(input_df[['batting_team', 'bowling_team', 'city']])

    # Combine encoded and numerical features
    final_input = np.concatenate([encoded_input, input_df[['runs_left', 'balls_left', 'wickets', 'total_runs_x', 'crr', 'rrr']].values], axis=1)

    # Check if final input has correct shape
    if final_input.shape[1] == model.n_features_in_:
        # Predict probabilities
        win_prob = model.predict_proba(final_input)[0][1] * 100  # Probability of winning
        lose_prob = 100 - win_prob  # Probability of losing

        # Display the result
        st.write(f"Win Probability: {win_prob:.2f}%")
        st.write(f"Lose Probability: {lose_prob:.2f}%")
    else:
        st.error(f"Model expected {model.n_features_in_} features, but got {final_input.shape[1]}. Please check encoding consistency.")

