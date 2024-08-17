urun_kaydi = dict()

def urun_ekle(x):
    print("***ÜRÜN KAYDI PROGRAMI***")
    urun_adi = input("Ürün Adı giriniz: ")
    urun_seri_no = input("Ürün Seri Numarası gir: ")
    x = urun_kaydi.setdefault(urun_adi,urun_seri_no)
    print(f"{urun_adi} kaydi yapılmıştır.!")
    input("devam edilsinmi?")

def urun_stok_bilgisi(x):
    stok_bilgisi = len(urun_kaydi)
    print(f"Stok'ta bulunan ürün sayısı: {stok_bilgisi}")
    for i,j in urun_kaydi.items():
        print(f"{i}:{j}")
    input("devam edilsinmi?")

def urun_sil(x):
    print("Stok silme ekranında bulunmaktasınız.!")
    stok_urun_sil = input("Sileceğiniz ürünü giriniz: ")
    if stok_urun_sil in urun_kaydi:
        urun_kaydi.pop(stok_urun_sil)
        print(f"{stok_urun_sil} stoktan silinmiştir.!")
    else:
        print(f"{stok_urun_sil} stokta bulunamadı.!")
    input("devam edilsinmi?")
while True:
    print("1-Ürün Ekle:\n2-stok göster\n3-Ürün sil\n4-Çıkış yapmak için 'q' bas")
    secim_yap = input("değer giriniz: ")
    if secim_yap == "1":
        urun_ekle(urun_kaydi)
    elif secim_yap == "2":
        urun_stok_bilgisi(urun_kaydi)
    elif secim_yap == "3":
        urun_sil(urun_kaydi)
    elif secim_yap == "q":
        print("Çıkış yapılıyor.")
        break
    else:
        print("Geçersiz değer girdiniz lütfen geçerli değer giriniz.!")

    # Sözlük verisini dosyaya kaydetme 
    with open("Dosya_adi.txt","w",encoding="utf-8") as f:
        for urun_adi, urun_seri_no in urun_kaydi.items():
            f.write(f"{urun_adi} : {urun_seri_no}\n")

    # Dosyadan okuma ve ekrana yazdırma
    with open("Dosya_adi.txt","r", encoding="utf-8") as f:
        print(f.read())
