#Programa que determine el mayor de 3 numeros
num1 = float(input("Ingresa el primer numero: "))
num2 = float(input("Ingresa el segundo numero: "))
num3 = float(input("Ingresa el tercer numero: "))
if num1 > num2 and num1 > num3 :
    print("El primer numero ingresado es mayor")
elif num2 > num1 and num2 > num3 :
    print("El segundo numero ingresado es mayor")
else:
    print("El tercer numero ingresado es mayor")