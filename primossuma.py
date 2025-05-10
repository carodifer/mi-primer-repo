def esprimo(n):
    if n < 2:
        return False
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i += 1
    return True
def sumaprimos(a, b):
    suma = 0
    if a > b:
        temp = a
        a = b
        b = temp
    for i in range(a, b + 1):
        if esprimo(i):
            suma += i
    return suma
inicio = int(input("Ingresa el primer número del rango: "))
fin = int(input("Ingresa el segundo número del rango: "))
resultado = sumaprimos(inicio, fin)
print(f"La suma de los números primos entre {inicio} y {fin} es: {resultado}")

