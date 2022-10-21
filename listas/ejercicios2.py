# EJECICIOS VISTAS

# Métodos propios

lista = [45, 32, 3, 78]
print("Lista original:", lista)
# función append: añada un elemento a la lista
lista.append(995)
lista.append(7)
print("Lista despues de usar append: * , lista")
# Función sort: ordena la lista
lista.sort() 
print("Lista ordenada: ", lista)
# Función reverse: invierte el orden de la lista
lista.reverse()
print("Lista al revés: ", lista)
# Función extend: añade los elementos de una lista a la lista 
lista_extend = [1,5,87,45]
lista.extend(lista_extend)
print("Lista despues de extend: ", lista)
# Función count: cuenta el número de veces que aparece el eelemento indicado como parametro dentro de la lista
print("Número de elementos 45: ", lista.count(45))
# Función insert: añade el elemento pasado como parámetro a la lista en la posición indicada también por parámetro
lista.insert(4,111)
print("Lista después de insert: ", lista)
# Función remove: elimina la primera ocurrencia empezando por la izquierda de la lista del elementos indicado como parámetro.
lista.remove(45)
print("Lista despues de remove: ",lista)
# Función index: devulve la posición de la primera ocurrencia de izquierda a derecha en la lista del elemnto pasado como parámetro
print("posición del elemento 111: ", lista.index(111))
# Función pop: Elimina el ultimo elemento de la lista y lo devuelve como resultado de la operación
lista.pop()
print("Lista despues de pop: ", lista)
# Función clear: elimina todos los elementos de la lista
lista.clear()
print("Lista despues de clear: ", lista)
