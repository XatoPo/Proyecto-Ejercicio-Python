import random
from algorithms.insertion_sort import insertion_sort
from algorithms.bubble_sort import bubble_sort
from algorithms.merge_sort import merge_sort
from algorithms.quick_sort import quick_sort
from utils.timer import progressive_timer
from utils.verifier import count_sorted_prefix
from utils.binary_search import binary_search

# Generar el mismo arreglo aleatorio de 1 millón de elementos para todos
ARRAY_SIZE = 1_000_000
original_array = [random.randint(1, 1_000_000) for _ in range(ARRAY_SIZE)]

algorithms = [
    ("Insertion Sort", insertion_sort),
    ("Bubble Sort", bubble_sort),
    ("Merge Sort", merge_sort),
    ("Quick Sort", quick_sort),
]

print("Iniciando comparativa de algoritmos de ordenamiento con interrupciones evolutivas...\n")

for name, algo_func in algorithms:
    print(f"--- Ejecutando: {name} ---")
    array_copy = original_array.copy()

    sorted_partial = progressive_timer(algo_func, array_copy, max_total_time=15)

    # Verificamos cuántos elementos están bien ordenados
    correct_count = count_sorted_prefix(sorted_partial)
    print(f"Progreso de {name}: {correct_count} elementos correctamente ordenados.\n")

    # Comprobación binaria de existencia de número para demostrar búsqueda
    found = binary_search(sorted_partial, original_array[500000])
    print(f"Verificación con búsqueda binaria: {'Encontrado' if found else 'No encontrado'}\n")

print("\n--- Comparativa Finalizada ---")