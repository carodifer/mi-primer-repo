n = 2 
primos = [] 
for _ in range(100):  
    numprimo = True  
    for i in range(2, n):
        if n % i == 0:  
            numprimo = False
            break
    if numprimo:
        primos += [n]  
    if len(primos) == 20:  
        break
    n += 1  
print(primos)