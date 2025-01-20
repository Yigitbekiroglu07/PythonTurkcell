#Yan Etkisiz Fonksiyonlar Örnek 1
A = 5 #Global Değişken

def impure_sum(b): #Dışardaki değere bağlı olduğundan çıktı değişkenlik gösterir.
    return b + A

def pure_sum(a,b): #Bir girdi verildiğinde çıktı üretir.
    return a + b

impure_sum(6)
pure_sum(3, 4)