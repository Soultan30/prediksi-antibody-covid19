import pickle
import numpy as np
import streamlit as st

model = pickle.load(open('covid.sav', 'rb'))

st.title('Prediksi Antibody Terhadap Penyakit COVID-19')

start_position = st.number_input('Start Position')

end_position = st.number_input('End Position')

chou_fasman = st.number_input('Chou Fasman')

emini = st.number_input('Emini')

kolaskar_tongaonkar = st.number_input('Kolaskar Tongaonkar')

parker = st.number_input('Parker')

isoelectric_point = st.number_input('Isoelectric Point')

aromaticity = st.number_input('Aromaticity')

hydrophobicity = st.number_input('Hydrophobicity')

stability = st.number_input('Stability')

covid_diagnosis =''

if st.button('Prediksi Antibody Terhadap Penyakit COVID-19'):
    covid_prediction = model.predict([[start_position, end_position, chou_fasman, emini, kolaskar_tongaonkar, parker, isoelectric_point, aromaticity, hydrophobicity, stability]])
    
    if (covid_prediction[0]==1):
        covid_diagnosis = 'Kuat'
    else:
        covid_diagnosis = 'Lemah'
st.success(covid_diagnosis)
    
