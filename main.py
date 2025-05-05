import random
import time
from algorithms.insertion_sort import insertion_sort
from algorithms.bubble_sort import bubble_sort
from algorithms.merge_sort import merge_sort
from algorithms.quick_sort import quick_sort
from utils.pause_timer import PauseTimer
from utils.verifier import Verifier

# VIDEO: Mostrar main.py y explicar imports y configuración inicial.

SEED = 42
SIZE = 10**6
TIMES = [5, 10, 15]  # segundos progresivos

# Generación de arreglo único
random.seed(SEED)
original_array = [random.randint(0, SIZE) for _ in range(SIZE)]

print("Comparativa de algoritmos con pausas e interrupciones\n")

for name, func in [
    ("Insertion Sort", insertion_sort),
    ("Bubble Sort", bubble_sort),
    ("Merge Sort", merge_sort),
    ("Quick Sort", quick_sort),
]:
    print(f"--- Ejecutando {name} ---")
    # Copiamos el arreglo para mantener igualdad de partida
    arr_copy = original_array.copy()
    timer = PauseTimer(limit_seconds=TIMES[0], step=TIMES)
    start = time.time()
    result = func(arr_copy, timer)
    elapsed = time.time() - start

    # Verificación y muestra de resultados
    verifier = Verifier(original_array)
    correct = verifier.count_correct(result)
    sample = result[:10]

    print(f"Tiempo total: {elapsed:.2f}s | Elementos correctos: {correct}")
    print(f"Muestra parcial (10 primeros): {sample}\n")

print("--- Fin de la comparativa ---")