print("""
      ****************************************
      Not Ortalaması Hesaplama Programı
      ****************************************
      """)
while True:
    vize=float(input("Vize Notunu Giriniz:"))
    if vize<0 or vize>100 :
        print("Lütfen Geçerli Bir Değer Giriniz.....!")
    else:
        break
while True:
    final=float(input("Final Değerini Giriniz:"))
    if final<0 or final>100 :
        print("Lütfen Geçerli Bir Değer Giriniz.....!")
    else:
        break

Ortalama=(vize*40/100)+(final*60/100)
if Ortalama>=60 and final>=60:
    print("Geçme Durumunuz:",Ortalama)
else:
    print("Kalma Durumunuz:",Ortalama)