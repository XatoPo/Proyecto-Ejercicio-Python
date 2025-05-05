from utils.pause_timer import PauseTimer

def quick_sort(arr, timer: PauseTimer):
    """
    Quick Sort iterativo con pausas e interrupciones.
    Complejidad promedio O(n log n).
    """
    stack = [(0, len(arr)-1)]
    while stack:
        lo, hi = stack.pop()
        if lo < hi:
            pivot = arr[hi]
            i = lo
            for j in range(lo, hi):
                if arr[j] < pivot:
                    arr[i], arr[j] = arr[j], arr[i]
                    i += 1
                if timer.tick():
                    return arr
            arr[i], arr[hi] = arr[hi], arr[i]
            stack.append((lo, i-1))
            stack.append((i+1, hi))
        if timer.tick():
            break
    return arr