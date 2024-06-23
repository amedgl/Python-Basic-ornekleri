while True:
    print("""
        1.Toplama işlemi
        2.Çıkarma işlemi
        3.Çarpma işlemi
        4.Bölme işlemi
    """)
    islem=int(input("işlem yapmak için lütfen bir değer giriniz:"))
    if islem==1:
        sayi1=float(input("1.değeri giriniz:"))
        sayi2=float(input("2.değeri giriniz:"))
        toplam=sayi1+sayi2
        print("işlem sonuçu:",toplam)
        cikmak=input("işlemden çıkmak istiyormusunuz? E/H:").upper()
        if cikmak=="E":
            break
        else:
            print("işlem devam ediliyor..!)
    elif islem==2:
        sayi1=float(input("1.değeri giriniz:"))
        sayi2=float(input("2.değeri giriniz:"))
        cikarma=sayi1-sayi2
        print("işlem sonuçu:",cikarma)
        cikmak=input("işlemden çıkmak istiyormusunuz? E/H:").upper()
        if cikmak=="E":
            break
        else:
            print("işlem devam ediliyor..!)
    elif islem==3:
        sayi1=float(input("1.değeri giriniz:"))
        sayi2=float(input("2.değeri giriniz:"))
        carpma=sayi1*sayi2
        print("Girdiğiniz değerlerin toplamı:",carpma)
        cikmak=input("işlemden çıkmak istiyormusunuz? E/H:").upper()
        if cikmak=="E":
            break
        else:
            print("işlem devam ediliyor..!)
    elif islem==4:
        sayi1=float(input("1.değeri giriniz:"))
        sayi2=float(input("2.değeri giriniz:"))
        bolme=sayi1/sayi2
        print("Girdiğiniz değerlerin toplamı:",bolme)
        cikmak=input("işlemden çıkmak istiyormusunuz? E/H:").upper()
        if cikmak=="E":
            break
        else:
            print("işlem devam ediliyor..!)
    else:
        print("Geçersiz değer girdiniz lütfen geçerli bir değer giriniz..!")
