# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
print("Hola mundo!")

# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
#el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
#por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
#realizar la impresión por pantalla

Nombre = input ("Ingrese su nombre: ")
print(f"Hola {Nombre}!")

#3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
#imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
#"Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
#años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
#la impresión por pantalla.

nombre = input ("Ingrese su nombre: ")
apellido = input ("Ingrese su apellido: ")
edad = input ("Ingrese su edad: ")
pais = input ("Ingrese pais donde vive: ")

print(f"Soy {nombre} {apellido} tengo {edad} y vivo en {pais}")

#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
#su perímetro.
#Definir pi
pi = 3.14
#Pedir al usuario el radio del circulo
Radio = float(input("Ingrese radio: "))
#Definimos como calcular area
Area = pi*Radio**2
#Definimos como calcular perimetro
Perimetro = 2* Radio * pi
print (f"El area del circulo es: {Area}")
print (f"El perimetro del circulo es: {Perimetro}")


# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
#cuántas horas equivale.
Segundos = int(input("Ingrese la cantidad de segundos: "))
Horas = Segundos / 3600
print (f"Equivale a {Horas} horas")

#6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
#multiplicar de dicho número.
Numero = int(input("Ingresa un numero: "))
print(f"Tabla de multiplicar del {Numero}")
for i in range (1,11):
    print(f"{Numero}*{i}={Numero*i}")

#7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
#pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
Numero1 = int(input("Ingrese un numero distinto de 0: "))
Numero2 = int(input("Ingrese otro numero distinto de 0: "))

Suma = Numero1 + Numero2
Resta = Numero1 - Numero2
Multiplicacion = Numero1 * Numero2
Division = Numero1 / Numero2

print(f"El resultado de la suma de {Numero1} y {Numero2} es {Suma}")
print (f"El resultado de la resta entre {Numero1} y {Numero2} es {Resta}")
print(f"El resultado de la multiplicacion de {Numero1} y {Numero2} es {Division}")
print(f"El resultado de la division ente {Numero1} y {Numero2} es {Division}")

# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
#de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
#modo
Altura = float(input("Ingrese su altura en metros: "))
Peso = float(input("Ingrese su peso en kg: "))

IMC = Peso / Altura **2

print(f"Su IMC es: {IMC}")

#9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
#pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia
Temperatura_C = float(input("Ingrese temperatura en grados Celsius: "))
Temperatura_f = 9/5 * Temperatura_C + 32
print(f"La temperatura ingresada equivale en Fahrenheit: {Temperatura_f}")

#10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
#dichos números.
Numero1 = float(input("Ingrese el primer numero: "))
Numero2 = float(input("ingrese el segundo numero: "))
Numero3 = float(input("Ingrese el tercer numero: "))

Promedio = Numero1 + Numero2 + Numero3 / 3

print(f"El promedio entero los 3 numeros es de: {Promedio}")

