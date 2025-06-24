class MonticuloBinario:
    def __init__(self):
        self._datos = []

    def insertar(self, item):
        self._datos.append(item)
        self._flotar(len(self._datos) - 1)

    def extraer(self):
        if not self._datos:
            return None
        self._intercambiar(0, -1)
        min_item = self._datos.pop()
        self._hundir(0)
        return min_item

    def _flotar(self, i):
        padre = (i - 1) // 2
        while i > 0 and self._datos[i] < self._datos[padre]:
            self._intercambiar(i, padre)
            i = padre
            padre = (i - 1) // 2

    def _hundir(self, i):
        n = len(self._datos)
        while True:
            menor = i
            izq = 2*i + 1
            der = 2*i + 2
            if izq < n and self._datos[izq] < self._datos[menor]:
                menor = izq
            if der < n and self._datos[der] < self._datos[menor]:
                menor = der
            if menor == i:
                break
            self._intercambiar(i, menor)
            i = menor

    def _intercambiar(self, i, j):
        self._datos[i], self._datos[j] = self._datos[j], self._datos[i]

    def __len__(self):
        return len(self._datos)

    def mostrar(self):
        return list(self._datos)
