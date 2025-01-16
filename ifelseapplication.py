# Uygulama: if ve input ile Kullanıcı Etkileşimli Program
sinir = 50000
magaza_adi = input("Mağaza adı nedir?")
gelir = int(input("Gelirinizi giriniz"))

if gelir > sinir:
    print("Tebrikler:" + magaza_adi + " promosyon kazandınız!")

elif gelir < sinir:
    print("Uyarı! Çok düşük gelir:" + str(gelir))
    
else:
    printf("Takibe devam")