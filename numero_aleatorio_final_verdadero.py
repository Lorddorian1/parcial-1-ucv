print("Este programa solicita un numero N, con el cual se generará un número aleatorio por la tecnica de cuadrado medio.")

numero_N = input("Por favor, ingrese un número para generar su cifra aleatoria: ")
cifras_de_N = len(str(numero_N))
contador = 3
if numero_N.isdigit() == True:
    while cifras_de_N < 4:
        print("Ha ingresado un valor inadecuado para N.")
        nuevo_numero_N = input("Por favor, ingrese un número de al menos 4 cifras: ")
        numero_N = nuevo_numero_N
        cifras_de_N = len(str(numero_N))
        if cifras_de_N < 4:
            contador -= 1
            if contador == 0:
                break

numero_N = int(numero_N)
cuadrado_N = (numero_N)**2
print(f"El cuadrado de su número es: {cuadrado_N}")
string_cuadrado_N = str(cuadrado_N)   #Es necesario convertir el cuadrado en string para poder extraer los valores medios.
cifras_del_cuadrado_N = int(len(string_cuadrado_N))  #Y acá se evalúa el número de elementos que tiene.
continuar = True
while continuar == True:
    if cifras_del_cuadrado_N % 2 == 0:
        mitad_cifras_N = cifras_de_N//2
        mitad_cifras_cuadrado_N = cifras_del_cuadrado_N//2
        primer_valor_frontera = mitad_cifras_cuadrado_N-mitad_cifras_N
        segundo_valor_frontera = mitad_cifras_cuadrado_N+mitad_cifras_N
        numero_aleatorio = string_cuadrado_N[primer_valor_frontera: segundo_valor_frontera]
        numero_aleatorio = int(numero_aleatorio)
        print(f"Su número aleatorio es: {numero_aleatorio/10000:.4f}")
        respuesta = input("Desea usted generar un nuevo número aleatorio a partir del anterior? (s/n): ")
        continuar = respuesta.lower() in ["si", "sí"]
#Usar in en una lista, permite una consulta que devuelve valores booleanos.
#Es como verificar que ese valor existe dentro de esa lista; entonces la respuesta intuitiva será un sí o un no, que en programación sería True o False.
        if continuar == True:
            cuadrado_N = (numero_aleatorio)**2
            print(f"El cuadrado de su número es: {cuadrado_N}")
            string_cuadrado_N = str(cuadrado_N)
            cifras_del_cuadrado_N = int(len(string_cuadrado_N))
        else:
            print("¡Gracias por su prueba!")
            break
    else:
        mitad_cifras_N = cifras_de_N//2
        mitad_cifras_cuadrado_N = cifras_del_cuadrado_N//2
        primer_valor_frontera = (mitad_cifras_cuadrado_N-mitad_cifras_N)+1
        segundo_valor_frontera = (mitad_cifras_cuadrado_N+mitad_cifras_N)+1
        numero_aleatorio = string_cuadrado_N[primer_valor_frontera: segundo_valor_frontera]
        numero_aleatorio = int(numero_aleatorio)
        print(f"Su número aleatorio es: {numero_aleatorio/10000:.4f}")
        respuesta = input("Desea usted generar un nuevo número aleatorio a partir del anterior? (s/n): ")
        continuar = respuesta.lower() in ["si", "sí"]
        if continuar == True:
            cuadrado_N = (numero_aleatorio)**2
            print(f"El cuadrado de su número es: {cuadrado_N}")
            string_cuadrado_N = str(cuadrado_N)
            cifras_del_cuadrado_N = int(len(string_cuadrado_N))
        else:
            print("¡Gracias por su prueba!")
            break
else:
    raise ValueError("Debe ingresar un valor númerico.")