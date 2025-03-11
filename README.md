📜 Siber SMS - Kurulum ve Kullanım Kılavuzu
📌 Siber SMS, @AtahanArslan tarafından geliştirilmiş, eğitim ve test amaçlı bir SMS gönderme aracıdır.

🔗 GitHub Linki: Siber SMS

🖥 Kali Linux & Termux Kurulum ve Çalıştırma
🔧 1. Gerekli Paketleri Güncelleyin
İlk olarak sisteminizi güncelleyin:
apt update && apt upgrade -y

📦 2. Python3 ve Gerekli Araçları Yükleyin
Eğer sisteminizde Python3 ve pip yüklü değilse aşağıdaki komutları çalıştırın:
apt install python3 python3-pip git -y
Python’un doğru yüklendiğini kontrol etmek için:
python3 --version

📂 3. Siber SMS Projesini İndirin
git clone https://github.com/siberdunyaniz/sibersms.git
cd sibersms

📥 4. Bağımlılıkları Yükleyin
Projenin çalışması için gerekli Python kütüphanelerini yükleyin:
pip3 install -r requirements.txt
Eğer requirements.txt dosyası yoksa manuel olarak yükleyin:
pip3 install colorama requests sms

🚀 5. Python3 ile Çalıştırma
Artık Siber SMS aracını başlatabilirsiniz:
python3 SiberSms.py
📢 Yasa dışı kullanımlar yasaktır!
📢 Destek için: Telegram Kanalı
