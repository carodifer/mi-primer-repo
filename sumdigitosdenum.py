def sumadigitos(n):
    suma = 0
    while n > 0:
        ultimo_digito = n % 10
        suma += ultimo_digito
        n = n // 10
    return suma
numero = int(input("Ingresa un número para sumar sus dígitos: "))
resultado = sumadigitos(numero)
print(f"La suma de los dígitos de {numero} es {resultado}.")