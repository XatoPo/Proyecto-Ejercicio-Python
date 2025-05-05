from utils.pause_timer import PauseTimer

def bubble_sort(arr, timer: PauseTimer):
    """
    Burbuja con pausas e interrupciones evolutivas.
    Complejidad O(n^2).
    """
    n = len(arr)
    # VIDEO: Analogía de personas en fila
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
            if timer.tick():
                return arr
        if not swapped:
            break
        if timer.tick():
            return arr
    return arr