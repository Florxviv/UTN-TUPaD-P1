#Ejercicio 1
multiples_4 = list(range(1, 101, 4))
print (multiples_4)

#Ejercicio 2
lista_Flor = ["Jazmin", "Orquidea", "Rosa", "Lirio", "Tulipan", "Girasol", "Amapola", "Margarita"]
lista_Flor_Posi = lista_Flor [6]
print(lista_Flor_Posi)

#Ejercicio 3
lista_v = []
lista_v.append(3)
lista_v.append("logitech")
print(lista_v)

#Ejercicio 4
animales = ["perro", "gato", "conejo", "pez"]
animales [1] = "loro"
animales [-1] = "oso"
print (animales)

#Ejercicio 5
numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)

# La funcion max(numeros) devuelve el valor mas alto de la lista o sea el numero 22. Luego numeros.remove elimina ese valor de la lista. Al final print(numeros) muestra la lista sin el numero 22.

#Ejercicio 6
numeros = list(range(10,31,5))
print(numeros[:2])

#Ejercicio 7
autos = ["sedan", "polo", "suran", "gol"]
autos [1:3] = ["siena", "cronos"]
print(autos)

#Ejercicio 8
dobles = []
dobles.append(5 * 2)
dobles.append(10 *2)
dobles.append(15 * 2)
print(dobles)

#Ejercio 9
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],
["agua"]]
compras[2].append("jugo")
indice_fideos = compras [1].index ("fideos")
compras [1] [indice_fideos] = "tallarines"
compras[0].remove("pan")
print(compras)

#Ejercicio 10
lista_anidada = [15,True,[25.5,57.9,30.6],False]
print(lista_anidada)