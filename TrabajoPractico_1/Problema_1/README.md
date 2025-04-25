# 🐍Comparación Visual de Algoritmos de Ordenamiento en Python

Breve descripción del proyecto:
Este es un script en Python que compara el rendimiento de distintos algoritmos de ordenamiento: Bubble Sort, Quick Sort, Radix Sort y la función built-in sorted. Genera listas de números aleatorios de diferentes tamaños, mide el tiempo que tarda cada algoritmo en ordenar dichas listas, y finalmente visualiza los resultados en un gráfico interactivo usando la librería Turtle. El proyecto permite analizar visualmente la eficiencia relativa de cada algoritmo según el tamaño de la lista, facilitando la comprensión de sus diferencias de rendimiento.

---
## 🏗Arquitectura General

Script en Python que compara el rendimiento de Bubble Sort, Quick Sort, Radix Sort y la función built-in sorted. Genera listas aleatorias, mide los tiempos de ordenamiento y muestra un gráfico con Turtle para visualizar las diferencias de eficiencia según el tamaño de la lista. Se ordena con varios codigos como: Algoritmos: bubble_sort, quick_sort, radix_sort (con counting_sort auxiliar); Generación y medición: generate_random_list crea listas aleatorias; measure_time calcula tiempo de ejecución; Ejecución: Se prueban distintos tamaños y se almacenan los tiempos; Visualización: draw_graph dibuja el gráfico comparativo con Turtle.

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
