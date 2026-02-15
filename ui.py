import streamlit as st
import time
from main import market_master_flow
import os

# Sayfa Konfigürasyonu
st.set_page_config(
    page_title="Market Master v2.0",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Profesyonel Stil Uygulama 
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #007bff; color: white; }
    
    /* Yatay Kart Tasarımı */
    .pipeline-card { 
        padding: 10px; 
        border-radius: 8px; 
        text-align: center; 
        font-size: 0.85em; 
        min-height: 80px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.05);
        border: 1px solid #e0e0e0;
    }
    .status-active { background-color: #fff9e6; border-top: 4px solid #ffc107; color: #856404; }
    .status-success { background-color: #d4edda; border-top: 4px solid #28a745; color: #155724; }
    .status-waiting { background-color: #f8f9fa; border-top: 4px solid #dee2e6; color: #6c757d; }
    
    /* Zincir Ok İşareti */
    .arrow { font-size: 20px; color: #dee2e6; text-align: center; padding-top: 25px; }
    </style>
    """, unsafe_allow_html=True)

# Yan Panel (Sidebar)
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2103/2103633.png", width=100)
    st.title("Sistem Operasyonları")
    
    # MODEL DURUMU 
    st.subheader("🤖 Model Durumu")
    st.success("Llama 3.2 (1B): Aktif")
    st.success("Llama 3 (8B): Aktif")
    st.caption("Model Seçim Stratejisi: LLM Cascading aktif.")
    
    st.markdown("---")
    
    # ARAÇ YETKİLERİ
    st.subheader("🛠️ Aktif Araçlar")
    st.write("✅ Web Search (DuckDuckGo)")
    st.write("✅ Python Interpreter (Sandbox)")
    st.write("✅ Currency Converter (Real-time)")
    
    st.markdown("---")
    
    # EKONOMİK VERİLER
    st.subheader("💸 Güncel Kurlar")
    st.metric(label="USD / TRY", value="43,61 ₺", delta="Sabit (Şubat '26)")
    st.metric(label="EUR / TRY", value="51,87 ₺", delta="Sabit (Şubat '26)")
    
    st.markdown("---")
    
    # MONITORING & LOGGING 
    st.subheader("📊 Sistem Yönetimi")
    if st.button("Sistem Loglarını Temizle"):
        if os.path.exists("market_analiz_log.txt"):
            os.remove("market_analiz_log.txt")
            st.success("Loglar temizlendi!")
    
    st.caption("v2.0.4 - Multi-Agent Architect")

# Ana Başlık
st.title("📈 Market Master: Otonom Pazar Analisti")
st.caption("Zincirleme Ajan Akışı ile Profesyonel Ürün Araştırması")

# Kullanıcı Girişi
query = st.text_input("Hangi ürün hakkında stratejik analiz raporu istersiniz?", placeholder="Örn: iPhone 16 Pro pazar analizi")

if st.button("Analizi Başlat"):
    if query:
        progress_bar = st.progress(0)
        
        # YATAY ZİNCİR AKIŞI
        st.subheader("🤖 Ajan Zinciri")
        # 5 Ajan ve 4 Ok için sütunlar oluşturur
        cols = st.columns([1, 0.2, 1, 0.2, 1, 0.2, 1, 0.2, 1])
        
        step_placeholders = {
            1: cols[0].empty(),
            2: cols[2].empty(),
            3: cols[4].empty(),
            4: cols[6].empty(),
            5: cols[8].empty()
        }
        
        # Ok işaretlerini yerleştirir
        for i in [1, 3, 5, 7]:
            cols[i].markdown('<div class="arrow">➜</div>', unsafe_allow_html=True)

        # Başlangıç Durumu (Bekliyor)
        for i in range(1, 6):
            step_placeholders[i].markdown(f'<div class="pipeline-card status-waiting">Adım {i}<br>Bekliyor</div>', unsafe_allow_html=True)

        st.markdown("---")
        
        # STRATEJİK RAPOR 
        st.subheader("📝 Stratejik Analiz Raporu")
        final_report_area = st.empty()
        final_report_area.info("Analiz başlatıldı, lütfen ajan zincirini takip ediniz...")

        # Generator Akışı
        try:
            for update in market_master_flow(query):
                step = update.get("step")
                
                if step == "error":
                    st.error(f"❌ Sistem Hatası: {update['message']}")
                    break
                
                progress_bar.progress(step * 20)
                
                if update["data"] is None:
                    # AKTİF (Sarı)
                    step_placeholders[step].markdown(f"""
                        <div class="pipeline-card status-active">
                            <b>ADIM {step}</b><br>Çalışıyor...
                        </div>
                    """, unsafe_allow_html=True)
                else:
                    # TAMAMLANDI (Yeşil)
                    step_placeholders[step].markdown(f"""
                        <div class="pipeline-card status-success">
                            <b>ADIM {step}</b><br>Tamamlandı
                        </div>
                    """, unsafe_allow_html=True)

                    if step == 5:
                        st.balloons()
                        with final_report_area:
                            st.markdown(update["data"])
                            
        except Exception as e:
            st.error(f"Hata: {str(e)}")
    else:
        st.warning("Lütfen bir ürün adı giriniz.")

# Alt Bilgi
st.markdown("---")
st.caption("Market Master v2.0 | Multi-Agent Local LLM Project | 2026")