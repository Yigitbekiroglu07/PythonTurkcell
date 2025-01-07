# Set Sorgu İşlemleri
set1 = set([7, 8, 9])
set2 = set([5, 6, 7, 8, 9, 10])

# İki kümenin kesişiminin boş olup olmadığının sorgulanması
set1.isdisjoint(set2)

# Bir kümenin bütün elemanlarının başka bir küme içerisinde yer alıp almadığı
set1.issubset(set2)

# Bir kümenin diğer kümeyi kapsayıp kapsamadığı
set2.issuperset(set1)