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
        
    def esta_vacia(self):             #retorna True si está vacia o False si no lo está
        return self.primero is None

    def agregar_al_final(self, valor):    #Agrega al final un dato introducido
        if self.esta_vacia():    
            self.primero = self.ultimo = Nodo(valor)
        else:
            auxiliar = self.ultimo
            self.ultimo = Nodo(valor)
            auxiliar.siguiente = self.ultimo
            self.ultimo.anterior = auxiliar
        self.size += 1

    def agregar_al_inicio(self, valor):  #Agrega al inicio un dato introducido
        if self.esta_vacia():
            self.primero = self.ultimo = Nodo(valor)
        else:
            auxiliar = Nodo(valor)
            auxiliar.siguiente = self.primero
            self.primero.anterior = auxiliar
            self.primero = auxiliar
        self.size += 1

    def __len__(self):     #Retorna el valor de Size, variable relacionada al tamaño de la lista
        return self.size

    def insertar(self, valor, posicion):   #Añade un dato introducido en la posicion deseada
        if not isinstance(posicion, int):   #el valor de posicion es entero?
            raise TypeError("La posición debe ser un entero")
        if posicion < 0 or posicion >= self.size: #el valor de posicion es menor que 0 o mayor que el tamaño de la lista?
            raise IndexError("Valor de posición inválido")

        auxiliar = Nodo(valor)
        if posicion == 0:     #para añadirlo en la 1era posicion
            auxiliar.siguiente = self.primero
            if self.primero:
                self.primero.anterior = auxiliar
            self.primero = auxiliar
            if self.size == 0:
                self.ultimo = auxiliar
        else:
            actual = self.primero
            for _ in range(posicion - 1):  #recorre la lista hasta la posicion deseada para posterirmente añadir el valor ingresado
                actual = actual.siguiente
            auxiliar.siguiente = actual.siguiente
            auxiliar.anterior = actual

            if actual.siguiente:
                actual.siguiente.anterior = auxiliar
            actual.siguiente = auxiliar
            if auxiliar.siguiente is None:
                self.ultimo = auxiliar
        self.size += 1

    def extraer(self, posicion=None):   #saca de la lista el valor alojado en la posicion deseada y lo retorna para utilizarlo
        if self.esta_vacia():   #la lista está vacía?
            raise IndexError("La lista está vacía")
        if posicion is None:   #Si no se ingresa un valor de posicion, la función retorna el ultimo dato de la lista
            valor = self.ultimo.valor
            if self.primero == self.ultimo:
                self.primero = self.ultimo = None
            else:
                self.ultimo = self.ultimo.anterior
                self.ultimo.siguiente = None
            self.size -= 1
            return valor

        if not isinstance(posicion, int):   #el valor posicion es entero?
            raise TypeError("La posición debe ser un entero")
        if posicion < 0 or posicion >= self.size: #el valor posicion es menos a 0 o mayor al tamaño total de la lista?
            raise IndexError("Posición ingresada inválida")

        if posicion == 0:  #extraer el 1er dato de la lista
            valor = self.primero.valor
            self.primero = self.primero.siguiente
            if self.primero:
                self.primero.anterior = None
            else:
                self.ultimo = None
        else:
            actual = self.primero
            for _ in range(posicion): #recorre la lista hasta la posicion deseada para sacar el valor de la lista y retornarlo al usuario
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

    def copia(self):    #Crea y retorna una copia de la lista doble enlazada
        copia = ListaDobleEnlazada()
        actual = self.primero
        while actual:
            copia.agregar_al_final(actual.valor)
            actual = actual.siguiente
        return copia

    def invertir(self):   #invierte el orden de la lista 
        actual = self.primero
        self.primero, self.ultimo = self.ultimo, self.primero

        while actual:
            actual.siguiente, actual.anterior = actual.anterior, actual.siguiente
            actual = actual.anterior

    def concatenar(self, lista): #conecta al final de la lista actual otra lista ingresada
        actual = lista.primero
        while actual:
            self.agregar_al_final(actual.valor)
            actual = actual.siguiente

    def __add__(self, lista):    #crea una lista nueva a partir de la suma lista actual y una ingresada como parametro
        auxiliar = self.copia()
        auxiliar.concatenar(lista)
        return auxiliar
