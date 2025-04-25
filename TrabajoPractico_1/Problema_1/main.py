import random  # Importa módulo para generar números aleatorios
import time    # Importa módulo para medir tiempo de ejecución
import turtle  # Importa módulo para gráficos con tortuga (visualización)

# Implementación de los algoritmos de ordenamiento
def bubble_sort(arr):  # Define función para ordenar con Bubble Sort
    n = len(arr)  # Obtiene tamaño de la lista
    for i in range(n):  # Itera sobre cada elemento para múltiples pasadas
        for j in range(0, n-i-1):  # Compara elementos adyacentes hasta el último ordenado
            if arr[j] > arr[j+1]:  # Si el elemento actual es mayor que el siguiente
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Intercambia los elementos
    return arr  # Devuelve la lista ordenada

def quick_sort(arr):  # Define función para ordenar con Quick Sort
    if len(arr) <= 1:  # Caso base: lista vacía o con un solo elemento
        return arr  # Devuelve la lista tal cual
    pivot = arr[len(arr) // 2]  # Selecciona el pivote en el medio de la lista
    left = [x for x in arr if x < pivot]  # Sublista con elementos menores al pivote
    middle = [x for x in arr if x == pivot]  # Sublista con elementos iguales al pivote
    right = [x for x in arr if x > pivot]  # Sublista con elementos mayores al pivote
    return quick_sort(left) + middle + quick_sort(right)  # Ordena recursivamente y concatena

def counting_sort(arr, exp):  # Función auxiliar para Radix Sort, ordena por dígito según exp
    n = len(arr)  # Tamaño de la lista
    output = [0] * n  # Lista temporal para almacenar resultados ordenados
    count = [0] * 10  # Lista para contar ocurrencias de dígitos (0-9)
    for i in range(n):  # Cuenta ocurrencias del dígito en la posición exp
        index = (arr[i] // exp) % 10  # Extrae el dígito relevante
        count[index] += 1  # Incrementa contador para ese dígito
    for i in range(1, 10):  # Acumula los conteos para posiciones correctas
        count[i] += count[i - 1]
    for i in range(n - 1, -1, -1):  # Construye la lista ordenada desde atrás
        index = (arr[i] // exp) % 10  # Extrae el dígito relevante
        output[count[index] - 1] = arr[i]  # Coloca el elemento en la posición correcta
        count[index] -= 1  # Decrementa el contador para ese dígito
    for i in range(n):  # Copia la lista ordenada de vuelta a arr
        arr[i] = output[i]

def radix_sort(arr):  # Función para ordenar con Radix Sort usando Counting Sort
    max_num = max(arr)  # Encuentra el número máximo para saber cuántos dígitos ordenar
    exp = 1  # Empieza con el dígito menos significativo (unidades)
    while max_num // exp > 0:  # Mientras queden dígitos por ordenar
        counting_sort(arr, exp)  # Ordena la lista por el dígito actual
        exp *= 10  # Pasa al siguiente dígito (decenas, centenas, etc.)

# Generar números aleatorios
def generate_random_list(size):  # Función para crear lista de números aleatorios
    return [random.randint(10000, 99999) for _ in range(size)]  # Lista con números de 5 dígitos

# Medir tiempos de ejecución
def measure_time(sort_function, arr):  # Función para medir tiempo de ejecución de un algoritmo
    start_time = time.time()  # Guarda tiempo inicial
    sort_function(arr.copy())  # Ejecuta el algoritmo con copia de la lista para no modificar original
    return time.time() - start_time  # Retorna el tiempo transcurrido

sizes = range(100, 1001, 100)  # Rango de tamaños de listas para probar (100 a 1000 en pasos de 100)
times_bubble = []  # Lista para almacenar tiempos de Bubble Sort
times_quick = []   # Lista para tiempos de Quick Sort
times_radix = []   # Lista para tiempos de Radix Sort
times_sorted = []  # Lista para tiempos de la función built-in sorted

for size in sizes:  # Para cada tamaño de lista
    test_list = generate_random_list(size)  # Genera una lista aleatoria
    times_bubble.append(measure_time(bubble_sort, test_list))  # Mide tiempo Bubble Sort
    times_quick.append(measure_time(quick_sort, test_list))    # Mide tiempo Quick Sort
    times_radix.append(measure_time(radix_sort, test_list))    # Mide tiempo Radix Sort
    times_sorted.append(measure_time(sorted, test_list))       # Mide tiempo función sorted

# Graficar resultados con Turtle
def draw_graph(sizes, times_bubble, times_quick, times_radix, times_sorted):
    screen = turtle.Screen()  # Crea ventana para dibujo
    screen.title("Comparación de Algoritmos de Ordenamiento")  # Título de la ventana
    screen.setup(width=800, height=600)  # Tamaño de la ventana
    turtle.speed(0)  # Velocidad máxima de dibujo

    # Dibujar ejes con escala
    turtle.penup()  # Levanta el lápiz para mover sin dibujar
    turtle.goto(-300, -200)  # Posiciona en esquina inferior izquierda para eje X
    turtle.pendown()  # Baja el lápiz para comenzar a dibujar
    turtle.forward(600)  # Dibuja eje X (horizontal)
    turtle.write("Tamaño de lista (n)", align="center", font=("Arial", 12, "bold"))  # Etiqueta eje X

    turtle.penup()  # Levanta lápiz para mover
    turtle.goto(-300, -200)  # Vuelve a posición inicial para eje Y
    turtle.left(90)  # Gira para dibujar eje Y vertical
    turtle.pendown()  # Baja lápiz para dibujar eje Y
    turtle.forward(400)  # Dibuja eje Y
    turtle.write("Tiempo de ejecución (s)", align="center", font=("Arial", 12, "bold"))  # Etiqueta eje Y

    # Función para graficar curvas
    def draw_curve(sizes, times, color, label, label_offset):
        turtle.penup()  # Levanta lápiz para posicionar
        turtle.goto(-300 + sizes[0] // 1.5, -200 + times[0] * 300)  # Posiciona primer punto de la curva
        turtle.pencolor(color)  # Cambia color del lápiz
        turtle.pendown()  # Baja lápiz para dibujar
        for size, time in zip(sizes, times):  # Para cada punto de datos
            turtle.goto(-300 + size // 1.5, -200 + time * 300)  # Dibuja línea hasta el punto siguiente
        
        # Etiqueta dinámica al final de la curva
        turtle.penup()
        turtle.goto(-300 + sizes[-1] // 1.5, -200 + times[-1] * 300 + label_offset)
        turtle.write(label, align="center", font=("Arial", 10, "normal"))

    # Dibujar cada curva y ajustar etiquetas dinámicamente
    draw_curve(sizes, times_bubble, "red", "Bubble Sort", 20)  # Curva rojo para Bubble Sort
    draw_curve(sizes, times_quick, "blue", "Quick Sort", -20)  # Curva azul para Quick Sort
    draw_curve(sizes, times_radix, "green", "Radix Sort", 40)  # Curva verde para Radix Sort
    draw_curve(sizes, times_sorted, "purple", "Built-in Sorted", 60)  # Curva morada para sorted()

    # Leyenda para identificar colores
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

    turtle.done()  # Finaliza dibujo y mantiene ventana abierta

draw_graph(sizes, times_bubble, times_quick, times_radix, times_sorted)  # Llama función para mostrar gráfico
