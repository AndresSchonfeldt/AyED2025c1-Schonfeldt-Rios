import datetime
import random

class Paciente:
    _contador = 0  # Para desempate según orden de llegada

    def __init__(self):
        self.riesgo = random.randint(1, 3)  # 1: crítico, 2: moderado, 3: bajo
        self.fecha_ingreso = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        self._orden_llegada = Paciente._contador
        Paciente._contador += 1

    def __lt__(self, otro):
        """Define prioridad en la cola de prioridad."""
        if self.riesgo == otro.riesgo:
            return self._orden_llegada < otro._orden_llegada  # Desempate por orden de llegada
        return self.riesgo < otro.riesgo  # Prioridad por menor riesgo (más crítico)

    def __repr__(self):
        return f"[Riesgo: {self.riesgo}, Ingreso: {self.fecha_ingreso}]"
