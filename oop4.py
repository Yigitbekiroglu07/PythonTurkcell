# Örnek Özellikleri
class VeriBilimci():
    bildigi_diller = ["R", "PYTHON"]
    bolum = ''
    sql = ''
    deneyim_yili = 0

    def __init__(self):
        self.bildigi_diller = []
        self.bolum = ''

ali = VeriBilimci()
print(ali.bildigi_diller)

veli = VeriBilimci()
print(veli.bildigi_diller)

ali.bildigi_diller.append("Python")
print(ali.bildigi_diller)

veli.bildigi_diller
veli.bildigi_diller.append("R")
veli.bildigi_diller

VeriBilimci.bildigi_diller
ali.bolum

VeriBilimci.bolum
ali.bolum = "İstatistik"
VeriBilimci.bolum
veli.bolum
veli.bolum = "end. müh"
veli.bolum
ali.bolum