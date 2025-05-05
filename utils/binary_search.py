import bisect

def binary_search_index(sorted_arr, value):
    """
    Devuelve índice si value está en sorted_arr, -1 si no.
    """
    i = bisect.bisect_left(sorted_arr, value)
    return i if i < len(sorted_arr) and sorted_arr[i] == value else -1