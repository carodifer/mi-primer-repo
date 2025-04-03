valor=int(input("Ingrese el valor de su producto: "))
if valor == 100:
    print ("Envio gratis")
elif (valor >= 50 and valor <= 100):
    print ("Costo de envio: 5$")
else:
    print ("Costo de envio: 10$")
