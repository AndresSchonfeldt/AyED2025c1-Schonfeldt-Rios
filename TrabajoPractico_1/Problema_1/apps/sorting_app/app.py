# sorting_app/app.py


import random
import time
import matplotlib.pyplot as plt

from modules.bubble_sort import bubble_sort
from modules.quick_sort import quick_sort
from modules.counting_sort import counting_sort
from modules.radix_sort import radix_sort

def generate_random_list(size):
    return [random.randint(10000, 99999) for _ in range(size)]

def measure_time(sort_function, arr):
    start = time.time()
    # Para counting_sort se necesita un wrapper para ordenar toda la lista
    if sort_function == counting_sort:
        # Ordenar por todos los dígitos (radix completo)
        max_num = max(arr)
        exp = 1
        arr_copy = arr.copy()
        while max_num // exp > 0:
            counting_sort(arr_copy, exp)
            exp *= 10
    else:
        sort_function(arr.copy())
    return time.time() - start

sizes = range(100, 1001, 100)

times_bubble = []
times_quick = []
times_counting = []
times_radix = []
times_builtin = []

for size in sizes:
    test_list = generate_random_list(size)
    times_bubble.append(measure_time(bubble_sort, test_list))
    times_quick.append(measure_time(quick_sort, test_list))
    times_counting.append(measure_time(counting_sort, test_list))
    times_radix.append(measure_time(radix_sort, test_list))
    times_builtin.append(measure_time(sorted, test_list))

plt.figure(figsize=(10, 6))
plt.plot(sizes, times_bubble, 'r-o', label='Bubble Sort')
plt.plot(sizes, times_quick, 'b-o', label='Quick Sort')
plt.plot(sizes, times_counting, 'c-o', label='Counting Sort (full)')
plt.plot(sizes, times_radix, 'g-o', label='Radix Sort')
plt.plot(sizes, times_builtin, 'm-o', label='Built-in sorted()')
plt.title('Comparación de Algoritmos de Ordenamiento')
plt.xlabel('Tamaño de lista (n)')
plt.ylabel('Tiempo de ejecución (segundos)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
