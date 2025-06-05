import heapq

class ColaPrioridad:
    def __init__(self):
        self._heap = []

    def agregar(self, elemento):
        heapq.heappush(self._heap, elemento)

    def atender(self):
        if self._heap:
            return heapq.heappop(self._heap)
        return None

    def __len__(self):
        return len(self._heap)

    def mostrar_pacientes(self):
        return sorted(self._heap)  # Muestra en orden de prioridad
