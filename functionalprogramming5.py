# Map, filter ve reduce Fonksiyonları

#Map
liste = [1,2,3,4,5]

list(map(lambda x: x*10, liste))

#Filter
liste = [1,2,3,4,5,6,7,8,9,10]
list(filter(lambda x: x % 2 == 0, liste))

#reduce
from functools import reduce
liste = [1,2,3,4,5]
reduce(lambda a,b: a+b, liste)

