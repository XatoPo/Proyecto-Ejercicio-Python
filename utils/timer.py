import time

def progressive_timer(sort_function, arr, max_total_time=15):
    start = time.time()
    elapsed = 0
    step = 3

    while elapsed < max_total_time:
        arr_copy = arr.copy()
        sort_function(arr_copy, timeout=step)
        time.sleep(2)  # Pausa simulada
        elapsed = time.time() - start
        print(f"Interrupción tras {step} segundos...")
        step += 3
    return arr_copy