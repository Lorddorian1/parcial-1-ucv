print("Este programa simula el ascenso de un caracol que durante el día sube por la pared de un pozo, pero al caer la noche cae un poco.")
#Se le pide al usuario que ingrese las variables de entrada
altura_pozo = float(input("Ingrese la profundidad medida en metros del pozo por el que el caracol cae: "))
distancia_de_ascenso = float(input("Ingrese la distancia que asciende el caracol durante el día en metros: "))
distancia_caida = float(input("Ingrese la distancia que resbala el caracol durante la noche en metros: "))
#Se establecen contadores para la distancia recorrida y los dias que tarde el caracol
distancia_total_recorrida = 0
dias = 0
#Se establece un ciclo while para repetir el bucle hasta que se satisfaga la condicion de distancia_total_recorrida = altura_pozo
if altura_pozo < 0 or distancia_de_ascenso < 0 or distancia_caida < 0:
    print("Por favor, ingrese valores positivos para las distancias.")
else:
    while distancia_total_recorrida < altura_pozo:
        dias += 1
        distancia_total_recorrida += distancia_de_ascenso
        if distancia_caida >= distancia_de_ascenso:
            print("El caracol no saldrá del pozo escalando.")
            break
        elif distancia_total_recorrida >= altura_pozo:
            print(f"El caracol tarda {dias} día(s) en salir del pozo.")
            break
        else:
            distancia_total_recorrida -= distancia_caida

