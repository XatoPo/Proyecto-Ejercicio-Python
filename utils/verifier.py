from .binary_search import binary_search_index

class Verifier:
    """
    Cuenta cuántos elementos están en su posición final correcta
    comparando con el arreglo totalmente ordenado.
    """
    def __init__(self, original_arr):
        self.sorted = sorted(original_arr)

    def count_correct(self, arr_partial):
        count = 0
        for idx, val in enumerate(arr_partial):
            if binary_search_index(self.sorted, val) == idx:
                count += 1
        return count