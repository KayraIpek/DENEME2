from tkinter import *
from PIL import ImageTk, Image

# --- 1. Veri Yapısı ---
# 6 adet tarifi sözlük olarak yazdım. 
tarifler = [
    {
        "ad": "Menemen",
        "resim": "menemen",
        "malzemeler": [
            "3 adet yumurta",
            "2 adet domates",
            "2 adet yeşil biber",
            "1 yemek kaşığı sıvı yağ",
            "Tuz, karabiber"
        ],
        "yapilis": [
            "Tavaya yağı koyup ısıtın, doğranmış biberleri ekleyip kavurun.",
            "Doğranmış domatesleri ekleyip suyunu çekene kadar pişirin.",
            "Yumurtaları kırın, isteğe göre karıştırarak ya da bütün bırakarak pişirin.",
            "Tuz ve karabiber ile tatlandırıp servis edin."
        ]
    },
    {
        "ad": "Islak Kek (Kakaolu)",
        "resim": "islak_kek",
        "malzemeler": [
            "3 adet yumurta",
            "1 su bardağı toz şeker",
            "1 su bardağı süt",
            "1 su bardağı sıvı yağ",
            "2 yemek kaşığı kakao",
            "1 paket kabartma tozu",
            "1,5 su bardağı un"
        ],
        "yapilis": [
            "Yumurta ve şekeri köpürene kadar çırpın.",
            "Süt, sıvı yağ, kakao ekleyip karıştırın, sonra un ve kabartma tozunu ekleyin.",
            "Yağlanmış kalıba döküp önceden ısıtılmış 180°C fırında yaklaşık 25–30 dakika pişirin.",
            "Fırından çıkarınca üzerine ılık sos döküp dinlendirdikten sonra servis edin."
        ]
    },
    {
        "ad": "Mercimek Çorbası",
        "resim": "MercoCorb",
        "malzemeler": [
            "1 su bardağı kırmızı mercimek",
            "1 adet soğan",
            "1 adet havuç (isteğe bağlı)",
            "1 yemek kaşığı un",
            "1 yemek kaşığı salça",
            "4 su bardağı su veya tavuk suyu",
            "Tuz, karabiber"
        ],
        "yapilis": [
            "Soğanı yemeklik doğrayıp tencerede yağ ile kavurun, rendelenmiş havucu ekleyin.",
            "Unu ve salçayı ekleyip kısaca karıştırın.",
            "Yıkanmış mercimek ve suyu ekleyip mercimekler yumuşayana kadar pişirin.",
            "Blenderdan geçirip pürüzsüz hale getirin, gerekirse kıvamını ayarlayın, tuz-karabiber ekleyip servise hazır hale getirin."
        ]
    },
    {
        "ad": "Meyhane Pilavı",
        "resim": "meyhn_plv",
        "malzemeler": [
            "1 su bardağı pilavlık bulgur",
            "1 orta boy soğan",
            "2 adet sivri biber",
            "1 adet küçük boy kapya biber",
            "2 orta boy domates",
            "1 yemek kaşığı domates salçası",
            "1 tatlı kaşığı tuz",
            "Sıvı yağ"
        ],
        "yapilis": [
            "Tencerede kıyılmış soğanı yağ ile pembeleşinceye kadar kavurun ve salça ekleyin.",
            "Küp küp doğranmış domates, sivri ve kapya biberleri ilave edin.",
            "Bulguru ekleyip hepsini birlikte bir iki dakika daha kavurun.",
            "Tuz ve 2 bardak sıcak suyu ekleyip kaynamaya bırakın.",
            "Kaynadıktan sonra ocağın ateşini kısıp tencerenin kapağını sıkıca kapatarak suyunu çekene kadar pişirin.",
            "Ocaktan alıp 10 dakika dinlendirdikten sonra karıştırıp servis edin."
        ]
    },
    {
        "ad": "Karnıyarık",
        "resim": "karnyark",
        "malzemeler": [
            "5 adet orta boy patlıcan",
            "300 g kıyma",
            "1 adet soğan",
            "2 diş sarımsak",
            "2 adet domates",
            "2 yemek kaşığı salça",
            "Tuz, karabiber, sıvı yağ"
        ],
        "yapilis": [
            "Patlıcanları alacalı soyup ortadan uzunlamasına yarın, tuzlu suda biraz bekletip kurulayın ve kızgın yağda kızartın veya fırında fırınlayın.",
            "Soğan ve sarımsağı doğrayıp kavurun, kıymayı ekleyip pişirin, salça ve doğranmış domatesleri ekleyip kıvam alana kadar pişirin; tuz ve karabiber ekleyin.",
            "Kızarmış patlıcanların ortasını açıp kıymalı harcı yerleştirip fırın tepsisine dizin, üzerlerine domates dilimi koyup 180°C’de 15–20 dakika pişirin.",
            "Sıcak servis edin."
        ]
    },
    {
        "ad": "Sütlaç",
        "resim": "sutlac",
        "malzemeler": [
            "1 litre süt",
            "1 çay bardağı pirinç",
            "1 su bardağı toz şeker",
            "1 yemek kaşığı nişasta (isteğe bağlı kıvam için)",
            "Tarçın (servis için)"
        ],
        "yapilis": [
            "Pirinçleri yıkayıp su ile yumuşayana kadar haşlayın.",
            "Sütü ekleyip kaynatın, şekerini ekleyip birkaç dakika daha pişirin.",
            "İsterseniz nişastayı az su ile açıp ekleyip kıvamını ayarlayın.",
            "Kaselere paylaştırıp soğuttuktan sonra tarçınla veya fındıkla servis edin."
        ]
    }
]
# Kitap uygulamasındaki'kapak' değişkeni ile aynı mantık
mevcut_tarif_no = 0


