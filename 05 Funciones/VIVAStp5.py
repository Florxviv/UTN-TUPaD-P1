#Ejercicio 1
def imprimir_hola_mundo():
    print('Hola Mundo!')
imprimir_hola_mundo()
#Ejercicio 2
nombre = input('Ingrese su nombre: ')
def saludar_usuario(nombre):
    print(f'Hola {nombre}!')
saludar_usuario(nombre)
#Ejercicio 3
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido:  ")
edad = int(input("Ingrese su edad:  "))
residencia = input("Ingrese su lugar de residencia: " )
def informacion_personal(nombre,apellido,edad,residencia):
    print(f"Soy {nombre} {apellido},tengo {edad} y vivo en {residencia}.")
informacion_personal(nombre,apellido,edad,residencia)
#Ejercicio 4
radio = float(input("Ingrese el radio del circulo: "))
pi = 3.14159
def area_circulo(radio):
    pi = 3.14159
    area = pi * (radio ** 2)
    return area
def perimetro_circulo(radio):
    pi = 3.14159
    perimetro = 2 * pi * radio
    return perimetro    
print(f"El area del circulo es: {area_circulo(radio)}")
print(f"El perimetro del circulo es: {perimetro_circulo(radio)}")
#Ejercicio 5
segundo = int(input("Ingrese los segundos: "))
def segundos_a_horas(segundos):
    horas = segundos // 3600
    return horas
print(f"{segundo} segundos son {segundos_a_horas(segundo)} horas")
#Ejercicio 6
numero = int(input("Ingrese un número: "))
def tabla_de_multiplicar(numero):
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}") 
tabla_de_multiplicar(numero)
#Ejercicio 7
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "No se puede dividir por cero"
    
    return (suma, resta, multiplicacion, division)

# Solicitar números al usuario
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))

# Obtener los resultados
resultados = operaciones_basicas(a, b)

# Mostrar los resultados de forma clara
print(f"\nResultados de las operaciones entre {a} y {b}:")
print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicación: {resultados[2]}")
print(f"División: {resultados[3]}")
#Ejercicio 8
def calcular_imc(peso,altura):
    imc = peso/(altura**2)
    return imc
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
print(f"Su IMC es: ", calcular_imc(peso,altura))
#Ejercicio 9
temperatura_c = float(input("Ingrese la temperatura en Celsius: "))
def celsus_a_fahrenheit(temperatura_c):
    return (temperatura_c * 9/5) + 32
print(f"La temperatura en Fahrenheit es: {celsus_a_fahrenheit(temperatura_c)}")
#Ejercicio 10
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

# Solicitar números al usuario
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
c = float(input("Ingrese el tercer número: "))

# Calcular el promedio
promedio = calcular_promedio(a, b, c)

# Mostrar el resultado
print(f"El promedio de {a}, {b} y {c} es: ", promedio)