## Este programa realiza una matriz de orden NxM dado por el usuario y lo organiza en zigzag horizontal

matrix = []
filas = int(input("Ingrese el número de filas N de su matriz: "))
columnas = int(input("Ingrese el número de columnas M de su matriz: "))

for i in range(filas):
    matrix.append([])
    for j in range(columnas):
            matrix[i].append(0)
contador = 1
for i in range(filas):
        if i % 2 == 0:
            for j in range(columnas):
                matrix[i][j] = contador
                contador += 1
        else:
             for j in reversed(range(columnas)):
                matrix[i][j] = contador
                contador += 1

for filas in matrix:   #Para mostrar el formato de matriz sin los corchetes, se usa esta configuración
    for element in filas:      #Este formato si da el formato acostumbrado de una matriz
        print(element, end=" ")
    print()