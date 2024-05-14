print("*"*70)
print("Not Hesaplama programı.......!")
print("*"*70)
while True:
    def ortalamahesaplama(vize,final):
        vize=vize1*40/100
        final=final1*60/100
        ortalama=(vize+final)
        if (ortalama>=60 and final1>=60):
            print("*"*70)
            print(ortalama,"ile geçtiniz..")
        else:
            print("*"*70)
            print(ortalama,"ile kaldınız..")
    while True:
        vize1=int(input("Lütfen vize notunu giriniz:"))
        if vize1<0 or vize1>100:
            print("Lütfen geçerli bir değer giriniz..")
        else:
            break
    while True:    
        final1=int(input("lütfen Final notunu giriniz:"))
        if final1<0 or final1>100:
            print("Lütfen geçerli bir değer giriniz..")
        else:
            break
    ortalamahesaplama(vize1,final1)
    break