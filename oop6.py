# Miras Yapıları
class Employees():
    def __init__(self): # Değişecek özellikler tanımlandı
        self.FirstName = ""
        self.LastName = ""
        self.Address = ""

class DataScience(Employees):
    def __init__(self): # Değişecek özellikler tanımlandı
        self.Programming = ""

veribilimci1 = DataScience()
veribilimci1.FirstName

class Marketing(Employees):
    def __init__(self): # Değişecek özellikler tanımlandı
        self.StoryTelling = ""
        
mar1 = Marketing()
mar1.LastName
mar1.StoryTelling