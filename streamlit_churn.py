import joblib
import streamlit as st

# Membaca model
with open("model_randomforest_churn.pkl", "rb") as file: # "rb" untuk read binary
    model_churn = joblib.load(file)

# Judul web
st.title("Prediksi Potensi Churn Pelanggan")

# Membagi kolom
col1, col2 = st.columns(2)

# Input kolom variabel fitur
with col1 :
    CreditScore = st.text_input("Score Kredit")

with col2 :
    Geography = st.text_input("Lokasi")

with col1 :
    Gender = st.text_input("Jenis Kelamin")

with col2 :
    Age = st.text_input("Usia")

with col1 :
    Tenure = st.text_input("Lama Berlangganan")

with col2 :
    Balance = st.text_input("Saldo Rekening")

with col1 :
    NumOfProducts = st.text_input("Jumlah Produk")	

with col2:
    HasCrCard = st.text_input("Memiliki Kartu Kredit")

with col1:
    IsActiveMember = st.text_input("Status Keanggotaan")

with col2:
    EstimatedSalary = st.text_input("Perkiraan Gaji")

# code untuk prediksi
churn_predict = ""

# Membuat tombol untuk prediksi
if st.button("Test Prediksi churn"):
    churn_prediction = model_churn.predict([[CreditScore, Geography, Gender, Age, Tenure, Balance, NumOfProducts, HasCrCard, 
                                             IsActiveMember, EstimatedSalary]])

    if(churn_prediction[0] == 1):
        churn_predict = "Pelanggan berpotensi berhenti berlangganan"
    else:
        churn_predict = "Pelanggan kemungkinan besar tetap berlangganan"

    st.success(churn_predict)    
    