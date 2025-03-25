from colorama import Fore, Style
from time import sleep
from os import system
from sms import SendSms
import threading
import pyfiglet
import webbrowser

# Kullanıcı giriş bilgileri
KULLANICI_ADI = "ariva"
SIFRE = "1234"

def giris_ekrani():
    system("cls||clear")
    print(Fore.LIGHTCYAN_EX + pyfiglet.figlet_format("ARIVA SMS BOM", font="slant"))  # Font değiştirildi
    print(Fore.LIGHTYELLOW_EX + "\n🚀 Bu Tool SiberDünyanız'a Aittir! 🚀")
    print(Fore.LIGHTBLUE_EX + "🔗 Telegram Kanalımıza Katıl: t.me/siberdunyanizz")
    
    # Telegram yönlendirmesi
    webbrowser.open("https://t.me/siberdunyanizz")

    while True:
        kullanici = input(Fore.LIGHTGREEN_EX + "👤 Kullanıcı Adı: ")
        sifre = input(Fore.LIGHTGREEN_EX + "🔑 Şifre: ")
        if kullanici == KULLANICI_ADI and sifre == SIFRE:
            print(Fore.LIGHTBLUE_EX + "✅ Giriş başarılı! Hoşgeldiniz! 🎉")
            sleep(2)
            break
        else:
            print(Fore.LIGHTRED_EX + "❌ Hatalı giriş! Tekrar deneyin. 🔁")
            sleep(2)
            system("cls||clear")

giris_ekrani()

servisler_sms = []
for attribute in dir(SendSms):
    attribute_value = getattr(SendSms, attribute)
    if callable(attribute_value) and not attribute.startswith('__'):
        servisler_sms.append(attribute)

while True:
    system("cls||clear")
    print(Fore.LIGHTCYAN_EX + f"📲 Kullanılabilir SMS Servisleri: {len(servisler_sms)}")
    print(Fore.LIGHTMAGENTA_EX + "\n1️⃣ - Normal SMS Gönder\n2️⃣ - Turbo SMS Gönder ⚡\n3️⃣ - Çıkış 🚪")
    secim = input(Fore.LIGHTYELLOW_EX + "👉 Seçim: ")

    if secim == "1":
        system("cls||clear")
        print(Fore.LIGHTYELLOW_EX + "📞 Telefon numarasını girin (Başında '+90' olmadan): ")
        tel_no = input()
        if len(tel_no) != 10 or not tel_no.isdigit():
            print(Fore.LIGHTRED_EX + "❌ Hatalı numara! Tekrar deneyin.")
            sleep(2)
            continue

        print(Fore.LIGHTYELLOW_EX + "📧 Mail adresi (Bilmiyorsanız Enter'a basın): ")
        mail = input()
        if mail and ("@" not in mail or ".com" not in mail):
            print(Fore.LIGHTRED_EX + "❌ Hatalı mail adresi! Tekrar deneyin.")
            sleep(2)
            continue

        sms = SendSms(tel_no, mail)
        system("cls||clear")
        print(Fore.LIGHTGREEN_EX + "📤 SMS gönderiliyor...")

        # Tüm SMS servislerini deniyoruz
        basari = False
        for fonksiyon in servisler_sms:
            sonuc = getattr(sms, fonksiyon)()
            if sonuc:
                basari = True
                print(Fore.LIGHTGREEN_EX + f"✅ {fonksiyon} ile SMS başarıyla gönderildi!")
            else:
                print(Fore.LIGHTRED_EX + f"❌ {fonksiyon} ile SMS gönderilemedi.")

        if basari:
            print(Fore.LIGHTGREEN_EX + "🎉 Tüm işlemler tamamlandı, SMS başarıyla gönderildi!")
        else:
            print(Fore.LIGHTRED_EX + "❌ Hiçbir servisle SMS gönderilemedi.")

        sleep(3)

    elif secim == "2":
        system("cls||clear")
        print(Fore.LIGHTGREEN_EX + "⚡ Turbo SMS gönderme aktif! ⚡")
        tel_no = input(Fore.LIGHTYELLOW_EX + "📞 Telefon numarasını girin (Başında '+90' olmadan): ")
        if len(tel_no) != 10 or not tel_no.isdigit():
            print(Fore.LIGHTRED_EX + "❌ Hatalı numara! Tekrar deneyin.")
            sleep(2)
            continue

        print(Fore.LIGHTYELLOW_EX + "📧 Mail adresi (Bilmiyorsanız Enter'a basın): ")
        mail = input()
        if mail and ("@" not in mail or ".com" not in mail):
            print(Fore.LIGHTRED_EX + "❌ Hatalı mail adresi! Tekrar deneyin.")
            sleep(2)
            continue

        send_sms = SendSms(tel_no, mail)
        dur = threading.Event()

        def Turbo():
            while not dur.is_set():
                thread_list = []
                for fonk in servisler_sms:
                    t = threading.Thread(target=lambda: print(
                        Fore.LIGHTGREEN_EX + f"✅ {fonk} ile SMS gönderildi!" if getattr(send_sms, fonk)()
                        else Fore.LIGHTRED_EX + f"❌ {fonk} ile SMS başarısız!"
                    ), daemon=True)
                    thread_list.append(t)
                    t.start()

                for t in thread_list:
                    t.join()

        try:
            Turbo()
        except KeyboardInterrupt:
            dur.set()
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "\n🔴 Turbo Mod durduruldu! Menüye dönülüyor...")
            sleep(2)

    elif secim == "3":
        print(Fore.LIGHTRED_EX + "🚪 Çıkış yapılıyor...")
        break

    else:
        print(Fore.LIGHTRED_EX + "❌ Geçersiz seçim! Tekrar deneyin.")
        sleep(2)
