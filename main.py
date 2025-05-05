import sys, os
# Asegura imports locales
sys.path.insert(0, os.path.dirname(__file__))

import random, time
from algorithms.insertion_sort import insertion_sort
from algorithms.bubble_sort    import bubble_sort
from algorithms.merge_sort     import merge_sort
from algorithms.quick_sort     import quick_sort
from utils.pause_timer import PauseTimer
from utils.verifier     import Verifier

# Configuración
SEED = 42
SIZE = 10**6
TIMES = [5, 10, 15]  # segundos

random.seed(SEED)
original_array = [random.randint(1, SIZE) for _ in range(SIZE)]

print("== Comparativa de algoritmos con pausas e interrupciones ==\n")

for name, func in [
    ("Insertion Sort", insertion_sort),
    ("Bubble Sort",    bubble_sort),
    ("Merge Sort",     merge_sort),
    ("Quick Sort",     quick_sort),
]:
    print(f"-- Ejecutando {name} --")
    arr = original_array.copy()
    timer = PauseTimer(limit_seconds=TIMES[0], steps=TIMES)
    start = time.time()
    result = func(arr, timer)
    elapsed = time.time() - start

    verifier = Verifier(original_array)
    correct = verifier.count_correct(result)
    sample = result[:10]

    print(f"Tiempo real: {elapsed:.2f}s | Elementos correctos: {correct}")
    print(f"Muestra parcial: {sample}\n")

print("== Fin de la comparativa ==")