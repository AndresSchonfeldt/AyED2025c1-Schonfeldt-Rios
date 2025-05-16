# Archivo de test para realizar pruebas unitarias del modulo1
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 14:00:21 2022
@author: Catedra de Algoritmos y Estructura de Datos
"""
import sys
import os
import unittest
import random

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Problema_2.modules.Lista_doble_enlazada import ListaDobleEnlazada


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


class Test_LDE(unittest.TestCase):
    """Test de la clase ListaDobleEnlazada"""

    def setUp(self):
        self.n_elementos = 200

        # LDE vacía
        self.lde_1 = ListaDobleEnlazada()

        # LDE con elementos repetidos
        self.lde_2 = ListaDobleEnlazada()
        self.lista_aux_2 = random.choices(range(-self.n_elementos // 2, self.n_elementos // 2), k=self.n_elementos)
        for item in self.lista_aux_2:
            self.lde_2.agregar_al_final(item)

        # LDE con elementos únicos
        self.lde_3 = ListaDobleEnlazada()
        self.lista_aux_3 = random.sample(range(-self.n_elementos, self.n_elementos), self.n_elementos)
        for item in self.lista_aux_3:
            self.lde_3.agregar_al_final(item)

    def recorrer_lista(self, lista):
        """Verifica la correcta conexión de los nodos"""
        nodo = lista.primero
        while nodo:
            if nodo.siguiente and nodo.siguiente.anterior != nodo:
                self.fail("Los nodos no están correctamente enlazados")
            nodo = nodo.siguiente

    def test_excepciones_extraer(self):
        """Prueba la extracción en listas vacías y posiciones inválidas"""
        with self.assertRaises(Exception):
            self.lde_1.extraer()
        with self.assertRaises(Exception):
            self.lde_1.extraer(0)

    def test_operador_len(self):
        """Prueba el operador len()"""
        self.assertEqual(len(self.lde_1), 0)
        self.assertEqual(len(self.lde_2), self.n_elementos)

    def test_copiar(self):
        """Prueba la copia de una lista enlazada"""
        lde_3_copia = self.lde_3.copia()
        self.recorrer_lista(lde_3_copia)

    def test_invertir(self):
        """Prueba el método invertir"""
        self.lde_1.invertir()
        self.recorrer_lista(self.lde_1)

    def test_metodo_concatenar(self):
        """Prueba el método concatenar"""
        lista_concatenada = self.lde_3.copia()
        lista_concatenada.concatenar(self.lde_2)
        self.recorrer_lista(lista_concatenada)

    def test_operador_add(self):
        """Prueba la concatenación con el operador '+'"""
        lista_concatenada = self.lde_3 + self.lde_2
        self.recorrer_lista(lista_concatenada)


if __name__ == "__main__":
    unittest.main()
