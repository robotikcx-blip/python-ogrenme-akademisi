from flask import Flask, render_template, request

app = Flask(__name__)

# Devasa Veri Havuzu
EGITIM_DATASI = {
    "Veri Tipleri": {
        "Aciklama": "Python'da her şey bir nesnedir ve her verinin bir tipi vardır.",
        "Detaylar": [
            {"alt_baslik": "Numbers (Sayılar)", "icerik": "Tam sayılar (int) ve ondalıklı sayılar (float).", "kod": "x = 10  # int\ny = 3.14 # float"},
            {"alt_baslik": "Strings (Metinler)", "icerik": "Tırnak içindeki her şey.", "kod": "isim = 'Gemini'\nmesaj = \"Merhaba Dünya\""},
            {"alt_baslik": "Boolean (Mantıksal)", "icerik": "Sadece True veya False değerini alır.", "kod": "sistem_acik_mi = True"}
        ]
    },
    "Listeler (Lists)": {
        "Aciklama": "Listeler, birden fazla veriyi tek bir kutuda saklamanı sağlar. Sıralıdır ve değiştirilebilir.",
        "Detaylar": [
            {"alt_baslik": "Liste Tanımlama", "icerik": "Köşeli parantez [] kullanılır.", "kod": "meyveler = ['elma', 'armut', 'muz']"},
            {"alt_baslik": "append() - Ekleme", "icerik": "Listenin EN SONUNA yeni bir eleman ekler.", "kod": "meyveler.append('çilek')\n# Sonuç: ['elma', 'armut', 'muz', 'çilek']"},
            {"alt_baslik": "pop() - Silme", "icerik": "Belirli bir sıradaki elemanı siler. Boş bırakırsan en sondakini siler.", "kod": "meyveler.pop(0) # İlk elemanı (elma) siler\nmeyveler.pop()  # En sondakini siler"},
            {"alt_baslik": "Slicing (Dilimleme)", "icerik": "Listenin belirli bir parçasını almanı sağlar.", "kod": "sayilar = [0,1,2,3,4,5]\nprint(sayilar[1:4]) # 1, 2 ve 3. indexleri getirir"}
        ]
    },
    "Dosya İşlemleri": {
        "Aciklama": "Bilgisayardaki dosyalara erişmek, okumak ve yazmak için kullanılır.",
        "Detaylar": [
            {"alt_baslik": "'r' Modu (Read)", "icerik": "Sadece okumak için açar. Dosya yoksa hata verir.", "kod": "with open('notlar.txt', 'r') as f:\n    icerik = f.read()"},
            {"alt_baslik": "'w' Modu (Write)", "icerik": "Yazmak için açar. İçindekileri SİLER, baştan yazar. Dosya yoksa oluşturur.", "kod": "with open('notlar.txt', 'w') as f:\n    f.write('Her şey silindi, bu yazıldı.')"},
            {"alt_baslik": "'a' Modu (Append)", "icerik": "Ekleme yapar. Mevcut verilere dokunmaz, sonuna ekler.", "kod": "with open('notlar.txt', 'a') as f:\n    f.write('\\nYeni satır eklendi.')"}
        ]
    },
    "Hata Yönetimi (Try-Except)": {
        "Aciklama": "Programın beklenmedik hatalarda çökmesini engeller.",
        "Detaylar": [
            {"alt_baslik": "Temel Mantık", "icerik": "Hata riski olan kodu try içine, çözümünü except içine yazarsın.", "kod": "try:\n    sayi = int(input('Sayı gir:'))\n    print(10 / sayi)\nexcept ZeroDivisionError:\n    print('Sıfıra bölünme hatası!')\nexcept ValueError:\n    print('Lütfen sadece sayı gir!')"}
        ]
    },
    "Flask Temelleri": {
        "Aciklama": "Python ile web sitesi yapmamızı sağlayan 'kütüphane' (framework).",
        "Detaylar": [
            {"alt_baslik": "Route (Yönlendirme)", "icerik": "Hangi URL'ye gidince hangi fonksiyon çalışacak?", "kod": "@app.route('/haberler')\ndef haber():\n    return 'Haberler Sayfası'"},
            {"alt_baslik": "Methods (GET/POST)", "icerik": "GET veri ister, POST veri gönderir (formlar gibi).", "kod": "@app.route('/', methods=['GET', 'POST'])\nif request.method == 'POST':\n    data = request.form.get('isim')"}
        ]
    }
}

@app.route("/", methods=["GET", "POST"])
def index():
    secilen_ana_konu = request.form.get("konu_adi")
    detay_verisi = EGITIM_DATASI.get(secilen_ana_konu)
    
    return render_template("index.html", 
                           konular=EGITIM_DATASI.keys(), 
                           secilen=secilen_ana_konu, 
                           detaylar=detay_verisi)

if __name__ == "__main__":
    app.run(debug=True)