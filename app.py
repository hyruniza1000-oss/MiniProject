
import streamlit as st
import pandas as pd
import numpy as np
import joblib


#Loading LGBM Model
lightGBM_model=joblib.load(open('lightGBM_model.pkl', 'rb'))

#Page Configuration
st.set_page_config(page_title="Voting Fraud Detection", page_icon=":bar_chart:", layout="wide")

st.title("🔍Voting Fraud Detection📊")
st.subheader("LightGBM Machine Learning Model")
st.write("Enter Election details to predict Fraud risk📰")

# Input layout
col1, col2 = st.columns(2)

with col1:
    round = st.number_input("Round", 0, 20, 1)
    Constituency_Name = st.number_input("Constituency Name", 50, 300, 120)
    Total_Votes = st.number_input("Total Votes ", 30, 150, 70)
    Postal_Votes = st.number_input("Postal Votes", 0, 100, 20)
    Vote_Percentage = st.number_input("VotePercentage", 0, 100, 20)
    Vote_Surge_score= st.number_input("Vote Surge Score", 0, 100, 20)
    Constituency_Volatility = st.number_input("Constituency Volatility", 0, 100, 20)
    Postal_Vote_Ratio = st.number_input("Postal Vote Ratio", 0, 100, 20)



with col2:
    Anomaly_Score = st.number_input("Anomaly Score", 0, 100, 50)
    Bot_Activity_Flag = st.number_input("Bot Activity Flag", 0, 1, 0)
    Fake_News_Score = st.number_input("Fake News Score", 0.05, 2.5, 0.5)
    Cyber_Attack_Risk = st.number_input("Cyber Attack Risk", 0, 100, 50)
    Server_Delay_ms = st.number_input("Server Delay (ms)", 0, 1000, 100)
    Late_Round_Surge = st.number_input("Late Round Surge", 0, 100, 20)
    Defense_Strategy = st.number_input("Defense Strategy", 0, 100, 20)
    

# Prediction
if st.button("🔍 Predict Fraud"):
    
    input_data = np.array([[round, Constituency_Name, Total_Votes, Postal_Votes,
       Vote_Percentage,Vote_Surge_score, Constituency_Volatility,
       Postal_Vote_Ratio, Anomaly_Score, Bot_Activity_Flag,
       Fake_News_Score, Cyber_Attack_Risk, Server_Delay_ms,
       Late_Round_Surge, Defense_Strategy]])
    
    prediction = lightGBM_model.predict(input_data)[0]
    
    if prediction == 1:
        st.error("⚠️ High Risk: Fraud Detected in the Election")
    else:
        st.success("✅ Low Risk: No Fraud Detected in the Election")

st.markdown("---")
st.caption("lightGBM Model | Streamlit Deployment | Sklearn")