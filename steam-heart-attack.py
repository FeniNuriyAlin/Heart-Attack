import pickle
import streamlit as st

# membaca model
heart_model =  pickle.load(open('heart_model.sav', 'rb'))

#Judul Web
st.title('Data Mining Prediksi Serangan Jantung')

Age = st.text_input('Input Umur')

sex = st.text_input('Jenis Kelamin')

cp = st.text_input('Jenis Nyeri Pada Dada')

trtbps = st.text_input('Input Tekanan Darah')

chol = st.text_input('Input Hasil Kolesterol')

fbs = st.text_input('Input Hasil Gula Darah')

restecg = st.text_input('Input Hasil Elektrokardiografi')

thalachh = st.text_input('Input Hasil Detak Jantung ')

exng = st.text_input('Input Hasil Angina Akibat Olahraga')

oldpeak = st.text_input('Input Hasil depresi ')

slp = st.text_input('Input Hasil Tekanan Depresi Maksimal')

caa = st.text_input('Input Hasil Pembuluh Darah ')

thall = st.text_input('Input Hasil Kelainan Darah')

# code untuk kelompok jenis bunga
heart_diagnosis = ''

# membuat tombol untuk prediksi
if st.button('Test Prediksi'):
    heart_prediction = heart_model.predict([[Age, sex, cp, trtbps, chol, fbs, restecg, thalachh, exng, oldpeak, slp, caa, thall]])
    if(heart_prediction[0] == 1):
        heart_diagnosis = 'Pasien Terkena Serangan Jantung'
    else :
        heart_diagnosis = 'Pasien tidak Terkena Serangan Jantung'

    st.success(heart_diagnosis)
