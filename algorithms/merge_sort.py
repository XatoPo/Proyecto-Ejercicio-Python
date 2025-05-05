from utils.pause_timer import PauseTimer

def merge_sort(arr, timer: PauseTimer):
    """
    Merge Sort bottom-up con pausas e interrupciones.
    Complejidad O(n log n).
    """
    n = len(arr)
    width = 1
    aux = arr.copy()
    while width < n:
        for left in range(0, n, 2*width):
            mid = min(left + width, n)
            right = min(left + 2*width, n)
            i, j, k = left, mid, left
            while i < mid and j < right:
                if arr[i] <= arr[j]:
                    aux[k] = arr[i]; i += 1
                else:
                    aux[k] = arr[j]; j += 1
                k += 1
            while i < mid:
                aux[k] = arr[i]; i += 1; k += 1
            while j < right:
                aux[k] = arr[j]; j += 1; k += 1
        arr[:] = aux[:]
        width *= 2
        if timer.tick():
            break
    return arr