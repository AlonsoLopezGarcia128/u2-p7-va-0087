# Alonso Lopez Garcia NC = 0087 | Fecha 28/10/2026
import numpy as np
import matplotlib.pyplot as plt
no_lista = [1, 2, 3, 17, 48]
calificacion_ml = [20, 30, 80, 100, 90]
calificacion_va = [70, 90, 60, 90, 100]

plt.plot(no_lista, calificacion_ml, label="Calificaciones Machine Learning -- 0087", color = "cyan", marker = "d")
plt.plot(no_lista, calificacion_va, label="Calificaciones Vision Artificial -- 0087", color = "green", marker = "*")

plt.title("Calificaciones materias -- 0087")
plt.xlabel("Numero de lista -- 0087")
plt.ylabel("Calificaciones ML / VA -- 0087")

plt.legend()
plt.show()

print("Alonso Lopez Garcia NC = 0087 | Fecha 28/10/2026")