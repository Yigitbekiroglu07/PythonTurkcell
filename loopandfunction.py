# Döngü ve Fonksiyonların Birlikte Kullanımı


maaslar = [1000,2000,3000,4000,5000]


# maaşlara yüzde 20 zam için gerekli kodları yaz

def yeni_maas(x):
    print(x)
    
yeni_maas(4)

def yeni_maas(x):
    print(x*20/100+x)
    
    yeni_maas(1000)
    yeni_maas(2000)
    yeni_maas(3000)
    yeni_maas(4000)
    yeni_maas(5000)
    
for i in maaslar:
    yeni_maas(i)
    
    