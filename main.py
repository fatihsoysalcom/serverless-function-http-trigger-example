from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/hello', methods=['GET', 'POST'])
def hello_function():
    # Bu fonksiyon, bir HTTP isteğiyle tetiklenen sunucusuz bir fonksiyonu simüle eder.
    # Gerçek bir sunucusuz ortamda, bu kod bir FaaS (Function as a Service) olarak dağıtılır.

    name = request.args.get('name') # Sorgu parametrelerinden 'name' almaya çalış (GET)
    if not name and request.is_json:
        name = request.json.get('name') # JSON gövdesinden 'name' almaya çalış (POST)
    if not name:
        name = 'Dünya' # 'name' sağlanmazsa varsayılan isim

    # "Sunucusuz fonksiyonumuzun" temel iş mantığı
    greeting = f"Merhaba, {name}! Bu sunucusuz bir fonksiyon simülasyonudur."

    # Gerçek bir sunucusuz ortamda, bulut sağlayıcısı (AWS, Azure, Google Cloud vb.)
    # altyapı, ölçeklendirme ve yürütme ortamını yönetir.
    # Geliştiriciler olarak sadece kod mantığına ve yanıtına odaklanırız.

    return jsonify({"message": greeting})

if __name__ == '__main__':
    # Bu kısım, fonksiyonu tetikleyen "olay dinleyicisini" simüle eder.
    # Gerçek bir sunucusuz kurulumda, bulut sağlayıcısının altyapısı
    # olayları (HTTP istekleri gibi) dinler ve fonksiyonumuzu çağırır.
    print("\nSunucusuz fonksiyon simülasyonu başlatılıyor...")
    print("http://127.0.0.1:5000/hello adresine GET veya POST isteği gönderin.")
    print("Örnek: http://127.0.0.1:5000/hello?name=Kullanıcı")
    print("Örnek POST: curl -X POST -H \"Content-Type: application/json\" -d '{\"name\": \"API_Kullanıcısı\"}' http://127.0.0.1:5000/hello\n")
    app.run(debug=True, port=5000)
