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
        return self.primero ==  None #Devuelve true si está vacia o false si contiene un elemento
    
    def agregar_al_final(self,valor):
        if self.esta_vacia():
            self.primero = self.ultimo = None
        else:
            auxiliar = self.ultimo
            self.ultimo = auxiliar.siguiente = Nodo(valor)
            self.ultimo.anterior = auxiliar
        self.size += 1
    
    
    def agregar_al_inicio(self, valor):
        if self.vacio():
            self.primero= self.ultimo = Nodo(valor)
        else:
            auxiliar = Nodo(valor)
            auxiliar.siguiente = self.primero
            self.primero.anterior = None
            self.primero = auxiliar
            
        self.size += 1
        
    def __len__(self):
        return self.size
        
            
            
            
    def insertar(self,valor, posicion):
        auxiliar = Nodo(valor)
        if posicion == None: #Agrega al final
            if self.esta_vacia() == True:
                self.primero = self.ultimo = auxiliar
            else:
                self.ultimo.siguiente = auxiliar
                auxiliar.anterior = self.ultimo
                self.ultimo = auxiliar
                
            
           
        if posicion != type(int):
            raise TypeError("La posicion debe ser un entero")
        if posicion < 0 or posicion >= self.size:
            raise IndexError("valor de posicion invalido")
        
        if posicion == 0: #Agrega al inicio
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
            if auxiliar.siguiente == None:
                self.ultimo = auxiliar
        self.size +=1

def extraer(self, posicion):
    if self.esta_vacia() == True:
        raise IndexError("La lista está vacía")
    if posicion == None: #extraer del final
        valor= self.ultimo.valor
        if self.primero == self.ultimo:
            self.primero = self.primero = None
        else:
            self.ultimo = self.ultimo.anterior
            self.ultimo.siguiente = None
        self.size -=1
        return valor
    
    if posicion != type(int):
        raise TypeError("posicion debe ser un entero")
    if posicion < 0 or posicion >= self.size:
        raise IndexError("Posicion ingresa invalida")
    
    if posicion == 0: #extraer del inicio
        valor = self.primero.valor
        self.primero = self.primero.siguiente
        if self.primero:
            self.primero.anterior = None
        else: 
            self.ultimo= None
    else:
        actual = self.primero
        for _ in range (posicion):
            actual= actual.siguiente
        valor= actual.valor
        if actual.anterior:
            actual.anterior.siguiente= actual.siguiente
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
        copia.insertar(actual.valor) #Agrega al final
        actual = actual.siguiente
    return copia

def invertir(self):
    actual = self.primero
    self.primero, self.ultimo = self.ultimo, self.primero #intercambia cabezas
    
    while actual:
        actual.siguiente, actual.anterior = actual.anterior, actual.siguiente #Intercambio de punteros del nodo actual
        actual = actual.anterior #Moverlo al siguiente nodo
        
    
def concatenar(self, lista):
    
    actual = lista.primero
    while actual:
        self.insertar(actual.valor)  #Agrega al final
        actual= actual.siguiente
    
def __add__(self, lista):
    
    auxiliar = self.copiar()     #copia la primera lista
    auxiliar.concatenar(lista)   #añade los elementos
    return auxiliar