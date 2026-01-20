import random
import time
from datetime import datetime
import streamlit as st
# Sayfa Ayarları
st.set_page_config(page_title="EVEYES 360 -HASTANE1", layout="wide")

st.title("🛡️""EVEYES 360 -HASTANE1")
st.markdown("---")

# Yan Menü (Sidebar) - Kayıt ve Seçenekler
with st.sidebar:
    st.header("Hasta Giriş Paneli")
    patient_id = st.text_input("Hasta ID", value="P-999")
    language = st.selectbox("Dil / Language", ["Türkçe", "English", "Arabic"])
    start_test = st.button("Süreci Başlat")

# Ana Ekran
if start_test:
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📊 Canlı Hayati Bulgular")
        # Önceki kodundaki 'vitals' verilerini buraya bağlıyoruz
        st.metric(label="Vücut Isısı", value="38.7 °C", delta="Kritik!", delta_color="inverse")
        st.metric(label="Nabız", value="73 BPM", delta="Normal")

    with col2:
        st.subheader("🎵 Biosonoloji & Terapi")
        st.info("Aktif Makam: **Nihavend**")
        st.write("Frekans: 432 Hz - Hücresel Stabilizasyon Modu")

    st.markdown("---")
    st.subheader("👨‍⚕️ Doktor Karar Destek Paneli")
    st.warning("ÖNERİ: Akut Apandisit Şüphesi - USG İstenmesi Önerilir.")
# 1. EN ÜSTTE: Yardımcı Sınıflar (Araçlar)
class VIPClassifier:
    def __init__(self, p_id): self.p_id = p_id
    def identify_status(self): return "STANDARD"

class LinguisticAI:
    def detect_language(self, audio): return "Turkish"

class FinancialBridge:
    def check_financial_clearance(self, p_id): return True

class BiometricScanner:
    def get_stress_and_pain_levels(self, cam, mic): return {"pain": 2, "stress": 1}

class ReactiveMusicEngine:
    def trigger_healing_sound(self, data): print("Müzik başladı")

class PatientAllocator:
    def __init__(self, p_id): self.p_id = p_id
    def assign_doctor(self): return "Dr. Selçuk"

# --- ANA YÖNETİCİ: KAYIT-KABUL MERKEZİ (RegistrationManager) ---    

class RegistrationManager:
    def __init__(self, patient_id):
        # TEMEL VERİLER
        self.patient_id = patient_id
        self.hospital_name = "EVEYES 360 - Merkez Hastanesi" 
        # MOTORLAR VE SİSTEMLER
        self.vip_manager = VIPClassifier(patient_id)
        self.language_engine = LinguisticAI() 
        self.finance_shield = FinancialBridge()
        self.bio_monitor = BiometricScanner()
        self.music_engine = ReactiveMusicEngine() 
        self.allocator = PatientAllocator(patient_id) # BURAYI EKLEMELİSİN

        # POZİSYON: class'ın bir basamak içinde olmalı
    def process(self, audio_feed, camera_feed):
        # 1. ADIM: Değişkeni önceden tanımla (Hata almamak için)
        bio_data = {"pain": 0, "stress": 0}
        print(f"--- EVEYES 360: {self.patient_id} İÇİN TAM KAYIT BAŞLATILDI ---")
        
        # Müziği başlat
        self.music_engine.trigger_healing_sound(bio_data)
                
        try: # try bloğu başlar
         # 1. TESPİT
                vip_status = self.vip_manager.identify_status()
                language = self.language_engine.detect_language(audio_feed)

            # 2. FİNANS KONTROLÜ
                if not self.finance_shield.check_financial_clearance(self.patient_id):
                  return {"status": "FAILED", "reason": "Finance Barrier"}
                bio_data = self.bio_monitor.get_stress_and_pain_levels(camera_feed, audio_feed)
            # 3. BIOSONOLOJİ
                self.music_engine.trigger_healing_sound(bio_data)
            # 4. DOKTOR ATAMA
                assigned_doctor = self.allocator.assign_doctor()
            # 5. BAŞARILI SONUÇ
                return {
                "PatientID": self.patient_id,
                "VIPStatus": vip_status,
                "Language": language,
                "Doctor": assigned_doctor,
                "InitialBio": bio_data,
                "Status": "SUCCESS"}

        except Exception as e: # except, try ile aynı hizada
            return {"status": "ERROR", "message": str(e)}

