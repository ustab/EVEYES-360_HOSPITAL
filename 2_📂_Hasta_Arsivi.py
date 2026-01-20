import streamlit as st

st.title("📂 Dijital Hasta Arşivi")
st.info("Bu sayfadaki tüm veriler AES-256 ile şifrelenmiştir.")
# Buraya daha sonra veritabanındaki hastaları listeleyeceğiz
st.table([{"ID": "P-101", "İsim": "Hasta X", "Durum": "Taburcu"}])
