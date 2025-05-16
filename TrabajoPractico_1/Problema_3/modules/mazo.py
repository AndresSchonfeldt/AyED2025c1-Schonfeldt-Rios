from modules.lista_doble import ListaDobleEnlazada
from modules.carta import Carta

class DequeEmptyError(Exception):
    pass

class Mazo:
    def __init__(self):
        self.cartas = ListaDobleEnlazada()

    def poner_carta_arriba(self, carta):
        self.cartas.agregar_al_final(carta)

    def sacar_carta_arriba(self, mostrar=False):
        if len(self.cartas) == 0:
            raise DequeEmptyError("El mazo está vacío")
        carta = self.cartas.extraer()
        if mostrar:
            carta.visible = True
        return carta

    def poner_carta_abajo(self, carta):
        self.cartas.agregar_al_inicio(carta)

    def __len__(self):
        return len(self.cartas)

    def __str__(self):
        resultado = []
        actual = self.cartas.primero
        while actual:
            resultado.append(str(actual.valor))
            actual = actual.siguiente
        return ' '.join(resultado)
