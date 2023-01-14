import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.ensemble import RandomForestClassifier
import time
import streamlit.components.v1 as components

#test
st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)
st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #1a1a1a; color: white; text-shadow: 2px 2px 5px black;">
  <a class="navbar-brand" >Machine Learning system using Random Forest Classifier</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
</nav>
""", unsafe_allow_html=True)

st.markdown(
    """
<style>
.sidebar .sidebar-content {
    background-image: linear-gradient(#2e7bcf,#001433);
    color: white;
}
</style>
""",
    unsafe_allow_html=True,
)

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
st.write("""
# DDoS Attack Detection System (Random Forest Classifier)
""")

st.sidebar.header('User Input Features')

st.sidebar.write("""
[Example CSV input file](https://raw.githubusercontent.com/zarulaiman/ddosdetectionv1/main/penguins_example.csv?token=GHSAT0AAAAAAB5GCAUKNSIIUIVJXBCDJQDAY5Z2VYQ)
""")

# Collects user input features into dataframe
uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])
if uploaded_file is not None:
    input_df = pd.read_csv(uploaded_file)
    df = input_df
else:
    st.sidebar.write("Please upload the .csv files and make sure the features are the same as the one that were used as example to make sure no error during the process.")


# Displays the user input features
st.subheader('User Input features')

# test if else menjadi
if uploaded_file is not None:
    st.write(df)
    my_bar = st.progress(0)
    for percent_complete in range(100):
        time.sleep(0.1)
        my_bar.progress(percent_complete + 1)
    # Reads in saved classification model
    load_clf = pickle.load(open('DDOS_RFC.pkl', 'rb'))

    # Apply model to make predictions
    prediction = load_clf.predict(df)
    prediction_proba = load_clf.predict_proba(df)
    st.success('Your dataset has been succesfully scanned! Please refer the table below to know which row is the DDoS Attack or not.')
    st.subheader('Prediction')
    penguins_species = np.array(['BENIGN', 'DDoS'])

    st.write(penguins_species[prediction])

    st.subheader('Prediction Probability')
    st.write(prediction_proba)


else:
    st.write('# --Awaiting User to upload CSV File--')
    st.write('# !ATTENTION!')
    st.write('HOW TO USE THIS WEBSITE? ')
    st.write('- Firstly, make sure that the .csv file have these features (The order does not matter):-')
    st.image('list.png')
    st.write('- Second, make sure the input data do not have any null, infinite or more than 3.4E+38 value or this error will popup')
    st.image('error1.png')
    st.write('- Third, on the left of the website there will be a section to upload the input files.')
    st.write('- Lastly, wait for the application to scan your input files and detect which one is the DDoS Attack or Benign.')
    st.write('  The system will show the input that were uploaded followed by the prediction for every row of the input and end with the probability that the prediction.')
    st.image('result.png')
