numeros = [23, 45, 67, 12, 89, 34, 56, 78, 9, 54] 
print ("Esta es la lista de numeros aleatorios: ", numeros)
mayor = numeros[0]  
i = 1 
while i < len(numeros):
    if numeros[i] > mayor:
        mayor = numeros[i]
    i += 1
print("El mayor número es:", mayor)
