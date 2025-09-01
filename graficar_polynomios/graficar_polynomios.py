import numpy as np
import matplotlib.pyplot as plt

# Solicitar al usuario los coeficientes del polinomio
entrada = input("Ingresa los coeficientes del polinomio separados por comas (de mayor a menor grado):\n")
coeficientes = [float(c.strip()) for c in entrada.split(",")]

# Crear el polinomio usando numpy
p = np.poly1d(coeficientes)

# Generar valores de x
x = np.linspace(-10, 10, 400)

# Evaluar el polinomio en esos valores
y = p(x)

# Graficar
plt.figure(figsize=(8, 6))
plt.plot(x, y, label=f"P(x) = {p}")
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.title("Gráfica del Polinomio")
plt.xlabel("x")
plt.ylabel("P(x)")
plt.legend()
plt.show()
