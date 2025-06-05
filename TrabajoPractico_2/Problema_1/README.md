# Sala de Emergencias - Simulación de Triaje🚑

Breve descripción del proyecto:
Este proyecto es una simulación simple de un sistema de triaje en una sala de emergencias, donde los pacientes son atendidos según su nivel de riesgo. La implementación garantiza que los casos más críticos tengan prioridad en la atención médica.

---
## 🏗Arquitectura General

La organización del código se basa en una estructura modular:

-paciente.py: Define los pacientes con su nivel de riesgo y datos de ingreso.

-cola_prioridad.py: Implementa la cola de prioridad mediante un heap.

-main.py: Ejecuta la simulación, gestionando el ingreso y atención de pacientes.

El proyecto se centra en la gestión de la información y en la correcta estructuración de la lógica de triaje, dejando la representación visual como parte del PDF del informe, que contiene gráficos generados con herramientas de visualización apropiadas.

---
## 📑Dependencias
Este proyecto usa las siguientes bibliotecas:

-heapq: Para la gestión eficiente de la cola de prioridad.

-random: Para la asignación aleatoria de riesgo a los pacientes.

-datetime: Para registrar tiempos de ingreso y atención.

---
## 🚀Cómo Ejecutar el Proyecto
1. Clonar o descargar el repositorio.

2. Asegurarse de tener Python 3.x instalado.

3. Ejecutar el archivo main.py:
   ```bash
   python main.py
   ```

---
## 🙎‍♀️🙎‍♂️Autores

- Rios Rodrigo Ezequiel
- Andres Schonfeldt

---

> **Consejo**: Mantén el README **actualizado** conforme evoluciona el proyecto, y elimina (o añade) secciones según necesites. Esta plantilla es sólo un punto de partida general.
