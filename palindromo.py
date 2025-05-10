def palindromo(texto):
    sinespacios = ""
    for letra in texto:
        if letra != " ":
            sinespacios += letra
    contador = 0
    for letra in sinespacios:
        contador += 1
    alreves = ""
    i = contador - 1
    while i >= 0:
        alreves += sinespacios[i]
        i -= 1
    if sinespacios == alreves:
        return True
    else:
        return False
frase = input("Ingresa una frase para verificar si es un palíndromo (sin importar espacios o mayusculas): ")
if palindromo(frase):
    print("Es un palíndromo.")
else:
    print("No es un palíndromo.")