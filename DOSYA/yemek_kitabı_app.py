from tkinter import *
from PIL import ImageTk, Image

# --- 1. Veri Yapısı ---
# Tarifleri bir liste içinde sözlük olarak tutalım
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
            "İstersen nişastayı az su ile açıp ekleyip kıvamını ayarlayın.",
            "Kaselere paylaştırıp soğuttuktan sonra tarçınla servis edin."
        ]
    }
]
# Sizin kodunuzdaki 'kapak' değişkeni ile aynı mantık
mevcut_tarif_no = 0

# --- 2. Pencere Kurulumu ---
pencere = Tk()
pencere.title("Tarif Kitabı")
pencere.geometry("500x750") # Pencereyi biraz büyüttüm

# --- 3. Widget'ları (Etiketleri) BİR KEZ Oluşturma ---
# Bu etiketler başta boş olacak, goster() fonksiyonu içlerini dolduracak

# Ana Başlık (Bu sabit kalacak)
ana_baslik = Label(pencere, text="Yemek Tarifleri", font=("Times New Roman", 28, "bold"))
ana_baslik.grid(row=0, column=0, padx=10, pady=10)

# Değişecek olan tarif başlığı
tarif_baslik_label = Label(pencere, text="", font=("Times New Roman", 22, "bold"), fg="blue")
tarif_baslik_label.grid(row=1, column=0, padx=10, pady=5)

# Değişecek olan görsel
# Başlangıçta boş bir Label
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
    # 1. Mevcut tarifi listeden al
    tarif = tarifler[mevcut_tarif_no]
    
    # 2. Etiketlerin içeriğini .config() ile GÜNCELLE
    
    # Başlığı güncelle
    tarif_baslik_label.config(text=tarif['baslik'])
    
    # Malzemeleri güncelle
    malzemeler_label.config(text=tarif['malzemeler'])
    
    # Talimatları güncelle
    talimatlar_label.config(text=tarif['talimatlar'])
    
    # Görseli güncelle
    try:
        # Resmi aç ve yeniden boyutlandır (tüm resimler aynı boyutta olsun)
        img = Image.open(tarif['gorsel_yolu'])
        img = img.resize((400, 300), Image.LANCZOS) # Boyutlandırma
        gorsel = ImageTk.PhotoImage(img)
        
        # Görsel etiketini güncelle
        gorsel_label.config(image=gorsel)
        gorsel_label.image = gorsel # Bu satır çok önemli! (Referansı tutar)
        
    except FileNotFoundError:
        # Resim bulunamazsa
        gorsel_label.config(image=None, text=f"Resim bulunamadı:\n{tarif['gorsel_yolu']}")
    except Exception as e:
        # Diğer hatalar için
        print(f"Hata: {e}")
        gorsel_label.config(image=None, text="Resim yüklenemedi")

# Sizin 'sonraki' fonksiyonunuzla birebir aynı mantık
def sonraki():
    global mevcut_tarif_no
    if mevcut_tarif_no < len(tarifler) - 1:
        mevcut_tarif_no += 1
    else:
        mevcut_tarif_no = 0
    print(mevcut_tarif_no)
    
    # Değişen 'mevcut_tarif_no'ya göre etiketleri güncelle
    goster()

# --- 5. Buton ve Başlatma ---

# Sizin butonunuzla aynı
buton = Button(text="Sonraki Tarif", command=sonraki)
buton.grid(row=7, column=0, padx=10, pady=20)
buton.config(font=("Arial", 20))

# Program başladığında ilk tarifi göster
goster()

pencere.mainloop()