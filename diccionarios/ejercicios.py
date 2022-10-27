# EJERCICIOS DICCIONARIOS

# EJERCICIOS DE MAMIPULACIÓN

# 1. 
diassemanaigles = {"Lunes":"Monday",
"Martes":"Tuesday",
"Miercoles":"Wednesday",
"Jueves":"Thursday",
"Viernes":"Friday"}

print(diassemanaigles["Lunes"])
print(diassemanaigles["Miercoles"])
print(diassemanaigles["Viernes"])

# 2.
diassemanaigles = {"Lunes":"Monday",
"Martes":"Tuesday",
"Miercoles":"Wednesday",
"Jueves":"Thursday",
"Viernes":"Friday"}

print(diassemanaigles)
diassemanaigles["Sabado"] = "Saturday"
print(diassemanaigles)
diassemanaigles["Domingo"] = "Sunday"
print(diassemanaigles)
diassemanaigles["Lunes"] = "MondayBORRAR"
print(diassemanaigles)
del diassemanaigles["Lunes"]
print(diassemanaigles)

# 3.
diassemanaingles = {"Lunes" : "Monday",
"Martes":"Tuesday",
"Miercoles":"Wednesday",
"Jueves":"Thursday",
"Viernes":"Friday"}

print("Número de elementos del diccionarios: ",len(diassemanaingles))
print("Elemento mayor del diccionario: ",max(diassemanaingles))
print("Elemento menor del diccionario: ",min(diassemanaingles))