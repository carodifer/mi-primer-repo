N = int(input("Ingresa la cantidad de números triangulares que deseas imprimir: "))
for n in range(1, N + 1):
    triangular = n * (n + 1) // 2 
    print(triangular)