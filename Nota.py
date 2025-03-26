#Programa calificacion
nota = float(input("Ingresa tu nota (entre 0 y 100): "))
if nota < 0 or nota > 100 :
    print ("Nota fuera de rango.")
elif nota >= 90 :
    print ("Excelente calificacion :D")
elif nota >= 70 :
    print ("Aprobaste :)")
else:
    print ("Reprobaste :(")