from modules.monticulo import MonticuloBinario

class ColaDePrioridad:
    def __init__(self):
        self._monticulo = MonticuloBinario()

    def agregar(self, paciente):
        self._monticulo.insertar(paciente)

    def atender(self):
        return self._monticulo.extraer()

    def __len__(self):
        return len(self._monticulo)

    def mostrar_pacientes(self):
        return self._monticulo.mostrar()
