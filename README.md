# ALGORITMOS DE BUSQUEDA BINARIA Y LINEAL

Este proyecto genera 100,000 usuarios con datos aleatorios y permite buscar un usuario por su ID utilizando dos métodos: búsqueda lineal y búsqueda binaria. Además, compara los tiempos de ejecución de ambas búsquedas.

🤑 Características

* Generación de 100,000 usuarios con ID único, nombre aleatorio y edad aleatoria.

* Implementación de búsqueda lineal y búsqueda binaria.

* Comparación de tiempos de ejecución entre ambos métodos.

## 📌 Requisitos
Python instalado en tu sistema, también la biblioteca **Faker**:

```bash
pip install faker
```


## 🛠️ Explicación del Código
Se te pedirá ingresar un **ID de usuario** para buscar en la base de datos generada con faker.

✴️ Importar librerías que nos servirán para: generar números random, medir el tiempo de ejecución y generar datos falsos aleatoriamente.

```bash
import random
import timeit
from faker import Faker
fake = Faker() #inicializa la librería faker con variable fake
```

### 🔹 Generación de Usuarios
El código crea una lista de 100,000 usuarios con datos generados aleatoriamente ya definida una clase *Usuario*:
```python
class Usuario:
    def __init__(self, user_id, nombre, edad):
        self.id = user_id
        self.nombre = nombre
        self.edad = edad
usuarios = [Usuario(i, fake.name(), random.randint(18, 86)) for i in range(1, 100001)]
```
Cada usuario tiene:
- Un **ID único** (del 1 al 100,000).
- Un **nombre aleatorio** generado con la librería Faker.
- Una **edad aleatoria** entre 18 y 86 años.

### 🔹 Métodos de Búsqueda
#### 1️⃣ **Búsqueda Lineal** (O(n))
Recorre la lista uno por uno hasta encontrar el usuario:
```python
def busqueda_lineal(lista, objetivo):
    for usuario in lista:
        if usuario.id == objetivo:
            return usuario.nombre
    return -1
```

#### 2️⃣ **Búsqueda Binaria** (O(log n))
Divide la lista en mitades hasta encontrar el usuario (requiere una lista ordenada):
```python
def busqueda_binaria(lista, objetivo):
    izquierda, derecha = 0, len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio].id == objetivo:
            return lista[medio].nombre
        elif lista[medio].id < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1
```

#### 🔹 Manejo de Resultados con if
Después de ejecutar la búsqueda, verificamos si el usuario fue encontrado usando if nombre_lineal != -1: y if nombre_binaria != -1:.Esto se debe a que nuestras funciones de búsqueda devuelven:
*El nombre del usuario si el ID existe en la lista. 
*-1 si el ID no se encuentra.
```python
if nombre_lineal != -1:
    print(f"Usuario encontrado con búsqueda lineal: {nombre_lineal}")
else:
    print("Usuario no encontrado con búsqueda lineal.")

if nombre_binaria != -1:
    print(f"Usuario encontrado con búsqueda binaria: {nombre_binaria}")
else:
    print("Usuario no encontrado con búsqueda binaria.")
```

### 🔹 Comparación de Tiempos
Se mide el tiempo de ejecución de cada búsqueda usando `timeit`:
```python
tiempo_lineal = timeit.timeit(lambda: busqueda_lineal(usuarios, id_prueba), number=1)
tiempo_binaria = timeit.timeit(lambda: busqueda_binaria(usuarios, id_prueba), number=1)
```

## 📝 Resultados Esperados
Al ejecutar e ingresar un ID, se mostrará:
```bash
----- BUSCANDO -----
Usuario encontrado con búsqueda lineal: John Doe
Usuario encontrado con búsqueda binaria: John Doe
Tiempo de búsqueda lineal: 0.045678 segundos
Tiempo de búsqueda binaria: 0.000345 segundos
```


