**Election Fraud Detection Using Machine Learning**

***Project Overview***

This project aims to detect potential election fraud using Machine Learning techniques. The model analyzes election-related and cyber-security related data to identify suspicious voting patterns and fraudulent activities.

***Problem Statement***

Election fraud can affect the transparency and fairness of democratic processes. Manual identification of fraudulent activities is time-consuming and prone to errors. This project uses Machine Learning algorithms to automate fraud detection and assist election authorities in identifying suspicious cases.

***Objective***

Analyze election and cyber-related datasets. Detect potentially fraudulent records. Compare multiple Machine Learning models. Identify important factors contributing to fraud. Provide predictions through an interactive Streamlit web application.

***Dataset***

Source: Kaggle - Strategic Voting Machine dataset (https://www.kaggle.com/datasets/lukhilaksh/strategic-voting-machine), saved locally as Vote_Ai.csv. 22,000 rows x 62 columns.

***The dataset contains features such as:***

Identifiers / location / time: Election_ID, State, Constituency_Code, Constituency_Name, Round, Last_Updated_Time, EVM_Device_ID, Candidate_Name

Candidate profile: Party, Gender, Age, Education, Criminal_Cases, Assets_Cr, Liabilities_Cr, Campaign_Spending_Cr, Social_Media_Followers, Speech_Sentiment, Popularity_Score, Historical_Win_Rate

Electoral / voting: Registered_Voters, EVM_Votes, Postal_Votes, Total_Votes, Vote_Percentage, Voter_Turnout, Urban_Voter_Ratio, Rural_Voter_Ratio, Postal_Vote_Ratio, Vote_Surge_Score, Vote_Change_Per_Round, Late_Round_Surge, Constituency_Volatility, Independent_Candidate_Count, Election_Result

Cyber / fraud indicators: Fraud_Risk_Score, Anomaly_Score, Strategic_Manipulation_Score, Sequential_Risk_Score, Fraud_Proxy_Duplicate, Bot_Activity_Flag, Fake_News_Score, Deepfake_Propagation_Score, Cyber_Attack_Risk, Booth_Capture_Risk, Vote_Injection_Risk, Suspicious_Timing_Index, Adversarial_Pressure, Strategic_Polarization_Index, Influence_Network_Strength, Time_Between_Updates_min, Server_Delay_ms, Network_Failure_Count, Power_Outage_Risk, Attack_Type, Defense_Strategy

Noise columns (named as such in the data): Noise_Float_1, Noise_Float_2, Noise_Category, Correlated_Noise_Score

Target: Fraud_Label. Risk_Category is also present but is derived from the target (see Step 5).

***The following preprocessing steps were performed:***

Handling missing values Converting date and time features Encoding categorical variables Feature scaling Train-test splitting Outlier and skewness analysis Machine Learning Models

***Models evaluated:***

Random Forest Classifier
XGBoost Classifier 
LightGBM Classifier

***Best Model***

LightGBM Classifier

***The best performing model was selected based on:***

Accuracy 
Precision
Recall
F1 Score

***Project Structure***

Election_Fraud_Detection/

│

├── data/

│ └── dataset.csv

│

├── models/

│ └── lightGBM_model.pkl

│

├── app.py

├── train.py

├── requirements.txt

└── README.md

***Technologies Used***

Python

Pandas

NumPy

Scikit-Learn

LightGBM

XGBoost

Streamlit

Matplotlib

Seaborn

***Results***

The model successfully identifies potentially fraudulent election records and provides predictions based on user inputs.

***Limitations***

Dataset size is larger. Accuracy can be improved with more real-world fraud cases. Some features may contain missing or noisy values.

***Future Work***

Decrease dataset size. 
Improve prediction accuracy by adding more real world fraud cases.
Implement deep learning techniques.
Integrate real-time election monitoring.

***Author***

Hyruniza C K
