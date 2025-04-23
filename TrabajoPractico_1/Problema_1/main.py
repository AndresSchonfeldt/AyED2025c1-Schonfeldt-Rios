import random
import time
import turtle

# Explicación teórica
explicacion = """
Bubble Sort: O(n^2) porque cada elemento se compara con todos los demás.
QuickSort: O(n log n) en promedio debido a la división recurrente del problema.
Radix Sort: O(nk), donde k depende de la cantidad de dígitos, siendo lineal para listas grandes.
Python sorted(): Implementa Timsort, una combinación de Merge Sort y Insertion Sort, con O(n log n) en el peor caso.
"""

print(explicacion)  # Mostrar explicación en la consola

# Algoritmos de ordenamiento
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def radix_sort(arr):
    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10
    return arr

def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]

# Generación de listas de números aleatorios
sizes = range(1, 1001)
times = {"Bubble Sort": [], "QuickSort": [], "Radix Sort": [], "Sorted": []}

for size in sizes:
    data = [random.randint(10000, 99999) for _ in range(size)]

    for sort_func, name in [(bubble_sort, "Bubble Sort"), (quicksort, "QuickSort"),
                            (radix_sort, "Radix Sort"), (sorted, "Sorted")]:
        arr_copy = data[:]
        start_time = time.time()
        sort_func(arr_copy)
        end_time = time.time()
        times[name].append(end_time - start_time)

# Gráfica con Turtle
turtle.speed(0)
turtle.title("Comparación de tiempos de ordenamiento")

# Mostrar explicación en la gráfica
turtle.penup()
turtle.goto(-350, 250)
turtle.pencolor("black")
turtle.write(explicacion, font=("Arial", 10, "normal"))

colors = ["red", "blue", "green", "black"]
x_scale = 0.3
y_scale = 100

for i, (name, time_list) in enumerate(times.items()):
    turtle.pencolor(colors[i])
    turtle.penup()
    turtle.goto(-400, -250 + (i * 50))
    turtle.pendown()
    for j, time_value in enumerate(time_list):
        turtle.goto(-400 + j * x_scale, -250 + (i * 50) + time_value * y_scale)

turtle.done()
