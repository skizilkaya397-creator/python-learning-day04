import random
sayi=random.randint(1,100)
tahmin_listesi=[]
while True:
    tahmin=int(input("1 ile 100 arasında bir sayı tahmin edin: "))
    if tahmin>100 or tahmin<1:
        print("Lütfen 1 ile 100 arasında bir sayı girin")
        continue
    tahmin_listesi.append(tahmin)
    if tahmin<sayi:
        print("Daha büyük bir sayı söyleyin")
    elif tahmin>sayi:
        print("Daha küçük bir sayı söyleyin")
    else:
        print("Tebrikler doğru tahmin ettiniz")
        print(len(tahmin_listesi),"tahminde bildiniz")
        break 
        