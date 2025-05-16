class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
        self.anterior = None

class ListaDobleEnlazada:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.size = 0

    def esta_vacia(self):
        return self.primero is None

    def agregar_al_final(self, valor):
        if self.esta_vacia():
            self.primero = self.ultimo = Nodo(valor)
        else:
            auxiliar = self.ultimo
            self.ultimo = Nodo(valor)
            auxiliar.siguiente = self.ultimo
            self.ultimo.anterior = auxiliar
        self.size += 1

    def agregar_al_inicio(self, valor):
        if self.esta_vacia():
            self.primero = self.ultimo = Nodo(valor)
        else:
            auxiliar = Nodo(valor)
            auxiliar.siguiente = self.primero
            self.primero.anterior = auxiliar
            self.primero = auxiliar
        self.size += 1

    def __len__(self):
        return self.size

    def extraer(self, posicion=None):
        if self.esta_vacia():
            raise IndexError("La lista está vacía")
        if posicion is None:
            valor = self.ultimo.valor
            if self.primero == self.ultimo:
                self.primero = self.ultimo = None
            else:
                self.ultimo = self.ultimo.anterior
                self.ultimo.siguiente = None
            self.size -= 1
            return valor

        if not isinstance(posicion, int):
            raise TypeError("La posición debe ser un entero")
        if posicion < 0 or posicion >= self.size:
            raise IndexError("Posición ingresada inválida")

        if posicion == 0:
            valor = self.primero.valor
            self.primero = self.primero.siguiente
            if self.primero:
                self.primero.anterior = None
            else:
                self.ultimo = None
        else:
            actual = self.primero
            for _ in range(posicion):
                actual = actual.siguiente
            valor = actual.valor
            if actual.anterior:
                actual.anterior.siguiente = actual.siguiente
            if actual.siguiente:
                actual.siguiente.anterior = actual.anterior
            if actual == self.ultimo:
                self.ultimo = actual.anterior
        self.size -= 1
        return valor
