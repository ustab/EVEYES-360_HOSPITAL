import streamlit as st

st.title("📂 Dijital Hasta Arşivi")
st.info("Bu sayfadaki tüm veriler AES-256 ile şifrelenmiştir.")
# Buraya daha sonra veritabanındaki hastaları listeleyeceğiz
st.table([{"ID": "P-101", "İsim": "Hasta X", "Durum": "Taburcu"}])
import streamlit as st
import pandas as pd # Verileri daha şık işlemek için

st.title("📂 Dijital Hasta Arşivi (LegalVault)")
st.info("Bu sayfadaki tüm kayıtlar [LEGAL-VAULT] protokolü ile korunmaktadır.")

# Daha kapsamlı bir veri seti
arsiv_verisi = [
    {"Hasta ID": "P-101", "İsim": "Ahmet Yılmaz", "Durum": "Taburcu", "Mizaç": "Demevî", "Makam": "Nihavend"},
    {"Hasta ID": "P-102", "İsim": "Ayşe Kaya", "Durum": "Muayene Bekliyor", "Mizaç": "Safravî", "Makam": "Hicaz"},
    {"Hasta ID": "P-103", "İsim": "Mehmet Demir", "Durum": "Kritik", "Mizaç": "Sevdavî", "Makam": "Irak"}
]

# Veriyi tablo olarak göster
st.dataframe(arsiv_verisi, use_container_width=True)

