def bisiesto(año):
    if año % 4 == 0:
        if año % 100 == 0:
            if año % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
a = int(input("Ingresa un año para verificar si es bisiesto: "))
if bisiesto(a):
    print(f"{a} es un año bisiesto.")
else:
    print(f"{a} no es un año bisiesto.")