set1 = set([1, 3, 5])
set2 = set([1, 2, 3])
#Kesişim
set1.intersection(set2)
set2.intersection(set1)
#Kesişim2
kesisim = set1 & set2
kesisim
# Kümelerin Birleşimi
birlesim = set1.union(set2)
birlesim

set1.intersection_update(set2)
set1