pencere = Tk()
pencere.title("Tarif Kitabı")
pencere.geometry("500x750") # Pencereyi biraz büyüttüm

# --- 3. Widget'ları (Etiketleri) BİR KEZ Oluşturma ---
# Bu etiketler başta boş olacak, goster() fonksiyonu içlerini dolduracak

ana_baslik = Label(pencere, text="Yemek Tarifleri", font=("Times New Roman", 28, "bold"))
ana_baslik.grid(row=0, column=0, padx=10, pady=10)

tarif_baslik_label = Label(pencere, text="", font=("Times New Roman", 22, "bold"), fg="blue")
tarif_baslik_label.grid(row=1, column=0, padx=10, pady=5)


gorsel_label = Label(pencere)
gorsel_label.grid(row=2, column=0, padx=10, pady=10)

# Malzemeler Başlığı (Sabit)
Label(pencere, text="Malzemeler", font=("Times New Roman", 16, "underline")).grid(row=3, column=0, pady=(10,0))

# Değişecek olan malzeme listesi
malzemeler_label = Label(pencere, text="", font=("Times New Roman", 12), justify=LEFT)
malzemeler_label.grid(row=4, column=0, padx=10, pady=5)

# Talimatlar Başlığı (Sabit)
Label(pencere, text="Hazırlanışı", font=("Times New Roman", 16, "underline")).grid(row=5, column=0, pady=(10,0))

# Değişecek olan talimat listesi
talimatlar_label = Label(pencere, text="", font=("Times New Roman", 12), justify=LEFT)
talimatlar_label.grid(row=6, column=0, padx=10, pady=5)

# --- 4. Fonksiyonlar ---

def goster():
    tarif = tarifler[mevcut_tarif_no]

    # Başlığı değiştir
    tarif_baslik_label.config(text=tarif['ad'])

    # Malzemeleri metin haline çevir
    malzemeler_label.config(text="\n".join(tarif['malzemeler']))

    # Yapılışı metin haline çevir
    talimatlar_label.config(text="\n".join(tarif['yapilis']))

    # Görseli göster
    try:
        img = Image.open(f"{tarif['resim']}.png")  # veya jpg, resimlerin uzantısına göre
        img = img.resize((400, 300), Image.LANCZOS)
        gorsel = ImageTk.PhotoImage(img)
        gorsel_label.config(image=gorsel, text="")
        gorsel_label.image = gorsel
    except FileNotFoundError:
        gorsel_label.config(image=None, text=f"Resim bulunamadı:\n{tarif['resim']}")


# 🔽 BURAYA EKLE — goster()’ın hemen altına
def sonraki():
    global mevcut_tarif_no
    mevcut_tarif_no = (mevcut_tarif_no + 1) % len(tarifler)
    goster()


    
    # Tarifler arasında gezinebilmek için... 

# --- 5. Buton ve Başlatma ---

# Sizin butonunuzla aynı
buton = Button(text="Sonraki Tarif", command=sonraki)
buton.grid(row=7, column=0, padx=10, pady=20)
buton.config(font=("Times New Roman", 20))

# Program başladığında ilk tarifi göster
goster()

pencere.mainloop()
