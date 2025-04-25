import random  # Importa módulo para generar números aleatorios
import time    # Importa módulo para medir tiempo de ejecución
import matplotlib.pyplot as plt  # Importa matplotlib para graficar

# Algoritmos de ordenamiento (sin cambios)
def bubble_sort(arr):
    n = len(arr)  # Obtiene tamaño de la lista
    for i in range(n):  # Itera sobre cada elemento para múltiples pasadas
        for j in range(0, n - i - 1):  # Compara elementos adyacentes hasta el último ordenado
            if arr[j] > arr[j + 1]:  # Si el elemento actual es mayor que el siguiente
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Intercambia los elementos
    return arr  # Devuelve la lista ordenada

def quick_sort(arr):
    if len(arr) <= 1:  # Caso base: lista vacía o con un solo elemento
        return arr  # Devuelve la lista tal cual
    pivot = arr[len(arr) // 2]  # Selecciona el pivote en el medio de la lista
    left = [x for x in arr if x < pivot]  # Sublista con elementos menores al pivote
    middle = [x for x in arr if x == pivot]  # Sublista con elementos iguales al pivote
    right = [x for x in arr if x > pivot]  # Sublista con elementos mayores al pivote
    return quick_sort(left) + middle + quick_sort(right)  # Ordena recursivamente y concatena

def counting_sort(arr, exp):
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

def radix_sort(arr):
    max_num = max(arr)  # Encuentra el número máximo para saber cuántos dígitos ordenar
    exp = 1  # Empieza con el dígito menos significativo (unidades)
    while max_num // exp > 0:  # Mientras queden dígitos por ordenar
        counting_sort(arr, exp)  # Ordena la lista por el dígito actual
        exp *= 10  # Pasa al siguiente dígito (decenas, centenas, etc.)

# Generar números aleatorios
def generate_random_list(size):
    return [random.randint(10000, 99999) for _ in range(size)]  # Lista con números de 5 dígitos

# Medir tiempos de ejecución
def measure_time(sort_function, arr):
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
    times_bubble.append(measure_time(bubble_sort, test_list))  # Mide tiempo Bubble Sort y agrega a lista
    times_quick.append(measure_time(quick_sort, test_list))    # Mide tiempo Quick Sort y agrega a lista
    times_radix.append(measure_time(radix_sort, test_list))    # Mide tiempo Radix Sort y agrega a lista
    times_sorted.append(measure_time(sorted, test_list))       # Mide tiempo función sorted y agrega a lista

# Graficar resultados usando matplotlib
plt.figure(figsize=(10, 6))  # Crea figura de tamaño 10x6 pulgadas
plt.plot(sizes, times_bubble, 'r-o', label='Bubble Sort')  # Dibuja curva roja con círculos para Bubble Sort
plt.plot(sizes, times_quick, 'b-o', label='Quick Sort')    # Dibuja curva azul con círculos para Quick Sort
plt.plot(sizes, times_radix, 'g-o', label='Radix Sort')    # Dibuja curva verde con círculos para Radix Sort
plt.plot(sizes, times_sorted, 'm-o', label='Built-in Sorted')  # Dibuja curva morada con círculos para sorted()

plt.title('Comparación de Algoritmos de Ordenamiento')  # Título del gráfico
plt.xlabel('Tamaño de lista (n)')  # Etiqueta eje X
plt.ylabel('Tiempo de ejecución (segundos)')  # Etiqueta eje Y
plt.legend()  # Muestra leyenda con etiquetas de cada curva
plt.grid(True)  # Activa cuadrícula para facilitar lectura
plt.tight_layout()  # Ajusta automáticamente el layout para que no se corten elementos
plt.show()  # Muestra el gráfico en pantalla

# módulo para organizar funciones o clases utilizadas en nuestro proyecto
# Crear tantos módulos como sea necesario para organizar el código
