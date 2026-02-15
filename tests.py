import pytest
import sys
import os
from tools import python_interpreter_tool, web_search_tool
from router import get_model_selection

def test_model_router_logic():
    """
    Model seçim mantığının doğruluğunu ve verimliliğini test eder.
    """
    print("\n[TEST] Model Router Mantığı Kontrol Ediliyor...")
    
    # Hız ve Düşük Gecikme (Kısa metin, basit görev) 
    model, reason = get_model_selection("query_analysis", "laptop")
    assert "1b" in model.lower()
    print(f"   > PASS: Latency-optimized model (1B) seçimi başarılı. Sebep: {reason}")
    
    # Muhakeme ve Bağlam Kapasitesi (Uzun metin veya karmaşık görev) 
    model_long, reason_long = get_model_selection("search", "X" * 1200)
    assert "8b" in model_long.lower()
    print(f"   > PASS: Accuracy-optimized model (8B) seçimi başarılı. Sebep: {reason_long}")

def test_python_tool_robustness():
    """
    Kod aracının güvenliğini ve LLM hatalarını onarma yeteneğini test eder.
    """
    print("\n[TEST] Python Tool Dayanıklılığı ve Güvenliği Kontrol Ediliyor...")

    # Matematiksel Hata Yönetimi
    faulty_code = "print(100 / 0)"
    result = python_interpreter_tool(faulty_code)
    assert "Hata" in result or "Python Kod Hatası" in result
    print("   > PASS: Sıfıra bölme hatası güvenli şekilde yakalandı.")

    # Güvenlik ve Zaman Aşımı (Sonsuz Döngü Koruması) 
    timeout_code = "import time\nwhile True: time.sleep(1)"
    result_timeout = python_interpreter_tool(timeout_code)
    assert "zaman aşımı" in result_timeout.lower()
    print("   > PASS: Sonsuz döngü sandboxing (zaman aşımı) koruması aktif.")

    # Onarım Yeteneği (Bozuk Liste / Ellipsis Fix) 
    # LLM bazen 'prices = [100, 200, ...]' şeklinde bozuk kod üretiyor.
    repair_code = "prices = [1000, 2000, ...]\nprint(sum(prices)/len(prices))"
    result_repair = python_interpreter_tool(repair_code)
    assert "1500" in result_repair
    print(f"   > PASS: Bozuk LLM kodu (ellipsis) başarıyla onarıldı. Sonuç: {result_repair}")

    # Karakter Kodlama (UTF-8 / Para Birimi Simgeleri) 
    encoding_code = "print('Birim Fiyat: 2500 ₺')"
    result_enc = python_interpreter_tool(encoding_code)
    assert "2500" in result_enc
    print("   > PASS: Unicode ve Türkçe karakter desteği doğrulandı.")

def test_search_tool_reliability():
    """
    İnternet arama aracının uç durumlarını test eder.
    """
    print("\n[TEST] İnternet Arama Tool Güvenilirliği Kontrol Ediliyor...")

    # Boş veya Anlamsız Sorgu Yönetimi 
    result_empty = web_search_tool(" ")
    assert "Uyarı" in result_empty or "Hata" in result_empty
    print("   > PASS: Geçersiz sorgu bariyeri çalışıyor.")

    # Veri Filtreleme Kapasitesi 
    # Çok kısa dönen veya başarısız olan aramalar kontrol edilir.
    result_fail = web_search_tool("shdhshshshshshshsh") # Anlamsız dizi
    assert len(result_fail) > 0
    print("   > PASS: Düşük kaliteli veri veya boş sonuç yönetimi başarılı.")

if __name__ == "__main__":
    print("\n" + "="*50)
    print("   MARKET MASTER: SİSTEM DOĞRULAMA (UNIT TESTS)")
    print("="*50)
    
    try:
        test_model_router_logic()
        test_python_tool_robustness()
        test_search_tool_reliability()
        
        print("\n" + "!"*50)
        print(" TEBRİKLER: TÜM TEST SENARYOLARI BAŞARIYLA GEÇTİ! ")
        print("!"*50)
        
    except AssertionError as e:
        print(f"\n[KRİTİK HATA] Test doğrulaması başarısız oldu: {str(e)}")
        sys.exit(1)
    except Exception as e:
        print(f"\n[BEKLENMEDİK HATA] Test sırasında bir aksaklık oluştu: {str(e)}")
        sys.exit(1)