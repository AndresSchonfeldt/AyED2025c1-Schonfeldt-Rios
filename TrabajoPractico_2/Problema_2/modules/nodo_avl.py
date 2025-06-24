import datetime

class NodoAVL:
    def __init__(self, clave, valor):
        if not isinstance(clave, datetime.date):
            raise TypeError("La clave debe ser un objeto datetime.date.")
        self.clave = clave
        self.valor = valor
        self.izquierda = None
        self.derecha = None
        self.altura = 1
