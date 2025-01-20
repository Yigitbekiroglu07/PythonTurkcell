# Hatalar

# ZeroDivisionError

a = 10
b = 0
a/b

try:
    print(a/b)
except ZeroDivisionError:
    print("Paydada sıfır olmaz.")
    
# Tip hatası

a = 10
b = "2"

a / b

try:
    print(a/b)
except TypeError:
    print("Sayı ve String Problemi")




    


