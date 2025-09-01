# actividad_encapsulamiento_csv.py

import matplotlib.pyplot as plt
import numpy as np
import csv
import os

# -------------------------------
# 1. FUNCIONALIDAD: GRAFICAR POLINOMIOS
# -------------------------------

def graficar_polinomios(*polinomios):
    """
    Grafica un número arbitrario de polinomios de la forma y = a*x^n.
    Cada polinomio se representa con una tupla (a, n).
    Se usa el operador * para aceptar múltiples argumentos.
    """
    x = np.linspace(-10, 10, 400)
    
    for a, n in polinomios:
        y = a * x**n
        plt.plot(x, y, label=f'y = {a}x^{n}')
    
    plt.title("Gráfica de Polinomios")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.legend()
    plt.show()

# Llamada de ejemplo (puedes cambiar los valores)
graficar_polinomios((1, 2), (0.5, 3), (-1, 1))


# -------------------------------
# 2. FUNCIONALIDAD: ESCRITURA DE CSV
# -------------------------------

# Lista de frutas
frutas = [
    ["Manzana", "Roja", "Dulce"],
    ["Plátano", "Amarillo", "Dulce"],
    ["Lima", "Verde", "Ácida"]
]

# Directorio para guardar el archivo CSV (en carpeta 'actividad_datos' dentro del directorio principal del usuario)
directorio = os.path.expanduser("~/actividad_datos")
os.makedirs(directorio, exist_ok=True)

# Ruta completa al archivo frutas.csv
ruta_csv = os.path.join(directorio, "frutas.csv")

# Escritura del archivo CSV
with open(ruta_csv, mode='w', newline='', encoding='utf-8') as archivo_csv:
    escritor = csv.writer(archivo_csv)
    escritor.writerows(frutas)

print(f"✅ Archivo frutas.csv guardado correctamente en: {ruta_csv}")


# -------------------------------
# 3. FUNCIONALIDAD: LECTURA DE CSV
# -------------------------------

# Lista para almacenar los datos leídos
datos_frutas = []

# Lectura del archivo CSV
with open(ruta_csv, mode='r', encoding='utf-8') as archivo_csv:
    lector = csv.reader(archivo_csv)
    for fila in lector:
        datos_frutas.append(fila)

# Mostrar datos leídos
print("✅ Contenido del archivo frutas.csv:")
print(datos_frutas)