class ReactiveMusicEngine:
    def __init__(self):
        # Burada sadece müzik kütüphanesi olsun
        self.makam_library = {
            "Nihavend": {"focus": "pain", "effect": "Kan Dolaşımı ve Fiziksel Ağrı", "hz": 432},
            "Rast": {"focus": "stress", "effect": "Zihinsel Dinginlik ve Kemik Sağlığı", "hz": 440},
            "Rehavi": {"focus": "general", "effect": "Hücresel Yenilenme ve Huzur", "hz": 528}
        }

    def trigger_healing_sound(self, bio_data):
        """  Biyometrik verileri (pain, stress) analiz eder ve  Selçuklu tıbbına göre uygun makamı tetikler. """
        #self.music_engine.trigger_healing_sound(bio_data)
        pain_level = bio_data.get("pain", 0)
        stress_level = bio_data.get("stress", 0)
        print(f"\n[BIOSONOLOGY ENGINE AKTİF] Veri işleniyor: {bio_data}")
        # Karar Mekanizması (Logic Layer)
        if pain_level > 4:
            selected = "Nihavend"
            reason = f"Ağrı seviyesi yüksek ({pain_level})."
        elif stress_level > 3:
            selected = "Rast"
            reason = f"Stres seviyesi saptandı ({stress_level})."
        else:
            selected = "Rehavi"
            reason = "Genel stabilizasyon moduna geçildi."

        makam_info = self.makam_library[selected]
        # 3. Sonucu yazdır
        print(f"Seçilen Makam: {selected}")
        
        # Çıktı: Sistemin neden bu kararı verdiğini kullanıcıya/doktora gösterir
        print(f"Saptanan Durum: {reason}")
        print(f"Tetiklenen Makam: {selected} ({makam_info['hz']} Hz)")
        print(f"Hücresel Etki: {makam_info['effect']} hedefleniyor.")
        print("----------------------------------")


import random
import time
from datetime import datetime, timedelta

# --- KLİNİK ASİSTAN VE YASAL KAYIT KATMANI (HEIDI & LEGAL) ---

class HeidiAsistant:
    """
    HEIDI Modu: Doktorun klinik asistanı gibi çalışır. 
    Konuşmaları dinler, tıbbi bulguları ayıklar ve onay mekanizmasına sunar.
    """
    def __init__(self):
        self.pending_findings = []
        self.medical_dictionary = [
            "Kuğu Boynu Deformitesi", "Ral ve Ronküs", "Akut Apandisit", 
            "Hipertansiyon", "Taşikardi", "Ödem"
        ]

    def listen_and_extract_medical_data(self, audio_stream):
        """
        Doktorun konuşmasından tıbbi bulguları yakalar.
        Örnek: 'Hastada Kuğu Boynu Deformitesi var' -> Bulgulara ekle.
        """
        # Simülasyon: Ses metne dönüştürülüyor (NLP İşlemi)
        mock_speech = "Hastanın fizik muayenesinde Kuğu Boynu Deformitesi var ve hafif ödem gözlendi."
        print(f"[HEIDI-EARS] Dinlenen: '{mock_speech}'")
        
        extracted = []
        for term in self.medical_dictionary:
            if term.lower() in mock_speech.lower():
                extracted.append(term)
        
        self.pending_findings.extend(extracted)
        return extracted

    def confirm_and_save_to_emr(self):
        """Doktor onayından sonra bulguları sisteme yazar."""
        if not self.pending_findings:
            return "Kaydedilecek yeni bulgu yok."
        
        confirmed_data = list(set(self.pending_findings)) # Tekrarları temizle
        self.pending_findings = []
        print(f"[HEIDI-WRITE] Onaylandı ve Sisteme Yazıldı: {confirmed_data}")
        return confirmed_data

class LegalVault:
    """
    Yasal Rehberlik ve Veri Saklama Sistemi (Madde 9).
    Konuşmaları belirli bir süre saklar, sonra kalıcı olarak siler.
    """
    def __init__(self):
        self.storage_limit_days = 365 # 1 yıl saklama süresi (Yasal Rehberlik)
        self.vault = []

    def archive_dialogue(self, patient_id, dialogue_text):
        expiry_date = datetime.now() + timedelta(days=self.storage_limit_days)
        record = {
            "patient_id": patient_id,
            "content": dialogue_text,
            "timestamp": datetime.now(),
            "expiry": expiry_date,
            "status": "ENCRYPTED"
        }
        self.vault.append(record)
        print(f"[LEGAL-VAULT] Diyalog şifrelendi ve arşivlendi. İmha Tarihi: {expiry_date}")

    def purge_expired_records(self):
        """Süresi dolan kayıtları sistemden tamamen temizler."""
        now = datetime.now()
        initial_count = len(self.vault)
        self.vault = [r for r in self.vault if r['expiry'] > now]
        deleted_count = initial_count - len(self.vault)
        if deleted_count > 0:
            print(f"[CLEANUP] {deleted_count} adet eski yasal kayıt kalıcı olarak silindi.")


