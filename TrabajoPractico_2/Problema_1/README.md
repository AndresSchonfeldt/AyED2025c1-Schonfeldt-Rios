# 🐍Comparación Visual de Algoritmos de Ordenamiento en Python

Breve descripción del proyecto:
Este es un script en Python que compara el rendimiento de distintos algoritmos de ordenamiento: Bubble Sort, Quick Sort, Radix Sort y la función built-in sorted. Genera listas de números aleatorios de diferentes tamaños, mide el tiempo que tarda cada algoritmo en ordenar dichas listas, y finalmente visualiza los resultados en un gráfico interactivo usando la librería Turtle. El proyecto permite analizar visualmente la eficiencia relativa de cada algoritmo según el tamaño de la lista, facilitando la comprensión de sus diferencias de rendimiento.

---
## 🏗Arquitectura General

Este programa en Python compara el rendimiento de cuatro algoritmos de ordenamiento (Bubble Sort, Quick Sort, Radix Sort y la función nativa sorted() de Python) mediante listas aleatorias de números de 5 dígitos. El código genera listas con tamaños entre 100 y 1000 elementos (en incrementos de 100), mide los tiempos de ejecución de cada algoritmo usando time.time() y visualiza los resultados con matplotlib.pyplot. Los algoritmos incluyen: Bubble Sort (O(n²) por sus bucles anidados), Quick Sort (O(n log n) promedio con pivote central) y Radix Sort (O(n × k) mediante counting_sort para dígitos individuales). La función generate_random_list crea las listas aleatorias, mientras measure_time calcula los tiempos sin alterar los datos originales. Tras ejecutar las pruebas, el script configura un gráfico de líneas con título, ejes etiquetados, leyenda y cuadrícula, mostrando cómo sorted() (basado en Timsort) supera en velocidad a los demás, seguido de Radix Sort para datos de dígitos fijos, mientras Bubble Sort evidencia su ineficiencia con crecimiento cuadrático. El gráfico final, generado con plt.plot() y plt.show(), confirma visualmente la escalabilidad óptima de los algoritmos modernos frente a métodos clásicos.

Las gráficas de los resultados están disponible en la carpeta [data](./data) del proyecto.

El informe completo está disponible en la carpeta [docs](./docs) del proyecto.

---
## 📑Dependencias

1. **Python 3.x**
2. **matplotlib** (`pip install matplotlib`)
3. listar dependencias principales
4. Dependencias listadas en requierements.txt

---
## 🚀Cómo Ejecutar el Proyecto
1. **Clonar o descargar** el repositorio.

2. **Crear y activar** un entorno virtual.

3. **Instalar las dependencias**:
   ```bash
   pip install -r requirements.txt
   ```
   El archivo `requirements.txt` se encuentran en la carpeta [deps](./deps) del proyecto.

---
## 🙎‍♀️🙎‍♂️Autores

- Rios Rodrigo Ezequiel
- Andres Schonfeldt

---

> **Consejo**: Mantén el README **actualizado** conforme evoluciona el proyecto, y elimina (o añade) secciones según necesites. Esta plantilla es sólo un punto de partida general.
