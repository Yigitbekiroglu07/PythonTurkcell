# Vektörel Operasyonlar
#OOP
a = [1,2,3,4]
b = [2,3,4,5]

ab = []

range (0, len(a)) # 0 ile 4 arasında aralık

for i in range(0,len(a)): # 0-4 arasında gezsin ve çarpsın
    ab.append(a[i]*b[i])
    
ab

#Fp

import numpy as np # Numpy isimli kütüphnaeyi dahil etmek

a = np.array([1,2,3,4]) # np.array özel bir veri yapısıdır.
b = np.array([2,3,4,5]) #  # np.array özel bir veri yapısıdır.

a*b