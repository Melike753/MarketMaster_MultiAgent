import os
import sys
import re
from datetime import datetime
from agents import analist, arastirmaci, teknik_buro, mentor, adaptor
from tools import web_search_tool, python_interpreter_tool
from router import get_model_selection

def save_to_log(query, keywords, raw_data, analysis, report):
    log_filename = "market_analiz_log.txt"
    timestamp = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    
    log_content = f"""
    {'='*70}
    TARİH: {timestamp}
    KULLANICI SORGUSU: {query}
    ARAMA TERİMLERİ: {keywords}
    TEKNİK ANALİZ SONUCU: {analysis}

    --- İNTERNETTEN ÇEKİLEN HAM VERİ ---
    {raw_data[:1500]}...

    --- ÜRETİLEN STRATEJİK RAPOR ---
    {report}
    {'='*70}
    \n"""
    try:
        with open(log_filename, "a", encoding="utf-8") as f:
            f.write(log_content)
    except Exception as e:
        print(f"CRITICAL: Log yazımı başarısız: {str(e)}")

def clean_llm_output(text: str):
    text = re.sub(r'^(Burada|İşte|Cevap|Aşağıda|Sonuç).*?:', '', text, flags=re.IGNORECASE).strip()
    return text

def market_master_flow(user_query: str):
    if not user_query or len(user_query.strip()) < 3:
        yield {"step": "error", "message": "Hata: Geçersiz sorgu."}
        return

    try:
        # 1. ADIM: STRATEJİK SORGU ANALİZİ
        yield {"step": 1, "status": "Sorgu Analisti: Arama stratejisi optimize ediliyor...", "data": None}
        raw_keywords = analist.invoke(f"Hedef Ürün/Pazar: {user_query}")
        search_keywords = clean_llm_output(raw_keywords).split('\n')[0].strip()
        
        if "talebi" in search_keywords.lower() or len(search_keywords) < 5:
            search_keywords = f"{user_query} fiyatları ve modelleri 2026"
        
        yield {"step": 1, "status": "Tamamlandı", "data": search_keywords}

        # 2. ADIM: ARAŞTIRMA VE DOĞRULAMA
        yield {"step": 2, "status": "Piyasa Araştırmacı: İnternet verileri taranıyor...", "data": None}
        search_result = web_search_tool(search_keywords)
        
        product_keyword = user_query.split()[0].lower() 
        if product_keyword not in search_result.lower() and "Hata" not in search_result:
            search_result = web_search_tool(f"{user_query} satış fiyatları listesi")

        if "Hata" in search_result or len(search_result) < 100:
            yield {"step": "error", "message": f"'{user_query}' hakkında güncel pazar verisi bulunamadı."}
            return
            
        yield {"step": 2, "status": "Tamamlandı", "data": f"{len(search_result)} karakter veri çekildi."}

        # 3. ADIM: TEKNİK ANALİZ (KODLAMA) 
        yield {"step": 3, "status": "Teknik Analist: Sayısal veriler işleniyor...", "data": None}
        code_prompt = f"Aşağıdaki metindeki fiyatları ayıkla, USD/EUR ise TL'ye (USD=43.61) çevir ve ortalamasını yazdır:\n{search_result[:2000]}"
        
        try:
            generated_code = clean_llm_output(teknik_buro.invoke(code_prompt))
            analysis_result = python_interpreter_tool(generated_code)
        except Exception:
            analysis_result = "Hata"

        # GÜÇLENDİRİLMİŞ REGEX FALLBACK 
        if "Hata" in analysis_result or "tespit edilemedi" in analysis_result or "bulunamadı" in analysis_result:
            prices_raw = re.findall(r'(\d{1,3}(?:[.,]\d{3})*(?:[.,]\d{1,2})?)', search_result)
            clean_prices = []
            for p in prices_raw:
                try:
                    temp_p = p.replace('.', '').replace(',', '.')
                    if temp_p.count('.') > 1:
                        parts = temp_p.split('.')
                        temp_p = "".join(parts[:-1]) + "." + parts[-1]
                    val = float(temp_p)
                    if 100 < val < 250000:
                        if val < 3000: val *= 43.61 
                        clean_prices.append(val)
                except: continue

            if clean_prices:
                avg = sum(clean_prices) / len(clean_prices)
                analysis_result = f"Otomatik Analiz: {avg:.2f} TL (Regex Fallback)"
            else:
                analysis_result = "Hesaplanabilir sayısal fiyat verisi tespit edilemedi."
        
        yield {"step": 3, "status": "Tamamlandı", "data": analysis_result}

        # 4. ADIM: MENTOR RAPORLAMASI 
        yield {"step": 4, "status": "Satın Alma Mentoru: Stratejik rapor oluşturuluyor...", "data": None}
        report_prompt = f"Kullanıcı: {user_query}\nPazar Verisi: {search_result[:1000]}\nAnaliz: {analysis_result}\nÖNEMLİ: Analiz sonucu güncel kurla (43.61) TL bazındadır."
        raw_report = mentor.invoke(report_prompt)
        yield {"step": 4, "status": "Tamamlandı", "data": "Taslak rapor hazır."}

        # 5. ADIM: ADAPTÖR 
        yield {"step": 5, "status": "Format Adaptörü: Son kontroller yapılıyor...", "data": None}
        final_report = adaptor.invoke(f"Bu raporu profesyonel Türkçe ile düzenle, giriş cümlesi ekleme:\n{raw_report}")
        
        # LOGLAMA 
        save_to_log(user_query, search_keywords, search_result, analysis_result, final_report)
        
        yield {"step": 5, "status": "Analiz Tamamlandı", "data": final_report}

    except Exception as e:
        yield {"step": "error", "message": f"Sistem hatası: {str(e)}"}

if __name__ == "__main__":
    print("\n" + "="*50)
    print("   MARKET MASTER v2.0: GÜVENLİ OTONOM SİSTEM")
    print("="*50)

    while True:
        try:
            user_input = input("\nAraştırmak istediğiniz ürün nedir? (Çıkış: q)\n> ")
            if user_input.lower() in ["q", "exit", "çıkış"]: break
            
            # Terminal kullanımı için generator'ı döngüde tüketiyoruz
            for update in market_master_flow(user_input):
                if update["step"] == "error":
                    print(f"\n!!! {update['message']} !!!")
                elif update["data"] is None:
                    print(f"\n{update['status']}")
                elif update["step"] == 5:
                    print("\n" + "!"*15 + " FİNAL RAPORU " + "!"*15)
                    print(update["data"])
                    print("!"*44)
        except KeyboardInterrupt: break
        