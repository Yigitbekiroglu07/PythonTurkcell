# Örnek Metodları
class VeriBilimci(): #Bir sınıf tanımlandı 
    calisanlar = [] # Çalışanlar nesnesi oluşturuldu.
    def __init__(self): # Değişecek özellikler tanımlandı
        self.bildigi_diller = []
        self.bolum = ''
    def dil_ekle(self,yeni_dil): # Değişecek özellikler tanımlandı
        self.bildigi_diller.append(yeni_dil)
    
ali = VeriBilimci()
ali.bildigi_diller
ali.bolum

veli = VeriBilimci()
veli.bildigi_diller
veli.bolum

ali.dil_ekle("R")
ali.bildigi_diller

veli.dil_ekle("Python")
veli.bildigi_diller