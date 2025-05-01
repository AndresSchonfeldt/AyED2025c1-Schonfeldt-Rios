import turtle # Importa el módulo turtle para gráficos
import random # Importa el módulo random para generar números aleatorios
import time # Importa el módulo time para controlar el tiempo

class DequeEmptyError(Exception): # Define una excepción personalizada para indicar que un deque está vacío
    pass

class Mazo: # Define la clase Mazo para representar una baraja de cartas
    def __init__(self): # Constructor de la clase Mazo
        self.cartas = [] # Inicializa la lista de cartas

    def poner_carta_arriba(self, carta): # Define el método para añadir una carta al final del mazo
        self.cartas.append(carta) # Añade la carta a la lista

    def sacar_carta_arriba(self, mostrar=False): # Define el método para sacar una carta del final del mazo
        if not self.cartas: # Comprueba si el mazo está vacío
            raise DequeEmptyError("El mazo está vacío") # Lanza una excepción si el mazo está vacío
        carta = self.cartas.pop() # Saca la última carta del mazo
        if mostrar: # Comprueba si la carta debe mostrarse
            carta.visible = True # Hace la carta visible
        return carta # Devuelve la carta

    def poner_carta_abajo(self, carta): # Define el método para poner una carta al principio del mazo
        self.cartas.insert(0, carta) # Inserta la carta al principio de la lista

    def __len__(self): # Define el método para obtener el número de cartas en el mazo
        return len(self.cartas) # Devuelve el número de cartas en la lista

    def __str__(self): # Define el método para convertir el mazo en una cadena
        return ' '.join(str(carta) for carta in self.cartas) # Devuelve una cadena con las cartas separadas por espacios

class Carta: # Define la clase Carta para representar una carta
    def __init__(self, valor='', palo=''): # Constructor de la clase Carta
        self.valor = valor # Inicializa el valor de la carta
        self.palo = palo # Inicializa el palo de la carta
        self.visible:bool = False # Inicializa la visibilidad de la carta

    @property # Define la propiedad visible
    def visible(self): # Define el getter de la propiedad visible
        return self._visible # Devuelve el valor de la propiedad visible

    @visible.setter # Define el setter de la propiedad visible
    def visible(self, visible): # Define el método para establecer el valor de la propiedad visible
        self._visible = visible # Establece el valor de la propiedad visible

    @property # Define la propiedad valor
    def valor(self): # Define el getter de la propiedad valor
        return self._valor # Devuelve el valor de la propiedad valor

    @valor.setter # Define el setter de la propiedad valor
    def valor(self, valor): # Define el método para establecer el valor de la propiedad valor
        self._valor = valor # Establece el valor de la propiedad valor

    @property # Define la propiedad palo
    def palo(self): # Define el getter de la propiedad palo
        return self._palo # Devuelve el valor de la propiedad palo

    @palo.setter # Define el setter de la propiedad palo
    def palo(self, palo): # Define el método para establecer el valor de la propiedad palo
        self._palo = palo # Establece el valor de la propiedad palo

    def _valor_numerico(self): # Define el método para obtener el valor numérico de la carta
        valores = ['J','Q','K','A'] # Define la lista de valores especiales
        if self.valor in valores: # Comprueba si el valor de la carta está en la lista de valores especiales
            idx = valores.index(self.valor) # Obtiene el índice del valor en la lista
            return (11 + idx) # Devuelve el valor numérico de la carta
        return int(self.valor) # Devuelve el valor numérico de la carta

    def __gt__(self, otra): # Define el método para comparar dos cartas
        """2 cartas deben compararse por su valor numérico""" # Documentación del método
        return self._valor_numerico() > otra._valor_numerico() # Compara los valores numéricos de las cartas

    def __str__(self): # Define el método para convertir la carta en una cadena
        if self.visible == False: # Comprueba si la carta es visible
            return "-X" # Devuelve "-X" si la carta no es visible
        else: # Si la carta es visible
            return self.valor + self.palo # Devuelve el valor y el palo de la carta

    def __repr__(self): # Define el método para representar la carta
        return str(self) # Devuelve la cadena de la carta
