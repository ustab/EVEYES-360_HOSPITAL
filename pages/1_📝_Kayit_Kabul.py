import streamlit as st

st.set_page_config(page_title="Kayıt Kabul - EVEYES 360", layout="wide")
st.title("📝 Hasta Kayıt Kabul ve Karşılama")

with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Hasta Bilgileri")
        ad = st.text_input("Ad Soyad")
        dil = st.selectbox("Dil", ["Türkçe", "English", "Arabic", "French"])
    with col2:
        st.subheader("Mizaç ve Ön Analiz")
        mizac = st.selectbox("Gözlemlenen Mizaç", ["Demevî", "Safravî", "Belgamî", "Sevdavî"])
        
    st.markdown("---")
    if st.button("Kaydı Tamamla ve Terapiyi Başlat"):
        st.success(f"Kayıt Başarılı: {ad} için {mizac} mizacına uygun Selçuklu Makamı tetiklendi.")
        st.info("🎵 Aktif Biosonoloji Modu: Hücresel Dengeleme Başlatıldı.")
