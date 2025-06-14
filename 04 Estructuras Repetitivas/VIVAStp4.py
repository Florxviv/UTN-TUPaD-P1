# Ejercicio 1
for i in range(101):  # range(101) genera números desde 0 hasta 100 inclusive.
    print(i)

# Ejercicio 2
# Solicitar al usuario un número entero
numero = input("Por favor, ingrese un número entero: ")

# Calcular la cantidad de dígitos
cantidad_digitos = len(numero)

# Mostrar el resultado
print(f"El número ingresado tiene {cantidad_digitos} dígitos.")

# Ejercicio 3
# Solicitar los dos valores al usuario
valor1 = int(input("Ingrese el primer valor: "))
valor2 = int(input("Ingrese el segundo valor: "))

# Determinar el rango excluyendo los valores dados
if valor1 < valor2:
    rango = range(valor1 + 1, valor2)  # Excluye valor1 y valor2
else:
    rango = range(valor2 + 1, valor1)  # Excluye valor2 y valor1

# Calcular la suma de los números en el rango
suma = sum(rango)

# Mostrar el resultado
print(f"La suma de los números entre {valor1} y {valor2}, excluyendo ambos, es: {suma}")

# Ejercicio 4
# Inicializar el acumulador de la suma
total = 0

print("Ingrese números enteros para sumar. Ingrese 0 para detener el programa.")

while True:
    # Solicitar un número al usuario
    numero = int(input("Ingrese un número: "))
    
    # Verificar si el número es 0
    if numero == 0:
        break  # Terminar el bucle si el usuario ingresa 0
    
    # Agregar el número al total
    total += numero


print(f"El total acumulado es: {total}")

# Ejercicio 5
import random

# Generar un número aleatorio entre 0 y 9
numero_secreto = random.randint(0, 9)
intentos = 0

print("¡Bienvenido al juego de adivinanza!")
print("Estoy pensando en un número entre 0 y 9. ¿Puedes adivinar cuál es?")

while True:
    try:
        adivinanza = int(input("Introduce un número: "))
        intentos += 1

        if adivinanza == numero_secreto:
            print(f"¡Felicidades! Has acertado el número en {intentos} intentos.")
            break
        else:
            print("Incorrecto, intenta de nuevo.")
    except ValueError:
        print("Por favor, introduce un número válido.")

#Ejercicio 6
# Imprimir números pares entre 100 y 0 en orden decreciente
for numero in range(100, -1, -2):
    print(numero)

#Ejercicio 7
# Solicitar al usuario un número entero positivo
while True:
    try:
        limite = int(input("Introduce un número entero positivo: "))
        if limite >= 0:
            break
        else:
            print("Por favor, introduce un número positivo.")
    except ValueError:
        print("Entrada no válida. Debes introducir un número entero.")

# Calcular la suma de todos los números desde 0 hasta el número indicado
suma_total = sum(range(limite + 1))

# Mostrar el resultado
print(f"La suma de los números entre 0 y {limite} es: {suma_total}")

#Ejercicio 8
# Inicialización de contadores
pares = 0
impares = 0
positivos = 0
negativos = 0

print("Ingresa 100 números enteros:")

# Pedir 100 números al usuario
for _ in range(100):
    while True:
        try:
            numero = int(input("Introduce un número: "))
            break
        except ValueError:
            print("Entrada no válida. Por favor, introduce un número entero.")

    # Contar pares e impares
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    
    # Contar positivos y negativos
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

# Mostrar resultados
print("\nResultados:")
print(f"Números pares: {pares}")
print(f"Números impares: {impares}")
print(f"Números positivos: {positivos}")
print(f"Números negativos: {negativos}")

#Ejercicio 9
# Inicialización de variables
suma = 0
cantidad_numeros = 100

print("Ingresa 100 números enteros:")

# Bucle para pedir 100 números
for _ in range(cantidad_numeros):
    while True:
        try:
            numero = int(input("Introduce un número: "))
            suma += numero  # Sumar el número ingresado
            break
        except ValueError:
            print("Entrada no válida. Por favor, introduce un número entero.")

# Calcular la media
media = suma / cantidad_numeros

# Mostrar el resultado
print(f"\nLa media de los números ingresados es: {media}")
#Ejercicio 10
numero = input("Introduce un numero: ")
numero_invertido = numero[::-1]
print(f"El numero invertido es {numero_invertido}")