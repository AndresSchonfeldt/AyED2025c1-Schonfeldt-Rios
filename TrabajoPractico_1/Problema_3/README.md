 🎮 Juego de Guerra

Breve descripción del proyecto:
Este es un script que simula el clásico juego de cartas "Guerra" entre dos jugadores, implementando una interfaz gráfica interactiva con la librería turtle de Python. Permite:
✅ Visualizar en tiempo real las cartas jugadas, los mazos y las victorias acumuladas.
✅ Simular dinámicas de guerra (empates) con pausas estratégicas para mejorar la legibilidad.
✅ Rastrear métricas clave: turnos jugados, cartas restantes y ganancias por jugador.
✅ Reproducir partidas mediante semillas aleatorias para garantizar consistencia en pruebas.

Características destacadas:

Lógica de comparación de cartas basada en valores numéricos (incluye figuras como J, Q, K, A).

Sistema de puntuación hasta 10 victorias para determinar el ganador final.

Animaciones simplificadas con velocidad ajustable para una experiencia de usuario adaptable.

Manejo de errores para casos como mazos vacíos durante guerras.
---
## 🏗Arquitectura General

Organización del código:

El código sigue un enfoque orientado a objetos con 3 clases principales:

1.Carta:(Propiedades: valor, palo, visible), (Métodos clave: _valor_numerico(): Convierte J/Q/K/A a valores 11-14 / __gt__(): Compara cartas por su valor numérico / __str__(): Representación visual (-X si está oculta, ej: "A♠"))
2.Mazo: (Funcionalidades: poner_carta_arriba/abajo(): Gestiona cartas / sacar_carta_arriba(): Extrae y muestra cartas / Manejo de errores con DequeEmptyError)
3.JuegoGuerra (clase principal): (Componentes:Métodos de inicialización:_setup_turtle():/ Configuración gráfica armar_mazo_inicial(): Crea y baraja 52 cartas repartir_cartas(): Divide el mazo en 2), (Lógica del juego: iniciar_juego(): Bucle principal del juego/ _actualizar_display(): Muestra cartas en pantalla/ _mostrar_guerra(): Visualiza conflictos por empate /_transferir_cartas(): Mueve cartas al ganador),  (Visualización: Graficas independientes para jugadores, mesa e información / Animaciones con tracer() y pausas con time.sleep())

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

- Schonfeld Andres
- Rios Rodrigo

---

> **Consejo**: Mantén el README **actualizado** conforme evoluciona el proyecto, y elimina (o añade) secciones según necesites. Esta plantilla es sólo un punto de partida general.
