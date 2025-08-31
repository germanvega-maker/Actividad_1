import numpy as np
import matplotlib.pyplot as plt

def graficar_polinomios(*polinomios):
    """
    Interfaz de usuario (IU) para graficar un número arbitrario de polinomios
    de la forma f(x) = a * x^n.

    Parámetro:
        *polinomios: cualquier cantidad de tuplas (a, n), donde:
            - a: coeficiente del polinomio
            - n: exponente del polinomio

    Ejemplo:
        graficar_polinomios((1, 2), (-0.5, 3), (2, 1))
        Esto grafica:
            f(x) = x^2
            f(x) = -0.5x^3
            f(x) = 2x
    """
    x = np.linspace(-10, 10, 400)  # Dominio común para todos los polinomios
    plt.figure(figsize=(10, 6))    # Tamaño de la figura

    for a, n in polinomios:
        y = a * x**n
        plt.plot(x, y, label=f"f(x) = {a}x^{n}")

    # Ejes, leyenda y estilo
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.title("Gráfica de polinomios f(x) = axⁿ")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid(True)
    plt.show()

# --------------------------
# EJECUCIÓN DEL PROGRAMA
# --------------------------

if __name__ == "__main__":
    # Definimos polinomios con parámetros (a, n)
    polinomio1 = (1, 2)     # f(x) = x^2
    polinomio2 = (-0.5, 3)  # f(x) = -0.5x^3
    polinomio3 = (2, 1)     # f(x) = 2x
    polinomio4 = (1, 0)     # f(x) = 1 (constante)

    # Llamamos a la IU pasando los polinomios
    graficar_polinomios(polinomio1, polinomio2, polinomio3, polinomio4)
