""" este codigo calcula la suma de fibonacci impar"""
a, b = 1, 1
suma = 0
i = 1
while b < 1000000:
    a = b
    b = a + b
    
    if not (i%2 == 0) :
        suma += b   
        print b, i

    i += 1

print suma


