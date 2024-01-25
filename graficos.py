import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)

# Datos de calificaciones de los estudiantes
matematicas = rng.integers(50, 100, 20)
ciencias = rng.integers(40, 95, 20)
literatura = rng.integers(60, 100, 20)

# Datos de errores para el gráfico de barras de error
errores_matematicas = rng.uniform(2, 5, 2)
errores_matematicas = [min(errores_matematicas), max(errores_matematicas)]

errores_ciencias = rng.uniform(1, 4, 2)
errores_ciencias = [min(errores_ciencias), max(errores_ciencias)]

errores_literatura = rng.uniform(3, 6, 2)
errores_literatura = [min(errores_literatura), max(errores_literatura)]

# Gráfico de dispersión
plt.figure(figsize=(10, 6))
plt.scatter(matematicas, ciencias, color='blue')
plt.title('Relación entre Calificaciones de Matemáticas y Ciencias')
plt.xlabel('Calificaciones de Matemáticas')
plt.ylabel('Calificaciones de Ciencias')
plt.grid(True)
plt.show()

# Gráfico de barras de error
materias = ['Matemáticas', 'Ciencias', 'Literatura']
calificaciones_promedio = [np.mean(matematicas), np.mean(ciencias), np.mean(literatura)]
errores = [errores_matematicas, errores_ciencias, errores_literatura]

plt.figure(figsize=(10, 6))
plt.bar(materias, calificaciones_promedio, yerr=errores, capsize=5, color=['blue', 'green', 'orange'])
plt.title('Calificaciones Promedio con Barras de Error')
plt.xlabel('Materias')
plt.ylabel('Calificación Promedio')
plt.legend(['Calificaciones Promedio'])
plt.grid(axis='y')
plt.show()

# Histograma
plt.figure(figsize=(10, 6))
plt.hist(matematicas, bins=10, color='skyblue', edgecolor='black')
plt.title('Distribución de Calificaciones de Matemáticas')
plt.xlabel('Calificaciones de Matemáticas')
plt.ylabel('Frecuencia')
plt.grid(axis='y')
plt.show()
