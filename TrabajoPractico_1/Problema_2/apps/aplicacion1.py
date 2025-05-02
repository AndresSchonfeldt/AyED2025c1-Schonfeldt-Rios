import timeit
import turtle
from modules.Actividad2 import ListaDobleEnlazada

# Tamaños de lista a evaluar
N_values = [100, 500, 1000, 5000, 10000]
times_len = []
times_copia = []
times_invertir = []

# Medir tiempos de ejecución para cada tamaño de lista
for N in N_values:
    lde = ListaDobleEnlazada()
    for i in range(N):
        lde.agregar_al_final(i)

    times_len.append(timeit.timeit(lambda: len(lde), number=10))
    times_copia.append(timeit.timeit(lambda: lde.copia(), number=10))
    times_invertir.append(timeit.timeit(lambda: lde.invertir(), number=10))

# Configurar pantalla de Turtle
pantalla = turtle.Screen()
pantalla.setup(width=900, height=600)
pantalla.title("Tiempo de ejecución vs. Cantidad de elementos")
pantalla.bgcolor("white")

# Configurar trazador de Turtle
grafico = turtle.Turtle()
grafico.speed(0)
grafico.color("black")
grafico.pensize(1.5)  # Línea más delgada

# Dibujar ejes
grafico.penup()
grafico.goto(-350, -250)
grafico.pendown()
grafico.forward(700)  # Eje X
grafico.penup()
grafico.goto(-350, -250)
grafico.left(90)
grafico.pendown()
grafico.forward(500)  # Eje Y

# Etiquetas de los ejes
grafico.penup()
grafico.goto(350, -270)
grafico.write("Cantidad de elementos (N)", align="center", font=("Arial", 14, "bold"))
grafico.goto(-370, 230)
grafico.write("Tiempo de ejecución (s)", align="center", font=("Arial", 14, "bold"))

# Escalar datos para la visualización
max_N = max(N_values)
max_time = max(max(times_len), max(times_copia), max(times_invertir))

def escalar_x(N):
    return (N / max_N) * 600 - 300

def escalar_y(time):
    return (time / max_time) * 400 - 200

# Dibujar los puntos y líneas
def dibujar_puntos(color, datos, forma):
    grafico.color(color)
    grafico.penup()
    prev_x, prev_y = None, None

    for i in range(len(N_values)):
        x = escalar_x(N_values[i])
        y = escalar_y(datos[i])
        grafico.goto(x, y)
        grafico.pendown()
        grafico.shape(forma)  # Cambia forma de los puntos
        grafico.stamp()  # Coloca marcador

        # Dibujar líneas entre los puntos
        if prev_x is not None:
            grafico.penup()
            grafico.goto(prev_x, prev_y)
            grafico.pendown()
            grafico.goto(x, y)
        
        prev_x, prev_y = x, y

dibujar_puntos("red", times_len, "circle")
dibujar_puntos("blue", times_copia, "square")
dibujar_puntos("green", times_invertir, "triangle")

# **Agregar leyenda dentro de la gráfica**
grafico.penup()
grafico.goto(150, 200)
grafico.color("red")
grafico.write("🔴 len()", align="left", font=("Arial", 12, "bold"))

grafico.goto(150, 180)
grafico.color("blue")
grafico.write("🔵 copia()", align="left", font=("Arial", 12, "bold"))

grafico.goto(150, 160)
grafico.color("green")
grafico.write("🟢 invertir()", align="left", font=("Arial", 12, "bold"))

# Mantener ventana abierta
turtle.done()
# Aplicación secundaria
