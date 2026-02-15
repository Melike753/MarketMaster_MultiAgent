# 📈 Market Master: Otonom Pazar Analisti

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit)
![Ollama](https://img.shields.io/badge/Ollama-Local_LLM-white?style=for-the-badge)

![LangChain](https://img.shields.io/badge/LangChain-Architecture-121212?style=for-the-badge)
![DuckDuckGo](https://img.shields.io/badge/DuckDuckGo-Search_Tool-005571?style=for-the-badge&logo=duckduckgo)
![Python Sandbox](https://img.shields.io/badge/Python-Sandbox_Safety-3776AB?style=for-the-badge&logo=python)

---

**Market Master**; statik yapay zeka yanıtlarının ötesine geçerek, yerel kaynaklı (**Local LLM**) modelleri uzmanlaşmış bir çoklu ajan (**Multi-Agent**) hiyerarşisiyle koordine eden uçtan uca bir pazar analizi ekosistemidir. 

Sistem; ham kullanıcı taleplerini alır, **LLM Cascading** stratejisiyle optimize edilmiş modeller (1B vs 8B) arasında görev dağıtımı yapar ve gerçek zamanlı internet verilerini izole bir **Python Sandbox** ortamında matematiksel doğrulamadan geçirerek stratejik satın alma raporlarına dönüştürür. 

### ✨ Neden Farklı?
* **Otonom Muhakeme**: 5 farklı uzman ajanın birbirini denetlediği yatay bir operasyon hattı kullanır.
* **Güvenli Uygulama**: Sayısal veriler LLM tahminlerine bırakılmaz; otonom üretilen Python kodları ile "Self-Correction" mekanizması altında sandbox ortamında hesaplanır.
* **Hibrit Model Yönetimi**: Görev tipine ve bağlam yoğunluğuna göre dinamik model yönlendirmesi yaparak (Router) yerel donanım kaynaklarını en verimli şekilde kullanır.

---

## 📝 1. Proje Özeti ve Vizyon

Günümüzün bilgi kirliliği ve manipülatif veri ortamında, sadece bir ürünü aramak değil, o ürünün gerçek pazar değerine ulaşmak bir mühendislik problemidir. Market Master, kullanıcıdan gelen basit bir ürün sorgusunu; internetten canlı veri toplayan, topladığı veriyi halüsinasyon riskine karşı gerçek kodlarla doğrulayan ve pazar stratejisine dönüştüren otonom bir iş hattıdır.

Bu projenin vizyonu, tek bir yapay zeka modelinin sınırlı yeteneklerine güvenmek yerine; her biri kendi alanında uzmanlaşmış ajanların bir araya gelerek karmaşık problemleri çözdüğü bir "dijital iş gücü" yaratmaktır. Tamamen yerel (local) kaynaklar üzerinde çalışan bu mimari, veri gizliliğini en üst seviyede tutarken; LLM Cascading stratejisiyle donanım gücünü en verimli şekilde kullanarak profesyonel düzeyde analiz raporları üretir.

---

## 🤖 2. Çoklu Ajan Mimarisi ve İş Akışı

Sistem, ham veriyi rafine bir pazar stratejisine dönüştüren, her biri bir sonraki aşamanın denetleyicisi ve veri sağlayıcısı olan 5 uzman ajandan oluşan bir "otonom operasyon hattı" üzerine kuruludur:


* **🔍 Sorgu Analisti (Query Strategist)**: Kullanıcının doğal dil sorgusunu deşifre eder; pazar trendlerini yakalayacak, gürültüden arındırılmış ve arama motoru verimliliği maksimize edilmiş 3 stratejik anahtar kelime öbeği üretir.
* **🌐 Piyasa Araştırmacı (Market Researcher)**: Canlı internet ekosisteminden gelen verileri tarar; reklamları, alakasız haberleri ve yanıltıcı içerikleri ayıklayarak sistemi sadece gerçek satıcı verileri ve teknik ürün spesifikasyonlarıyla besler.
* **🐍 Teknik Analist (Data Engineer)**: Eldeki metinsel veriyi sayısal bir modele dönüştürür. Ürettiği Python kodlarını izole bir Sandbox ortamında koşturarak; USD/EUR gibi döviz birimlerini şu anki kur parametreleriyle Türk Lirasına standardize eder ve istatistiksel bir veri tabanı oluşturur.
* **🧠 Satın Alma Mentoru (Decision Support)**: Teknik analizin sayısal çıktılarını pazar gerçekleriyle yorumlar. Halüsinasyon bariyerlerini aktif tutarak, sadece doğrulanmış verilere dayalı "al/bekle/araştır" tavsiyeleri ve risk analizleri geliştirir.
* **✍️ Format Adaptörü (Linguistic Auditor)**: Üretilen tüm teknik ve stratejik raporu son kontrol sürecinden geçirir. İngilizce kalıpları ve teknik gürültüyü temizleyerek, son kullanıcıya hitap eden profesyonel, akıcı ve tamamen Türkçe bir final raporu sunar.

---

## 🧠 3. Model Seçim Stratejisi: LLM Cascading

Bu proje, "her görev için en büyük modeli kullanma" verimsizliği yerine, yerel donanım kaynaklarını akıllıca yöneten bir LLM Cascading (Kademeli Model) mimarisi üzerine inşa edilmiştir. Amaç, sistemin toplam yanıt süresini (latency) düşürürken, kritik analizlerdeki doğruluk payını (accuracy) maksimize etmektir.

### 📉 Hibrit Model Yapılandırması
* **Hız Odaklı (Llama 3.2 - 1B)**: Sorgu analizi ve anahtar kelime üretimi gibi hızın doğruluğun bir adım önünde olduğu, düşük muhakeme gerektiren başlangıç adımlarında kullanılır. Bu sayede basit işlemler milisaniyeler içinde tamamlanır.
* **Doğruluk Odaklı (Llama 3 - 8B)**: Kod yazımı, karmaşık veri analizi ve stratejik raporlama gibi hata payının sıfıra yakın olması gereken süreçlerde devreye girer. Sistemin "karar verici" mekanizması olarak yüksek muhakeme (reasoning) kapasitesi sunar.


### 🚦 Dinamik Karar Mekanizması (router.py)
Sistem, `get_model_selection` fonksiyonu ile her ajan çağrısında şu üç kritik parametreyi otonom olarak değerlendirir:

1. **Görev Hassasiyeti (Task-Specific Routing)**: `coding` ve `reporting` görevleri, "Kritik Görev" statüsünde değerlendirilerek her zaman 8B modeline yönlendirilir; böylece teknik hataların ve halüsinasyonların önüne geçilir.
2. **Bağlam Yoğunluğu (Attention-Aware Scaling)**:  İşlenecek veri 1000 karakter eşiğini aştığında, küçük modellerin uzun metinlerde yaşadığı "dikkat kaybı" (attention loss) riskini bertaraf etmek için sistem otomatik olarak 8B modeline geçiş yapar.
3. **Performans ve Kaynak Dengesi**: Basit mantıksal çıkarımlar 1B modelinde çözülerek ekran kartı belleği (VRAM) ve işlemci yükü optimize edilir; bu da sistemin yerel cihazlarda akıcı çalışmasını sağlar.

---

## 🛠 4. Otonom Araç Entegrasyonu ve Güvenlik Protokolleri

Ajanlar, saf metin üretiminin ötesine geçmek ve analizlerini gerçek dünya verileriyle temellendirmek için iki kritik yeteneği **"Tool Use"** protokolüyle otonom olarak yönetir:

### 🌐 Canlı Veri Erişimi (Web Search Tool)
* **Neden?**: Statik LLM eğitim verileri, güncel pazar fiyatlarını ve anlık trendleri takip edemediği için sistemin güncelliğini koruması zorunludur.
* **Çözüm**: DuckDuckGo API wrapper aracılığıyla dış kaynaklardan gerçek zamanlı pazar verileri çekilir.
* **Rafine Veri**: Çekilen ham içerik, anlamsal gürültüden (reklam, alakasız içerik) arındırılmak üzere piyasa araştırmacısı ajana "temizlenmiş veri havuzu" olarak iletilir.

### 🛡️ Hesaplama Güvenliği (Python Sandbox)
* **Neden?**: LLM'ler karmaşık matematiksel işlemlerde ve kur dönüşümlerinde halüsinasyon (hatalı sayı üretme) riski taşır; bu da pazar analizinin güvenilirliğini zedeler.
* **Çözüm**: Sayısal analizler LLM tahminine bırakılmaz; ajan tarafından üretilen gerçek Python kodları izole bir **Sandbox** ortamında çalıştırılır.
* **Öz-Onarım (Self-Correction)**: LLM'in üretebileceği sözdizimi hataları veya eksik kod blokları (ellipsis `...` vb.), sisteme entegre edilen **Regex tabanlı iyileştirme katmanı** ile otomatik olarak onarılır.
* **Güvenlik Bariyeri**: Ana sistemi korumak adına, sonsuz döngü ve aşırı kaynak tüketimine karşı **15 saniyelik sert `timeout`** sınırı ve izole `subprocess` protokolü uygulanır.

--- 

## ⚡ 5. Mühendislik Zorlukları ve Çözümler

Geliştirme sürecinde karşılaşılan teknik kısıtlamalar ve donanım limitleri, sistemin sürekliliğini ve kullanıcı deneyimini korumak amacıyla aşağıdaki mühendislik yaklaşımlarıyla aşılmıştır:

### ⏳ Asenkron Akış ve Kullanıcı Deneyimi (Latency Management)
* **Zorluk**: Yerel donanım üzerinde çalışan modellerin (Local LLM) üretim süresi, bulut tabanlı servislere göre daha uzun olabilmekte ve bu durum arayüzün "donmuş" gibi algılanmasına neden olmaktadır.
* **Çözüm**: Sistem, Streamlit üzerinde `yield` yapısı destekli bir **Canlı Akış (Streaming)** protokolü ile modernize edilmiştir. Bu sayede ajanların her bir adımı (sorgu optimizasyonu, arama, analiz) anlık olarak arayüzde görselleştirilerek kullanıcıya kesintisiz geri bildirim sağlanmaktadır.

### 💹 Dinamik Döviz ve Birim Standardizasyonu
* **Zorluk**: Küresel pazardan çekilen veriler farklı para birimlerinde ($, €, ₺) gelmekte, bu da fiyat analizlerinde tutarsız sonuçlara yol açmaktadır.
* **Çözüm**: Teknik Analist ajanı, analiz sürecinde ham veriyi doğrudan işlemek yerine; sabit kur parametrelerini (1 USD = 43.61 TRY, 1 EUR = 51.87 TRY) kullanan bir **Kur Dönüşüm Katmanı** ile donatılmıştır. Tüm veriler hesaplama öncesinde Türk Lirasına standardize edilerek matematiksel tutarlılık garanti altına alınmıştır.

### 🛡️ Sistem Dayanıklılığı (Regex Fallback Mekanizması)
* **Zorluk**: LLM'lerin nadiren de olsa çalıştırılabilir Python kodu üretmekte başarısız olduğu veya eksik veri döndürdüğü "uç durumlar" (edge cases) sistemin çökmesine neden olabilmektedir.
* **Çözüm**: Sistemin sürekliliğini sağlamak amacıyla bir **Güçlendirilmiş Yedekleme Sistemi (Regex Fallback)** geliştirilmiştir. Eğer kod aracı başarısız olursa, sistem otomatik olarak devreye girerek karmaşık düzenli ifadeler (Regex) ile ham metin içerisinden fiyat verilerini ayıklar ve analizi başarıyla tamamlar.

---

## 🧪 6. Test ve Kalite Güvence: Sistem Doğrulama Protokolleri

Market Master, otonom kararlar veren bir yapı olduğu için sistemin kararlılığı ve hata toleransı, `pytest` framework'ü üzerine inşa edilmiş kapsamlı bir test altyapısı ile garanti altına alınmıştır.

### 🚦 Akıllı Model Yönlendirme Testleri (Decision Logic)
* **Zorluk**: Yanlış model seçimi, basit bir görevde yüksek gecikmeye (latency) veya karmaşık bir görevde hatalı sonuçlara yol açabilir.
* **Çözüm**: `test_model_router_logic` ile sistemin karar mekanizması test edilir. Kısa sorgularda **1B (Hız)**, 1000 karakteri aşan verilerde veya teknik analizlerde ise otomatik olarak **8B (Doğruluk)** modellerinin atanıp atanmadığı her birim testinde doğrulanır.

### 🛡️ Sandboxing ve Kod Güvenliği Testleri (Robustness)
* **Zorluk**: LLM'in ürettiği kontrolsüz kodların ana sistemi çökertme veya sonsuz döngüye sokma riski bulunmaktadır.
* **Çözüm**: `test_python_tool_robustness` senaryoları ile sistemin dayanıklılığı uç sınırlarda test edilir:
    * **Zaman Aşımı**: Sonsuz döngü içeren kodlar 15 saniye sınırında otomatik olarak durdurulur.
    * **Hata Yakalama**: Sıfıra bölme gibi matematiksel hatalar sistem tarafından güvenli bir şekilde yakalanarak kullanıcıya bildirilir.
    * **Bozuk Kod Onarımı**: LLM'in yarım bıraktığı veya '...' (ellipsis) gibi hatalı yapılar içeren kodların otomatik onarılarak doğru sonuç üretip üretmediği kontrol edilir.

### 📥 Veri Giriş ve Arama Doğrulaması (Data Integrity)
* **Zorluk**: Boş sorgular veya anlamsız veri girişleri, sistem kaynaklarının gereksiz tüketilmesine yol açar.
* **Çözüm**: `test_search_tool_reliability` ve sistem girişindeki **Input Validation** katmanıyla; 3 karakterden kısa sorgular veya anlamsız veri setleri sistemin en başında reddedilerek işlem maliyeti minimize edilir.

---

## 📂 7. Klasör Yapısı

Market Master, her modülün net bir sorumluluğu olduğu, karmaşıklıktan uzak ve okunabilirliği yüksek bir dosya yapısı üzerine kurulmuştur:

```text
├── agents.py           # Ajan rollerinin ve promptların tanımlandığı merkez
├── router.py           # Akıllı model seçim mantığı (Cascading)
├── tools.py            # Arama ve Kod çalıştırma araçları
├── main.py             # Ajan orkestrasyonu ve generator akışı
├── ui.py               # Streamlit tabanlı kullanıcı arayüzü ve canlı akış
├── tests.py            # Pytest ile sistem dayanıklılık ve mantık doğrulama testleri
├── requirements.txt    # Proje bağımlılıkları
└── market_analiz_log.txt # Geçmiş analizlerin teknik kayıtları
```

---

## 🚀 5. Kurulum ve Çalıştırma

### Ön Hazırlık

**1.Ollama Kurulumu:** Yerel LLM'lerin çalışabilmesi için [Ollama.com](https://ollama.com) üzerinden uygulamayı indirin.

**2. Modelleri Hazırlayın**: Sistem, LLM Cascading stratejisi için şu iki modele ihtiyaç duyar:

```bash
   ollama pull llama3.2:1b
   ollama pull llama3:8b
```

### Uygulamanın Başlatılması

**1.Sanal Ortamı Oluşturun ve Aktif Edin:**

```bash
    python -m venv venv
    .\venv\Scripts\activate
```

**2. Bağımlılıkları Yükleyin:**

```bash
    pip install -r requirements.txt
```

**3. Uygulamayı Çalıştırın:**

```bash
    streamlit run ui.py
```

---

## 🌟 Son Söz

**Market Master**, geleneksel bir sohbet asistanının ötesinde; ham veriyi otonom olarak işleyen, doğruluğunu izole bir sandbox ortamında gerçek kodlarla teyit eden ve yerel donanım kaynaklarını en üst düzey verimlilikle yöneten bir "dijital iş gücü" projesidir.

Bu çalışma; yapay zekanın sadece metin üretmekle kalmayıp, internet verisi ile matematiksel kesinliği birleştirerek stratejik kararlar alabileceğini kanıtlayan bir mühendislik örneğidir. Veri gizliliğinden ödün vermeden, tamamen yerel kaynaklar üzerinde çalışan bu mimari, otonom pazar analitiğinin geleceğine dair somut bir vizyon sunmaktadır.

**Geliştiren:** *Melike Dönmez* 

---
