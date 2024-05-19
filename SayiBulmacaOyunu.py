print("""
      Sayı Bulmaca Oyunu...............!
      """)
import random
a=random.randint(0,100)
while True:
    b=int(input("Bir değer giriniz:"))
    if a<b:
        print("a b'den küçüktür")
    if b<a:
        print("a b'den büyüktür")
    if a==b:
        print("Tebrikler kazandınız")
        break
