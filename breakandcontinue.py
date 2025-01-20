# Break ve Continue

maaslar = [8000,5000,2000,1000,3000,7000,1000]
dir(maaslar)

maaslar.sort()
maaslar
# Break komutu belirtilen değerden sonrasını göstermez.
for i in maaslar:
    if i == 3000:
        print("kesildi")
        break
    print(i)
# Continue belirtilen değeri atlamak için kulllanılır.
for i in maaslar:
    if i == 3000:
        continue
    print(i)