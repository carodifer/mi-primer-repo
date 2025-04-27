n = 2  
contador = 0  
primos = []  
while contador < 20:
    numprimo = True  
    i = 2
    while i < n:
        if n % i == 0: 
            numprimo = False
            break
        i += 1
    if numprimo:
        primos += [n]  
        contador += 1
    n += 1
print(primos)