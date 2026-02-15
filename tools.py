import subprocess
import re
import os
import sys
import unicodedata
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.utilities import DuckDuckGoSearchAPIWrapper

def web_search_tool(query: str):
    """
    Gerçek internet araması.
    Ajanların dış kaynaklardan canlı bilgi çekmesini sağlar.
    """
    # Max results artırılarak veri havuzu genişletildi.
    wrapper = DuckDuckGoSearchAPIWrapper(max_results=10)
    search = DuckDuckGoSearchRun(api_wrapper=wrapper)
    
    try:
        # Sorgu temizliği: Gereksiz karakterleri at
        clean_query = query.replace('"', '').replace("'", "").strip()
        
        # Eksik veya hatalı giriş formatı kontrolü.
        if not clean_query or len(clean_query) < 2:
            return "Uyarı: Arama yapmak için çok kısa veya geçersiz bir sorgu girildi."

        # Arama motoru çağrısı
        results = search.run(clean_query)
        
        # Tool çağrısından dönen boş sonuç senaryosu.
        if not results or len(results) < 50:
            return "Uyarı: Arama motoru yeterli veri döndüremedi veya hız sınırına takıldı. Lütfen farklı terimlerle tekrar deneyin."
        
        # Metin Temizliği: Unicode hatalarını ve aşırı boşlukları giderir
        results = "".join(ch for ch in results if unicodedata.category(ch)[0] != 'C' or ch in '\n\r\t')
        results = re.sub(r'\s+', ' ', results).strip()
        
        return results
    except Exception as e:
        # Hata mesajı üretme ve yakalama.
        return f"Arama hatası (Bağlantı veya Hız Sınırı): {str(e)}"

def python_interpreter_tool(code: str):
    """
    Güvenli Python kodu çalıştırma.
    LLM halüsinasyonlarını sayısal olarak doğrulamak için kullanılır.
    """
    try:
        # Gelişmiş Output Parsing: Markdown bloklarını temizle
        clean_code = re.sub(r"```(?:python)?\n?(.*?)```", r"\1", code, flags=re.DOTALL).strip()
        
        # Karakter Onarımı: Ellipsis (...) ve yanlış kopyalanan karakterleri temizle
        clean_code = clean_code.replace("...", "").replace("..", "").replace("’", "'").replace("”", '"')
        
        # Dinamik Fiyat Ayıklama Onarımı (Self-Correction):
        # Eğer ajan hatalı bir prices listesi oluşturduysa, metinden sayıları çekip kodu onarır.
        if "prices =" in clean_code:
            match = re.search(r"prices\s*=\s*\[(.*?)\]", clean_code, re.DOTALL)
            if match:
                inner_content = match.group(1)
                found_numbers = re.findall(r"\d+(?:\.\d+)?", inner_content)
                clean_code = f"prices = [{', '.join(found_numbers)}]\n" + \
                             "if len(prices) > 0:\n" + \
                             "    print(round(sum(prices) / len(prices), 2))\n" + \
                             "else:\n" + \
                             "    print('Hesaplanabilir sayısal veri bulunamadı.')"

        # Boş Kod Kontrolü 
        if not clean_code or len(clean_code) < 5:
            return "Hata: Çalıştırılabilir Python kodu üretilemedi."

        # Sandboxing ve Güvenlik: Zaman aşımı ve UTF-8 zorlaması.
        custom_env = os.environ.copy()
        custom_env["PYTHONIOENCODING"] = "utf-8"

        process = subprocess.run(
            [sys.executable, "-c", clean_code],
            capture_output=True,
            text=True,
            timeout=15, 
            env=custom_env,
            encoding='utf-8'
        )

        if process.returncode == 0:
            return process.stdout.strip()
        else:
            # Kod çalışma hatasını kullanıcıya bildirir
            return f"Python Kod Hatası: {process.stderr.strip()}"
    
    except subprocess.TimeoutExpired:
        return "Hata: Kod çalıştırma güvenli zaman aşımı sınırını (15s) aştı."
    except Exception as e:
        return f"Sistem hatası: {str(e)}"

# Ajan orkestrasyonu için araç haritası.
tools_dict = {
    "search": web_search_tool,
    "python": python_interpreter_tool
}