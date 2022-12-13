import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.ensemble import RandomForestClassifier

st.write("""
# DDoS Attack Detection System (Machine Learning)

""")

st.sidebar.header('User Input Features')

st.sidebar.markdown("""
[Example CSV input file](https://raw.githubusercontent.com/dataprofessor/data/master/penguins_example.csv)
""")

# Collects user input features into dataframe
uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])
if uploaded_file is not None:
    input_df = pd.read_csv(uploaded_file)
    df = input_df
else:
    st.sidebar.write("Before upload, text ni akan appear, lepas upload csv text ni akan hilang, pandai2 kau atur")


# Displays the user input features
st.subheader('User Input features')

# test if else menjadi
if uploaded_file is not None:
    st.write(df)
    # Reads in saved classification model
    load_clf = pickle.load(open('DDOS_RFC.pkl', 'rb'))

    # Apply model to make predictions
    prediction = load_clf.predict(df)
    prediction_proba = load_clf.predict_proba(df)

    st.subheader('Prediction')
    penguins_species = np.array(['BENIGN', 'DDoS'])

    st.write(penguins_species[prediction])

    st.subheader('Prediction Probability')
    st.write(prediction_proba)


else:
    st.write('# --Awaiting Czarul to upload CSV File--')
    st.write('--mcm biasa text ni hilang lepas kau upload file--')