# --- GÜNCELLENMİŞ MUAYENE MODÜLÜ (ClinicalSuite) ---

class ClinicalSuite:
    """  Muayene odasındaki tüm AI, Anamnez ve HEIDI raporlama süreçlerini yönetir. """
    def __init__(self, patient_id, doctor_id):
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.legal = LegalVault()
        self.heidi_mode = HeidiNarrator() 
        self.ai_analyzer = ClinicalAIAnalyzer()
    
    
    def start_examination(self, camera_feed, audio_feed):
        # 1. Önce diyalog içeriğini oluştur (Sensörlerden gelen veriyi metne çevirmiş gibi yapıyoruz)
        full_dialogue = f"Hasta P-101 muayeneye alındı. Kamera: {camera_feed} aktif."
        
        # 2. Arşivleme yap (Artık 'full_dialogue' tanımlı olduğu için hata vermez)
        self.legal.archive_dialogue(self.patient_id, full_dialogue)
      
        # 3. AI Analizlerini yap
        vitals = self.ai_analyzer.scan_vitals(camera_feed)
        physical=self.ai_analyzer.analyze_physical_state(camera_feed)
        print(f"\n--- MUAYENE BAŞLADI: Hasta {self.patient_id} | Dr. {self.doctor_id} ---")
       
        # 2. Diyalog Analizi (Anamnez)
        # Burayı şimdilik boş bir sözlük veya metin olarak tanımlayabilirsin
        anamnesis_data = "Hasta halsizlik şikayeti ile başvurdu."
        #full_dialogue = "Doktor: Şikayetiniz nedir? Hasta: Ellerimde şekil bozukluğu var..."
        self.legal.archive_dialogue(self.patient_id, full_dialogue)
       
        # 1. Önce AI analizörüyle hayati bulguları tara
        vitals = self.ai_analyzer.scan_vitals(camera_feed)
        physical_status = self.ai_analyzer.scan_physical(camera_feed)
        anamnesis_data = self.ai_analyzer.analyze_speech(audio_feed)
        # 2. Öneriyi Oluştur (3 Parametreyi de gönderiyoruz)
        ai_suggestion = self.ai_analyzer.generate_suggestion(vitals, physical, anamnesis_data)

        # 3. Final Raporu Döndür
        return {
            "PatientID": self.patient_id,
            "Vitals": vitals,
            "PhysicalAnalysis": physical,
            "Anamnesis": anamnesis_data,
            "AISuggestion": ai_suggestion,
            "Status": "COMPLETED",          
            "Timestamp": datetime.now().strftime("%H:%M:%S")}
        
        # --- YARDIMCI ANALİZ SINIFLARI ---

class ClinicalAIAnalyzer:
    """Kamera üzerinden ısı, dolaşım ve fiziksel analiz yapar."""
    def __init__(self):
        pass

    def analyze_speech(self, audio_feed):
        """ Hastanın ses verisini analiz ederek anamnez (hastalık öyküsü) çıkarır. Selçuklu tıbbındaki 'hastanın ifadesi' prensibini simüle eder """
        complaints = ["Baş ağrısı", "Halsizlik", "Mide bulantısı", "Yaygın eklem ağrısı"]
        # Rastgele bir şikayet seçerek simülasyon yapalım
        return f"Hasta Şikayeti: {random.choice(complaints)} (Akut başlangıçlı)."

    def scan_physical(self, camera_feed):
        """Kameradan gelen görüntü ile hastanın fiziksel durumunu, postürünü ve Selçuklu tıbbındaki 'yüz rengi/göz akı'  gibi emareleri analiz eder """
        return "Normal - Postür stabil, yüz rengi sağlıklı (Demevî mizaç belirtileri)."
    def scan_vitals(self, camera_feed):
        # Simülasyon: Uzaktan Termal ve Fotopletismografi (rPPG) analizi
        temp = round(random.uniform(36.2, 39.5), 1)
        pulse = random.randint(60, 110)
        blood_flow = "Normal" if pulse < 95 else "Hızlanmış / Hipertansiyon Riski"
        if temp > 38.5: print("[CRITICAL] Yüksek Ateş Tespit Edildi!")
        return {"temp": temp, "pulse": pulse, "blood_flow": blood_flow}

    def analyze_physical_state(self, camera_feed):
        # Yüz analizi ve mikro-mimiklerle ağrı odağı tespiti
        pain_zones = ["Abdominal", "Cranial", "None"]
        detected_zone = random.choice(pain_zones)
        posture = "Bükük / Koruyucu Refleks" if detected_zone != "None" else "Normal"
        return {"detected_pain_zone": detected_zone, "posture_analysis": posture}
    

    def generate_suggestion(self, vitals, physical, anamnesis):
        # Doktora klinik karar destek önerisi sunar
        if vitals['temp'] > 38.0 and physical['detected_pain_zone'] == "Abdominal":
            return "ÖNERİ: Akut Apandisit Şüphesi - USG ve Kan Sayımı İstenmesi Önerilir."
        return "ÖNERİ: Rutin Kontrol / Semptomatik Tedavi."


