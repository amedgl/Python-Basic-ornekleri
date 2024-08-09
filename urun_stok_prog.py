urun_kaydi = dict()

def urun_ekle(x):
    print("***ÜRÜN KAYDI PROGRAMI***")
    urun_adı = input("Ürün Adı giriniz: ")
    urun_seri_no = input("Ürün Seri Numarası gir: ")
    x = urun_kaydi.setdefault(urun_adı,urun_seri_no)
    print(f"{urun_adı} kaydı yapılmıştır..")
    input("devam edilsinmi?")

def urun_stok_bilgisi(x):
    sutuk_bilgisi = len(x)
    print(f"stok'ta bulunan ürün sayısı:{sutuk_bilgisi}")
    for i,j in x.items():
        print(i,":",j)
    input("devam edilsinmi?")

def urun_sil(x):
    print("stok silme ekranında bulunmaktasınız.")
    stok_urun_sil = input("sileceğiniz ürünü giriniz:")
    x = urun_kaydi.pop(stok_urun_sil)
    input("devam edilsinmi?")

while True:
    print("***ÜRÜN STOK PROGRAMINA HOŞ GELDİNİZ***")
    secim_yap = input("1-Ekle\n2-bilgi\n3-sil\n4-çıkış yapmak için 'q' bas.\nseçim yap: ")
    if secim_yap == "1":
        urun_ekle(urun_kaydi)
    elif secim_yap == "2":
        urun_stok_bilgisi(urun_kaydi)
    elif secim_yap == "3":
        urun_sil(urun_kaydi)
    elif secim_yap == "q":
        print("Çıkış yapılıyor...")
        break
    else:
        print("Girdiğiniz değer geçersizdir lütfen tekrar giriniz...")