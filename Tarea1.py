import random
import timeit
from faker import Faker

fake = Faker()

class Usuario:
    def __init__(self, user_id, nombre, edad):
        self.id = user_id
        self.nombre = nombre
        self.edad = edad

#Generar 100,000 usuarios con datos aleatorios
#Cada usuario tiene un ID único (del 1 al 100,000), un nombre aleatorio y una edad aleatoria del 18 al 86
usuarios = [Usuario(i, fake.name(), random.randint(18, 86)) for i in range(1, 100001)]

#Función búsqueda lineal: recorre la lista de usuarios hasta encontrar el ID objetivo
def busqueda_lineal(lista, objetivo):
    for usuario in lista:
        if usuario.id == objetivo:
            return usuario.nombre  #Devuelve el nombre del usuario si lo encuentra
    return -1

#Función búsqueda binaria: parte la lista en dos para encontrar el id objetivo
def busqueda_binaria(lista, objetivo):
    izquierda, derecha = 0, len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio].id == objetivo:
            return lista[medio].nombre  #Devuelve el nombre del usuario si lo encuentra
        elif lista[medio].id < objetivo:
            izquierda = medio + 1  #Buscar en la mitad derecha
        else:
            derecha = medio - 1  #Buscar en la mitad izquierda
    return -1


id_prueba = int(input("Ingrese el ID del usuario: "))

tiempo_lineal = timeit.timeit(lambda: busqueda_lineal(usuarios, id_prueba), number=1)

tiempo_binaria = timeit.timeit(lambda: busqueda_binaria(usuarios, id_prueba), number=1)

#Imprimir los resultados de la búsqueda
print("*------- BUSCANDO -------*")
nombre_lineal = busqueda_lineal(usuarios, id_prueba)
nombre_binaria = busqueda_binaria(usuarios, id_prueba)

if nombre_lineal != -1:
    print(f"Usuario encontrado con búsqueda lineal: {nombre_lineal}")
else:
    print("Usuario no encontrado con búsqueda lineal.")

if nombre_binaria != -1:
    print(f"Usuario encontrado con búsqueda binaria: {nombre_binaria}")
else:
    print("Usuario no encontrado con búsqueda binaria.")

#Imprimir los tiempos de ejecución
print(f"Tiempo de búsqueda lineal: {tiempo_lineal:.6f} segundos")
print(f"Tiempo de búsqueda binaria: {tiempo_binaria:.6f} segundos")
