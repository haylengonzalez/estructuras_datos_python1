# METODOS PROPIOS
# Funciones

# Copy: Realiza una copia exacta del diccionario en uno nuevo. Valor devuelto: diccionario copiado y parámetros no tiene.
diassemanaingles = {"Lunes" : "Monday",
"Martes":"Tuesday",
"Miercoles":"Wednesday",
"Jueves":"Thursday",
"Viernes":"Friday"}

print("Diccionario original: ",diassemanaingles)
diccionariocopia = diassemanaingles.copy()
print("Diccionario copy:",diccionariocopia)

# pop: obtiene el valor de la clave pasada comp parámetro y además elimina el elemento del diccionario. Valor devuelto: valor del elemento o erroe en caso de no encontrar la clave en el diccionario.
print("Valor de lunes (pop): ",diassemanaingles.pop("Lunes"))
print("Diccionario después del pop:",diassemanaingles)

# popitem: obtiene un elemento aleatorio del diccionario y lo elimina del mismo.
print("Elemento al azar con popitem: ",diassemanaingles.popitem())
print("Diccionariodespués del popitem: ",diassemanaingles)

# get: obtene el valor de la clave pasada como parámetro
print("Valor del Mastes (get): ",diassemanaingles.get("Martes"))
print("Valor del Lunes (get) (no existe): ",diassemanaingles.get("Lunes"))
print("Valor del Lunes (get) (no existe): ",diassemanaingles.get("Lunes","No existe"))

# update: realiza una actualización del diccionario utilizando otro diccionario. Aquellos elementos del diccionario que se utilizan para actualizar el pincipal sustituirán los existentes en el ismo y aquellos elementos que no existían serán aadidos al diccionario como nuevos elementos.
diassemanaingles.update({"Lunes":"MondayNUEVO","Martes":"TuesdayNUEVO"})
print("Diccionario después del update: ",diassemanaingles)

# setdefault: intenta insertar un elemento (clave y valor) en el diccionario.
print("setdefault del Sabado:",diassemanaingles.setdefault("Sabado","Saturday"))
print("Diccionario despues del setdefault (elemento existente): ",diassemanaingles)

# items
print("Elementos iterable (items): ",diassemanaingles.items())

# keys
print("Elemento iterable (claves): ",diassemanaingles.keys())

# values
print("Elemento iterable(valores): ",diassemanaingles.values ())

# clear
print("Diccionario después del clear: ",diassemanaingles.clear ())