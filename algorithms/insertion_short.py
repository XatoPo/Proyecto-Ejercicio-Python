def insertion_sort(arr, timeout=15):
    import time
    start = time.time()
    for i in range(1, len(arr)):
        if time.time() - start > timeout:
            break
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key