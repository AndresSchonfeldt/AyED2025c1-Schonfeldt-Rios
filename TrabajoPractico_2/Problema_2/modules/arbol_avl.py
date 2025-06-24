from modules.nodo_avl import NodoAVL

class ArbolAVL:
    def __init__(self):
        self.raiz = None
        self._cantidad = 0

    def insertar(self, clave, valor):
        self.raiz = self._insertar(self.raiz, clave, valor)

    def eliminar(self, clave):
        conteo = self._cantidad
        self.raiz = self._eliminar(self.raiz, clave)
        return self._cantidad < conteo

    def buscar(self, clave):
        actual = self.raiz
        while actual:
            if clave < actual.clave:
                actual = actual.izquierda
            elif clave > actual.clave:
                actual = actual.derecha
            else:
                return actual.valor
        return None

    def recorrido_rango(self, clave1, clave2):
        lista = []
        self._recorrido_en_orden(self.raiz, clave1, clave2, lista)
        return lista

    def cantidad(self):
        return self._cantidad

    def _obtener_altura(self, nodo):
        return nodo.altura if nodo else 0

    def _actualizar_altura(self, nodo):
        nodo.altura = 1 + max(self._obtener_altura(nodo.izquierda), self._obtener_altura(nodo.derecha))

    def _balance(self, nodo):
        return self._obtener_altura(nodo.izquierda) - self._obtener_altura(nodo.derecha) if nodo else 0

    def _rotar_izquierda(self, x):
        y = x.derecha
        T2 = y.izquierda
        y.izquierda = x
        x.derecha = T2
        self._actualizar_altura(x)
        self._actualizar_altura(y)
        return y

    def _rotar_derecha(self, y):
        x = y.izquierda
        T2 = x.derecha
        x.derecha = y
        y.izquierda = T2
        self._actualizar_altura(y)
        self._actualizar_altura(x)
        return x

    def _insertar(self, nodo, clave, valor):
        if not nodo:
            self._cantidad += 1
            return NodoAVL(clave, valor)

        if clave < nodo.clave:
            nodo.izquierda = self._insertar(nodo.izquierda, clave, valor)
        elif clave > nodo.clave:
            nodo.derecha = self._insertar(nodo.derecha, clave, valor)
        else:
            nodo.valor = valor
            return nodo

        self._actualizar_altura(nodo)
        balance = self._balance(nodo)

        if balance > 1 and clave < nodo.izquierda.clave:
            return self._rotar_derecha(nodo)
        if balance < -1 and clave > nodo.derecha.clave:
            return self._rotar_izquierda(nodo)
        if balance > 1 and clave > nodo.izquierda.clave:
            nodo.izquierda = self._rotar_izquierda(nodo.izquierda)
            return self._rotar_derecha(nodo)
        if balance < -1 and clave < nodo.derecha.clave:
            nodo.derecha = self._rotar_derecha(nodo.derecha)
            return self._rotar_izquierda(nodo)

        return nodo

    def _nodo_min(self, nodo):
        while nodo.izquierda:
            nodo = nodo.izquierda
        return nodo

    def _eliminar(self, nodo, clave):
        if not nodo:
            return nodo

        if clave < nodo.clave:
            nodo.izquierda = self._eliminar(nodo.izquierda, clave)
        elif clave > nodo.clave:
            nodo.derecha = self._eliminar(nodo.derecha, clave)
        else:
            if not nodo.izquierda or not nodo.derecha:
                nodo = nodo.izquierda or nodo.derecha
                self._cantidad -= 1
            else:
                sucesor = self._nodo_min(nodo.derecha)
                nodo.clave = sucesor.clave
                nodo.valor = sucesor.valor
                nodo.derecha = self._eliminar(nodo.derecha, sucesor.clave)

        if not nodo:
            return nodo

        self._actualizar_altura(nodo)
        balance = self._balance(nodo)

        if balance > 1 and self._balance(nodo.izquierda) >= 0:
            return self._rotar_derecha(nodo)
        if balance > 1 and self._balance(nodo.izquierda) < 0:
            nodo.izquierda = self._rotar_izquierda(nodo.izquierda)
            return self._rotar_derecha(nodo)
        if balance < -1 and self._balance(nodo.derecha) <= 0:
            return self._rotar_izquierda(nodo)
        if balance < -1 and self._balance(nodo.derecha) > 0:
            nodo.derecha = self._rotar_derecha(nodo.derecha)
            return self._rotar_izquierda(nodo)

        return nodo

    def _recorrido_en_orden(self, nodo, ini, fin, lista):
        if not nodo:
            return
        if ini < nodo.clave:
            self._recorrido_en_orden(nodo.izquierda, ini, fin, lista)
        if ini <= nodo.clave <= fin:
            lista.append((nodo.clave, nodo.valor))
        if fin > nodo.clave:
            self._recorrido_en_orden(nodo.derecha, ini, fin, lista)
