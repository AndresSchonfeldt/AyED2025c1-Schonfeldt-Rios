# módulo para organizar funciones o clases utilizadas en nuestro proyecto
# Crear tantos módulos como sea necesario para organizar el código
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

    def insertar(self, valor, posicion):
        if not isinstance(posicion, int):
            raise TypeError("La posición debe ser un entero")
        if posicion < 0 or posicion >= self.size:
            raise IndexError("Valor de posición inválido")

        auxiliar = Nodo(valor)
        if posicion == 0:
            auxiliar.siguiente = self.primero
            if self.primero:
                self.primero.anterior = auxiliar
            self.primero = auxiliar
            if self.size == 0:
                self.ultimo = auxiliar
        else:
            actual = self.primero
            for _ in range(posicion - 1):
                actual = actual.siguiente
            auxiliar.siguiente = actual.siguiente
            auxiliar.anterior = actual

            if actual.siguiente:
                actual.siguiente.anterior = auxiliar
            actual.siguiente = auxiliar
            if auxiliar.siguiente is None:
                self.ultimo = auxiliar
        self.size += 1

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

    def copia(self):
        copia = ListaDobleEnlazada()
        actual = self.primero
        while actual:
            copia.agregar_al_final(actual.valor)
            actual = actual.siguiente
        return copia

    def invertir(self):
        actual = self.primero
        self.primero, self.ultimo = self.ultimo, self.primero

        while actual:
            actual.siguiente, actual.anterior = actual.anterior, actual.siguiente
            actual = actual.anterior

    def concatenar(self, lista):
        actual = lista.primero
        while actual:
            self.agregar_al_final(actual.valor)
            actual = actual.siguiente

    def __add__(self, lista):
        auxiliar = self.copia()
        auxiliar.concatenar(lista)
        return auxiliar
