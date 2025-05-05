from utils.pause_timer import PauseTimer

def insertion_sort(arr, timer: PauseTimer):
    """
    Inserción con pausas e interrupciones evolutivas.
    Complejidad O(n^2).
    """
    # VIDEO: Analogía del mazo de cartas
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
            if timer.tick():
                return arr
        arr[j+1] = key
        if timer.tick():
            return arr
    return arr