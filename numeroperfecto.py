def perfecto(n):
    if n <= 1:
        return False
    suma = 0
    for i in range(1, n):
        if n % i == 0:
            suma += i
    if suma == n:
        return True
    else:
        return False
numero = int(input("Ingresa un número para verificar si es perfecto: "))
if perfecto(numero):
    print(f"{numero} es un número perfecto.")
else:
    print(f"{numero} no es un número perfecto.")
