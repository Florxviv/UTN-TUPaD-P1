# Ejercicio 1 
# Solicitar la edad al usuario
edad = int(input("Por favor, ingresa tu edad: "))

# Verificar si el usuario es mayor de 18 años
if edad > 18:
    print("Es mayor de edad")
else:
    print("No es mayor de edad")


# Ejercicio 2
# Solicitar la nota al usuario
nota = int(input("Por favor, ingresa tu nota: "))

# Verificar la condición
if nota >= 6:
    print("Aprobado")  # Este mensaje aparece si la nota es 6 o superior.
else:
    print("Desaprobado")  # Este mensaje aparece si la nota es menor a 6.

# Ejercicio 3
# Solicitar al usuario ingresar un número
numero = int(input("Por favor, ingrese un número: "))

# Evaluar si el número es par usando el operador %
if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

# Ejercicio 4
# Solicitar la edad al usuario
edad = int(input("Por favor, ingresa tu edad: "))

# Determinar a qué categoría pertenece
if edad < 12:
    print("Niño/a")
elif 12 <= edad < 18:
    print("Adolescente")
elif 18 <= edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

# Ejercicio 5 
# Solicitar la contraseña al usuario
contraseña = input("Por favor, ingrese una contraseña: ")

# Evaluar la longitud de la contraseña usando len()
if 8 <= len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# Ejercicio 6 

from statistics import mean, median, mode

# Lista de números aleatorios
import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
# Calcular la media, la mediana y la moda
media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

# Determinar el tipo de sesgo
if media > mediana > moda:
    sesgo = "Sesgo positivo (a la derecha)"
elif media < mediana < moda:
    sesgo = "Sesgo negativo (a la izquierda)"
elif media == mediana == moda:
    sesgo = "Sin sesgo"
else:
    sesgo = "No se ajusta exactamente a los criterios de sesgo"

# Imprimir los resultados
print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")
print(f"Resultado: {sesgo}")

# Ejercicio 7 
# Solicitar una frase o palabra al usuario
frase = input("Ingresa una frase o palabra: ")

# Verificar si la última letra es una vocal
if frase[-1].lower() in "aeiou":
    frase_resultante = frase + "!"
else:
    frase_resultante = frase

# Imprimir el resultado
print("Resultado:", frase_resultante)

# Ejercicio 8 
# Solicitar al usuario que ingrese su nombre
nombre = input("Ingresa tu nombre: ")

# Mostrar las opciones disponibles
print("Selecciona una opción:")
print("1. Convertir el nombre a mayúsculas.")
print("2. Convertir el nombre a minúsculas.")
print("3. Convertir el nombre con la primera letra en mayúscula.")

# Solicitar al usuario que elija una opción
opcion = input("Ingresa el número de la opción deseada (1, 2 o 3): ")

# Realizar la transformación según la opción seleccionada
if opcion == "1":
    print("Resultado:", nombre.upper())
elif opcion == "2":
    print("Resultado:", nombre.lower())
elif opcion == "3":
    print("Resultado:", nombre.title())
else:
    print("Opción no válida. Por favor, elige 1, 2 o 3.")

# Ejercicio 9
# Solicitar al usuario que ingrese la magnitud del terremoto
magnitud = float(input("Ingresa la magnitud del terremoto: "))

# Clasificar la magnitud y determinar la categoría
if magnitud < 3:
    categoria = "Muy leve (imperceptible)"
elif 3 <= magnitud < 4:
    categoria = "Leve (ligeramente perceptible)"
elif 4 <= magnitud < 5:
    categoria = "Moderado (sentido por personas, pero generalmente no causa daños)"
elif 5 <= magnitud < 6:
    categoria = "Fuerte (puede causar daños en estructuras débiles)"
elif 6 <= magnitud < 7:
    categoria = "Muy fuerte (puede causar daños significativos)"
else:
    categoria = "Extremo (puede causar graves daños a gran escala)"

# Imprimir el resultado
print("La categoría del terremoto es:", categoria)

# Ejercicio 10 
# Solicitar información al usuario
hemisferio = input("¿En cuál hemisferio te encuentras? (N/S): ").strip().upper()
mes = input("Ingresa el mes del año (en formato numérico, ej: 1 para enero, 12 para diciembre): ").strip()
dia = input("Ingresa el día del mes: ").strip()

# Convertir mes y día a valores numéricos
mes = int(mes)
dia = int(dia)

# Determinar la estación según el hemisferio y la fecha
if hemisferio == "N":
    if (mes == 12 and dia >= 21) or (mes <= 3 and (mes < 3 or dia <= 20)):
        estacion = "Invierno"
    elif (mes == 3 and dia >= 21) or (mes <= 6 and (mes < 6 or dia <= 20)):
        estacion = "Primavera"
    elif (mes == 6 and dia >= 21) or (mes <= 9 and (mes < 9 or dia <= 20)):
        estacion = "Verano"
    else:
        estacion = "Otoño"
elif hemisferio == "S":
    if (mes == 12 and dia >= 21) or (mes <= 3 and (mes < 3 or dia <= 20)):
        estacion = "Verano"
    elif (mes == 3 and dia >= 21) or (mes <= 6 and (mes < 6 or dia <= 20)):
        estacion = "Otoño"
    elif (mes == 6 and dia >= 21) or (mes <= 9 and (mes < 9 or dia <= 20)):
        estacion = "Invierno"
    else:
        estacion = "Primavera"
else:
    estacion = "Hemisferio no válido. Por favor ingresa 'N' o 'S'."

# Imprimir el resultado
print("La estación en tu ubicación es:", estacion)