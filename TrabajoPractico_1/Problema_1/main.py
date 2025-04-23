import random
import time
import turtle

# Implementación de los algoritmos de ordenamiento
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

# Generar números aleatorios
def generate_random_list(size):
    return [random.randint(10000, 99999) for _ in range(size)]

# Medir tiempos de ejecución
def measure_time(sort_function, arr):
    start_time = time.time()
    sort_function(arr.copy())
    return time.time() - start_time

sizes = range(100, 1001, 100)
times_bubble = []
times_quick = []
times_radix = []
times_sorted = []

for size in sizes:
    test_list = generate_random_list(size)
    times_bubble.append(measure_time(bubble_sort, test_list))
    times_quick.append(measure_time(quick_sort, test_list))
    times_radix.append(measure_time(radix_sort, test_list))
    times_sorted.append(measure_time(sorted, test_list))  # Comparar con la función sorted de Python

# Graficar resultados con Turtle
def draw_graph(sizes, times_bubble, times_quick, times_radix, times_sorted):
    screen = turtle.Screen()
    screen.title("Comparación de Algoritmos de Ordenamiento")
    screen.setup(width=800, height=600)
    turtle.speed(0)

    # Dibujar ejes con escala
    turtle.penup()
    turtle.goto(-300, -200)
    turtle.pendown()
    turtle.forward(600)
    turtle.write("Tamaño de lista (n)", align="center", font=("Arial", 12, "bold"))

    turtle.penup()
    turtle.goto(-300, -200)
    turtle.left(90)
    turtle.pendown()
    turtle.forward(400)
    turtle.write("Tiempo de ejecución (s)", align="center", font=("Arial", 12, "bold"))

    # Función para graficar curvas
    def draw_curve(sizes, times, color, label, label_offset):
        turtle.penup()
        turtle.goto(-300 + sizes[0] // 1.5, -200 + times[0] * 300)
        turtle.pencolor(color)
        turtle.pendown()
        for size, time in zip(sizes, times):
            turtle.goto(-300 + size // 1.5, -200 + time * 300)
        
        # Etiqueta dinámica
        turtle.penup()
        turtle.goto(-300 + sizes[-1] // 1.5, -200 + times[-1] * 300 + label_offset)
        turtle.write(label, align="center", font=("Arial", 10, "normal"))

    # Dibujar cada curva y ajustar etiquetas dinámicamente
    draw_curve(sizes, times_bubble, "red", "Bubble Sort", 20)
    draw_curve(sizes, times_quick, "blue", "Quick Sort", -20)
    draw_curve(sizes, times_radix, "green", "Radix Sort", 40)
    draw_curve(sizes, times_sorted, "purple", "Built-in Sorted", 60)

    # Leyenda
    turtle.penup()
    turtle.goto(-300, 150)
    turtle.write("Leyenda:", font=("Arial", 12, "bold"))
    turtle.goto(-300, 130)
    turtle.pencolor("red")
    turtle.write("Rojo: Bubble Sort", font=("Arial", 10, "normal"))
    turtle.goto(-300, 110)
    turtle.pencolor("blue")
    turtle.write("Azul: Quick Sort", font=("Arial", 10, "normal"))
    turtle.goto(-300, 90)
    turtle.pencolor("green")
    turtle.write("Verde: Radix Sort", font=("Arial", 10, "normal"))
    turtle.goto(-300, 70)
    turtle.pencolor("purple")
    turtle.write("Morado: Built-in Sorted", font=("Arial", 10, "normal"))

    turtle.done()

draw_graph(sizes, times_bubble, times_quick, times_radix, times_sorted)
