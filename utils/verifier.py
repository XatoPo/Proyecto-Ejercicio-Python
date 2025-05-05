from .binary_search import binary_search_index

class Verifier:
    """
    Cuenta cuántos elementos están en posición correcta
    comparando con arreglo fully sorted.
    """
    def __init__(self, original):
        self.sorted = sorted(original)

    def count_correct(self, arr_partial):
        count = 0
        for idx, val in enumerate(arr_partial):
            if binary_search_index(self.sorted, val) == idx:
                count += 1
        return count