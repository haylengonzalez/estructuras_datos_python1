# EJECICIOS VISTAS

# EJERCICIOS MANIPULACIÓN

# 1. Consiste en la definición de una lista con elementos de diferentes tipos y en mostrarla por pantalla, tanto entera como por elementos accediendo ala posición que ocupa dentro dela lista.
lista = ["Python", "Gaunenta", 2022, "Libro",]
print (lista)
print (lista[0])
print(lista[2])

# 2. Consiste en el uso del operador + para realizar uniones de listas. Además la función len para conocer el número de elementos que componen la lista.
lista1 = ["Camiseta", "Pantalon", "Zapatillas"]
lista2 = ["Abrigo", "Jersey", "Sudadera", "Calcetines"]
print("Número elementos lista1: ", len(lista1))
print("lista1:", lista1)
print("Número elementos lista2: ", len(lista2))
print("lista2: ", lista2)
lista_concatenada = lista1 + lista2
print("Número elementos lista concatenada: ", len(lista_concatenada))
print("lista_concatenada: ", lista_concatenada)

# 3. Añadir elementos a la lista de diferentes formas 
lista1 = ["Camiseta", "Pantalon", "Zapatillas"]
print(lista)
lista = lista + ["Abrigo"]
print(lista)
lista = lista + ["Jersey", "Sudadera"]
print(lista)
lista = lista + ["Calcetines"] + ["Bufanda"]
print(lista)

# 4. Modificar elementos de una lista y borrar elementos de la misma 
lista1 = ["Camiseta", "Pantalon", "Zapatillas"]
print(lista)
lista[1] = "Cazadora"
print(lista)
del lista[0]
print(lista)


# 5. Uso del operador *. Permite concatenar uan lista con ella misma un número finito de veces.
lista1 = ["Camiseta", "Pantalon", "Zapatillas"]
print(lista)
lista_resultante = lista*  3
print(lista_resultante)

# 6.Creación de listas como elementos de listas y acceso a dichos elementos.
print("-----Ejercicio 6----")
lista = ["Camiseta", ["Calcetices", "Cazadores"], "Zapatillas"]
print(lista) 
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[1][0])
print(lista[1][1])

# 7. Extraer una porción de la lista en una lista nueva.
print("-----Ejercicio 7----")
lista = [1,2,3,4,5,6,7,8,9]
print(lista)
lista1 = lista[3:7]
print(lista1)
lista2 = lista[:5]
print(lista2)
lista3 = lista[6:]
print(lista3)
