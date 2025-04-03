#Condicionales ejercicio
a = int(input("ingrese lado 1 del triangulo: "))
b = int(input("Ingrese lado 2 del triangulo: "))
c = int(input("Ingrese lado 3 del triangulo: "))
if (a + b > c and a + c > b and b + c > a):
    if (a==b==c):
        print ("El triangulo es equilatero")
    elif (a==b or b==c or a==c):
        print("El triangulo es isosceles")
    else:
        print ("El triangulo es escaleno")
else:
   print ("No es un triangulo")                                                                                                                                                                         
aaaaaaaa