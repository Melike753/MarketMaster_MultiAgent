import os
from dotenv import load_dotenv

# .env dosyasındaki değişkenleri yükler
load_dotenv()

def get_model_selection(task_type: str, input_text: str = ""):
    """
    Model seçim stratejisi.
    Görevin türüne, beklenen doğruluğa (accuracy) ve metin uzunluğuna (context) göre karar verir.
    
    Strateji Notu: Literatürdeki 'LLM Cascading' ve 'Cost-Effective Routing' 
    prensipleri baz alınmıştır.
    """
    
    # Küçük ve hızlı görevler için Efficiency-Optimized model.
    # Not: Llama 3.2 1B veya 3B modelleri yerel kullanımda düşük gecikme sağlar.
    fast_model = "llama3.2:1b"
    
    # Karmaşık muhakeme için Accuracy-Optimized model.
    # Not: Llama 3 (8B) veya Mistral (7B) daha yüksek muhakeme kapasitesine sahiptir.
    smart_model = "llama3:8b"

    # ÖNCELİK 1: Teknik Doğruluk ve Güvenlik (Kritik Görevler)
    # Kod yazımı (coding) ve raporlama (reporting) aşamalarında hata payı minimize edilmek zorundadır. Bu yüzden her zaman büyük model seçilir.
    if task_type in ["coding", "reporting"]:
        return smart_model, "Kritik Görev: Yüksek muhakeme ve teknik doğruluk (Reasoning) öncelikli."

    # ÖNCELİK 2: Bağlam Penceresi (Context Window) ve Yoğunluk
    # Arama motorundan gelen veri 1000 karakteri aşıyorsa, küçük modellerde 'Attention' kaybı oluşabileceği için akıllı modele geçiş yapılır.
    if len(input_text) > 1000:
        return smart_model, f"Bağlam Yoğunluğu: {len(input_text)} karakter. Bilgi kaybını önlemek için büyük model seçildi." 

    # ÖNCELİK 3: Hız ve Kaynak Optimizasyonu (Latency-optimized)
    # Sorgu analizi (query_analysis) ve anahtar kelime üretimi basit mantık ve hız gerektirdiği için küçük model yeterlidir.
    if task_type in ["query_analysis", "search"]:
        return fast_model, "Hız Öncelikli: Düşük gecikme süresi (Latency) hedeflendi." 

    # Varsayılan Karar (Fail-Safe): Belirsiz durumlarda doğruluktan ödün vermemek için 8B kullanılır.
    return smart_model, "Varsayılan: Güvenli çalışma modu (Fail-safe) aktif."

if __name__ == "__main__":
    # Test ve Doğrulama süreci 
    print("\n" + "="*60)
    print("   MARKET MASTER: MODEL ROUTER KARAR MEKANİZMASI TESTİ")
    print("="*60)
    
    # Test Senaryoları
    scenarios = [
        {"type": "query_analysis", "input": "Laptop fiyatları", "label": "HIZ (1B)"},
        {"type": "search", "input": "X" * 1500, "label": "BAĞLAM (8B)"},
        {"type": "coding", "input": "prices = [100, 200]", "label": "DOĞRULUK (8B)"},
        {"type": "reporting", "input": "Rapor oluştur", "label": "KALİTE (8B)"}
    ]

    for test in scenarios:
        model, reason = get_model_selection(test["type"], test["input"])
        print(f"\n[TEST - {test['label']}]:")
        print(f"   Görev: {test['type']}")
        print(f"   Seçilen: {model}")
        print(f"   Gerekçe: {reason}")
    
    print("\n" + "="*60)