import time

class PauseTimer:
    """
    Temporiza la ejecución de un algoritmo con pausas de 2s
    tras cada 1s de ejecución, y permite cambiar el límite de tiempo
    según una lista de pasos evolutivos.
    """
    def __init__(self, limit_seconds, step):
        self.start_time = time.time()
        self.limit_seconds = limit_seconds
        self.steps = step
        self.current_step_index = 0
        self.last_pause = self.start_time

    def tick(self):
        now = time.time()
        elapsed = now - self.start_time
        # Si excede el límite actual, avanzar al siguiente límite o detener
        if elapsed > self.steps[self.current_step_index]:
            print(f"[Timer] Interrupción tras {self.steps[self.current_step_index]}s")
            self.current_step_index += 1
            # Si no hay más pasos, finaliza
            if self.current_step_index >= len(self.steps):
                return True
        # Pausa de 2s cada 1s de ejecución
        if now - self.last_pause >= 1:
            print("[Timer] Pausando 2 segundos...")
            time.sleep(2)
            self.last_pause = time.time()
        return False