class HeidiNarrator:
    """HEIDI Modu: Vocal Narrative ve Yasal Kayıt Sistemi (Madde 7 & 9)."""
    
    def listen_and_record(self, mic_feed):
        # Sesli konuşmayı metne çevirir ve tıbbi terimleri ayıklar
        summary = "Hasta sağ alt kadranda şiddetli ağrı ve mide bulantısı şikayetiyle başvurdu."
        print(f"[HEIDI-REPORT] Sesli kayıt özeti oluşturuldu.")
        return summary
    
    # 3. EN ALTTA: Test Fonksiyonları
def run_heidi_integration_test():
    print("=== EVEYES 360: HEIDI & LEGAL SİSTEM TESTİ ===\n")
    
    # 1. Kayıt
    reg = RegistrationManager("P-101")
    
    # BURAYI GÜNCELLE: Parantez içine iki adet tırnak içinde metin ekle
    reg_data = reg.process("mic_input_active", "cam_input_active") 
   # reg_data = reg.process("audio_stream_data", "camera_stream_data")
   # reg_data = reg.process()
    
    # 2. Muayene ve HEIDI Asistanlığı
    clinic = ClinicalSuite(reg_data["PatientID"], reg_data["Doctor"])
    exam_results = clinic.start_examination("room_cam_01", "room_mic_01")
    
    # 3. Yasal Temizlik (Periyodik kontrol simülasyonu)
    clinic.legal.purge_expired_records()
    
    print("\n[FINAL] Muayene tamamlandı, veriler işlendi ve yasal koruma altına alındı.")

if __name__ == "__main__":
    run_heidi_integration_test()


# --- BÖLÜM 1, 2, 3 (Önceki Sınıflar Buradadır - Kısaltılarak Gösterilmiştir) ---
# [VIPClassifier, LinguisticAI, FinancialBridge, BiometricScanner, vb. burada yer alır]

class VIPClassifier:
    def __init__(self, p_id): self.p_id = p_id
    def identify_status(self): return "STANDARD"

class LinguisticAI:
    def detect_language(self, audio): return "Turkish"

class FinancialBridge:
    def check_financial_clearance(self, p_id): return True

class BiometricScanner:
    def get_stress_and_pain_levels(self, cam, mic): return {"pain": 4.2, "stress": 3.1, "valid": True}

class ReactiveMusicEngine:
    def trigger_healing_sound(self, data): pass

class PatientAllocator:
    def __init__(self, p_id): self.p_id = p_id
    def assign_doctor(self): return "Dr. Selçuk"

# --- ENTEGRASYON TESTİ: MUAYENE ODASI ---

def run_clinical_test():
    print("=== EVEYES 360: KLİNİK SÜREÇ TESTİ BAŞLATILDI ===")
    
    # 1. Adım: Kayıt-Kabul (Zaten Hazırdı)
    reg_manager = RegistrationManager("P-999")
    reg_data = reg_manager.process("audio_stream", "camera_stream")
    
    if reg_data["Status"] == "SUCCESS":
        # 2. Adım: Muayene Odasına Geçiş
        clinic = ClinicalSuite(reg_data["PatientID"], reg_data["Doctor"])
        exam_results = clinic.start_examination("room_cam_hd", "room_mic_array")
        
        print("\n" + "="*50)
        print("DOKTOR EKRANI (DASHBOARD):")
        print(f"Hayati Bulgular: {exam_results['Vitals']}")
        print(f"Fiziksel Analiz: {exam_results['PhysicalAnalysis']}")
        print(f"HEIDI Özeti: {exam_results['Anamnesis']}")
        print(f"AI Karar Destek: {exam_results['AISuggestion']}")
        print("="*50)

if __name__ == "__main__":
    run_clinical_test()