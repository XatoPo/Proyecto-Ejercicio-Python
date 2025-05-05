import time

class PauseTimer:
    """
    Pausa 2s cada 1s de ejecución y avanza límites progresivos.
    """
    def __init__(self, limit_seconds, steps):
        self.start = time.time()
        self.steps = steps
        self.step_idx = 0
        self.last_pause = self.start

    def tick(self):
        now = time.time()
        elapsed = now - self.start
        # Si supera el límite actual, avanza al siguiente o finaliza
        if elapsed > self.steps[self.step_idx]:
            print(f"[Timer] Interrupción tras {self.steps[self.step_idx]}s")
            self.step_idx += 1
            if self.step_idx >= len(self.steps):
                return True
        # Pausa 2s cada ~1s
        if now - self.last_pause >= 1:
            print("[Timer] Pausando 2 segundos...")
            time.sleep(2)
            self.last_pause = time.time()
        return False