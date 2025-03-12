Multiscene Pack
Multiscene Pack, birden fazla cihazla bağlantı kurarak multiplayer özellikli bir uygulama geliştirmeyi sağlayan Python kütüphanesidir. Bu kütüphane, socket kullanarak cihazlar arasında bağlantı kurar ve kullanıcıların birbirleriyle iletişim kurmalarına olanak tanır.

Özellikler
MultiConnect: Socket üzerinden bağlantı kurma.
Server: Verilen port ve IP üzerinden bağlantıları kabul etme.
Client: Server ile bağlantı kurup mesaj gönderme.
Kurulum
Gereksinimler
Python 3.x veya üstü
Socket modülü (Python ile birlikte gelir)


2. Gerekli Bağımlılıkları Kurma
Projenin bağımlılıkları yoktur çünkü sadece Python'un standart kütüphanesini kullanmaktadır. Python 3.x'in yüklü olduğundan emin olun.

3. Server'ı Başlatma
Önce server'ı başlatmanız gerekiyor.

server.py dosyasını çalıştırın:
bash
Kopyala
Düzenle
python server.py
Bu, server'ı localhost:12345 portunda başlatacak ve bağlantıları dinlemeye başlayacaktır.

4. Client Bağlantısını Yapma
Server çalıştıktan sonra, client.py dosyasını çalıştırarak bağlantı kurabilirsiniz. Aşağıdaki gibi bir Python dosyasına sahip olmalısınız:

python
Kopyala
Düzenle
from worksets.multiconnect import MultiConnect

# MultiConnect sınıfını kullanarak bağlantı kur
connection = MultiConnect()
if connection.connect():
    connection.disconnect()
Bu, server'a bağlanmayı ve bağlantıyı kesmeyi sağlayacaktır.

Proje Yapısı
Projede şu dosyalar bulunmaktadır:

graphql
Kopyala
Düzenle
multiscene.pack/
├── README.md             # Projeyi tanımlayan dosya
├── folderadder.py        # Yeni klasör ekleyici
├── readcodes.py          # Kod okuma fonksiyonları
├── setuppack.py          # Kurulum dosyası
├── worksets/             # Çalışma seti dosyaları
│   ├── codeextender.py   # Kod düzeltici
│   ├── connection.py     # Bağlantı ile ilgili işlemler
│   ├── foldercontroller.py # Dosya kontrolörü
│   ├── fpsconnector.py   # FPS ayarları
│   ├── localapp.py       # Uygulama oluşturucu
│   ├── multiconnect.py   # Bağlantı yönetimi
│   ├── openconnect.py    # Bağlantı kontrolörü
│   ├── pythonload.py     # Python yükleyici
│   ├── serveron.py       # Server başlatıcı
│   ├── serverrefresh.py  # Server yenileyici
├── Interface/            # Kullanıcı arayüzü dosyaları
│   ├── terminalstarter.py
│   ├── foldersaver.py
│   ├── require.py
│   ├── output.py
│   ├── reader.py
│   ├── printer.py
│   ├── errormessages.py
Katkıda Bulunma
Eğer bu projeye katkı sağlamak isterseniz, lütfen pull request gönderin. Kodunuzu test ettikten sonra uygun gördüğümüzde projeye dahil edebiliriz.

Lisans
Bu proje MIT Lisansı ile lisanslanmıştır. Daha fazla bilgi için LICENSE dosyasına bakabilirsiniz.

