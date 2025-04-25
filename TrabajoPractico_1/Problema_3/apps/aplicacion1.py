import turtle
import random
from modules.modulo1 import Mazo, Carta, DequeEmptyError # Importa las clases Mazo, Carta y DequeEmptyError del módulo modules
import time # Importa el módulo time para controlar el tiempo de ejecución


class JuegoGuerra: # Define la clase JuegoGuerra para representar el juego
    valores = ['2','3','4','5','6','7','8','9','10','J','Q','K','A'] # Define los valores de las cartas
    palos = ['♠', '♥', '♦', '♣'] # Define los palos de las cartas
    VICTORIA = 10 # Define el número de victorias necesarias para ganar

    def __init__(self, random_seed = 0): # Constructor de la clase JuegoGuerra
        self._mazo_inicial = Mazo() # Inicializa el mazo inicial
        self.mazo_1 = Mazo() # Inicializa el mazo del jugador 1
        self.mazo_2 = Mazo() # Inicializa el mazo del jugador 2
        self._guerra = False # Inicializa la variable de guerra
        self._ganador = '' # Inicializa la variable del ganador
        self.empate = False # Inicializa la variable de empate
        self._turno = 0 # Inicializa el número de turno
        self._cartas_en_la_mesa = [] # Inicializa la lista de cartas en la mesa
        self._seed = random_seed # Inicializa la semilla aleatoria
        self.jugador1_ganadas = 0 # Inicializa el número de victorias del jugador 1
        self.jugador2_ganadas = 0 # Inicializa el número de victorias del jugador 2
        self._setup_turtle() # Inicializa la interfaz turtle

    @property # Define la propiedad mazo_1
    def mazo_1(self): # Define el getter de la propiedad mazo_1
        return self._mazo_1 # Devuelve el valor de la propiedad mazo_1

    @mazo_1.setter # Define el setter de la propiedad mazo_1
    def mazo_1(self, valor): # Define el método para establecer el valor de la propiedad mazo_1
        self._mazo_1 = valor # Establece el valor de la propiedad mazo_1

    @property # Define la propiedad mazo_2
    def mazo_2(self): # Define el getter de la propiedad mazo_2
        return self._mazo_2 # Devuelve el valor de la propiedad mazo_2

    @mazo_2.setter # Define el setter de la propiedad mazo_2
    def mazo_2(self, valor): # Define el método para establecer el valor de la propiedad mazo_2
        self._mazo_2 = valor # Establece el valor de la propiedad mazo_2

    @property # Define la propiedad empate
    def empate(self): # Define el getter de la propiedad empate
        return self._empate # Devuelve el valor de la propiedad empate

    @empate.setter # Define el setter de la propiedad empate
    def empate(self, valor): # Define el método para establecer el valor de la propiedad empate
        self._empate = valor # Establece el valor de la propiedad empate

    @property # Define la propiedad ganador
    def ganador(self): # Define el getter de la propiedad ganador
        return self._ganador # Devuelve el valor de la propiedad ganador

    def _setup_turtle(self): # Define el método para inicializar la interfaz turtle
        self.screen = turtle.Screen() # Inicializa la pantalla
        self.screen.setup(width=800, height=600) # Establece el tamaño de la pantalla
        self.screen.title("Juego de Guerra") # Establece el título de la pantalla
        self.screen.bgcolor("white") # Establece el color de fondo de la pantalla
        self.screen.tracer(5)  # Velocidad muy lenta # Ajusta la velocidad de la animación

        # Configurar tortugas para visualización
        self.t_jugador1 = turtle.Turtle() # Inicializa la tortuga del jugador 1
        self.t_jugador2 = turtle.Turtle() # Inicializa la tortuga del jugador 2
        self.t_mesa = turtle.Turtle() # Inicializa la tortuga de la mesa
        self.t_info = turtle.Turtle()  # Nueva tortuga para información # Inicializa la tortuga de información

        self._configurar_tortugas() # Configura las tortugas

    def _configurar_tortugas(self): # Define el método para configurar las tortugas
        for t in [self.t_jugador1, self.t_jugador2, self.t_mesa, self.t_info]: # Itera sobre las tortugas
            t.hideturtle() # Oculta la tortuga
            t.penup() # Levanta el lápiz
            t.speed(0) # Establece la velocidad de la tortuga a la máxima

        self.t_jugador1.goto(-300, 0) # Establece la posición de la tortuga del jugador 1
        self.t_jugador2.goto(300, 0) # Establece la posición de la tortuga del jugador 2
        self.t_mesa.goto(0, 200) # Establece la posición de la tortuga de la mesa
        self.t_info.goto(0, -200)  # Posición para la información # Establece la posición de la tortuga de información

    def armar_mazo_inicial(self): # Define el método para armar el mazo inicial
        """representa el mazo inicial, este mazo se crea al inicio
        de cada partida mediante combinación de los números y palos
        de la baraja para formar cartas
        """ # Documentación del método
        random.seed(self._seed) # Establece la semilla aleatoria
        cartas = [Carta(valor, palo) for valor in JuegoGuerra.valores # Crea una lista de cartas
                  for palo in JuegoGuerra.palos] # Itera sobre los valores y palos

        #cartas_shuffled = random.sample(cartas, len(cartas))
        random.shuffle(cartas) # Mezcla las cartas
        cartas_shuffled = cartas # Asigna las cartas mezcladas a una variable

        for carta in cartas_shuffled: # Itera sobre las cartas mezcladas
            self._mazo_inicial.poner_carta_arriba(carta) # Añade la carta al mazo inicial

        return self._mazo_inicial # Devuelve el mazo inicial

    def repartir_cartas(self): # Define el método para repartir las cartas
        """reparte el mazo inicial entre los dos jugadores""" # Documentación del método
        while len(self._mazo_inicial): # Mientras haya cartas en el mazo inicial
            carta_1 = self._mazo_inicial.sacar_carta_arriba() # Saca una carta del mazo inicial
            self.mazo_1.poner_carta_arriba(carta_1) # Añade la carta al mazo del jugador 1
            carta_2 = self._mazo_inicial.sacar_carta_arriba() # Saca una carta del mazo inicial
            self.mazo_2.poner_carta_arriba(carta_2) # Añade la carta al mazo del jugador 2

        return self.mazo_1, self.mazo_2 # Devuelve los mazos de los jugadores

    def iniciar_juego(self, ver_partida=True): # Define el método para iniciar el juego
        self.jugador1_ganadas = 0 # Reinicia el contador de victorias del jugador 1
        self.jugador2_ganadas = 0 # Reinicia el contador de victorias del jugador 2
        self.armar_mazo_inicial() # Arma el mazo inicial
        self.repartir_cartas() # Reparte las cartas
        self._cartas_en_la_mesa = [] # Reinicia la lista de cartas en la mesa
        self._turno = 0 # Reinicia el contador de turnos

        while self.jugador1_ganadas < JuegoGuerra.VICTORIA and self.jugador2_ganadas < JuegoGuerra.VICTORIA: # Mientras ningún jugador haya alcanzado el número de victorias necesarias para ganar
            self._turno += 1 # Incrementa el número de turno
            try: # Intenta
                if self._guerra: # Comprueba si hay guerra
                    for _ in range(3): # Itera 3 veces
                        self._cartas_en_la_mesa.append(self.mazo_1.sacar_carta_arriba()) # Añade una carta del mazo del jugador 1 a la mesa
                        self._cartas_en_la_mesa.append(self.mazo_2.sacar_carta_arriba()) # Añade una carta del mazo del jugador 2 a la mesa
                        time.sleep(0.5) # Pausa adicional en guerra # Añade una pausa

                carta1 = self.mazo_1.sacar_carta_arriba(mostrar=True) # Saca una carta del mazo del jugador 1
                carta2 = self.mazo_2.sacar_carta_arriba(mostrar=True) # Saca una carta del mazo del jugador 2
                self._cartas_en_la_mesa.extend([carta1, carta2]) # Añade las cartas a la mesa

            except DequeEmptyError: # Si ocurre una excepción DequeEmptyError
                if len(self.mazo_1): # Comprueba si el jugador 1 tiene cartas
                    self._ganador = 'jugador 1' # El jugador 1 es el ganador
                else: # Si el jugador 1 no tiene cartas
                    self._ganador = 'jugador 2' # El jugador 2 es el ganador
                self._guerra = False # No hay guerra
                break # Sale del bucle

            else: # Si no ocurre ninguna excepción
                self._actualizar_display(carta1, carta2) # Actualiza la interfaz
                time.sleep(1.5)  # Pausa antes de comparar cartas # Añade una pausa

                if  carta1 > carta2: # Comprueba si la carta del jugador 1 es mayor que la del jugador 2
                    self._transferir_cartas(self.mazo_1) # Transfiere las cartas al jugador 1
                    self._guerra = False # No hay guerra
                    self.jugador1_ganadas += 1 # Incrementa el número de victorias del jugador 1
                elif  carta2 > carta1: # Comprueba si la carta del jugador 2 es mayor que la del jugador 1
                    self._transferir_cartas(self.mazo_2) # Transfiere las cartas al jugador 2
                    self._guerra = False # No hay guerra
                    self.jugador2_ganadas += 1 # Incrementa el número de victorias del jugador 2
                else: # Si las cartas son iguales
                    self._guerra = True # Hay guerra
                    self._mostrar_guerra() # Muestra el mensaje de guerra

            time.sleep(1) # Pausa después de cada turno # Añade una pausa

        self._mostrar_resultado_final() # Muestra el resultado final
        turtle.done() # Finaliza la ejecución de turtle

    def _actualizar_display(self, carta1, carta2): # Define el método para actualizar la interfaz
        self.t_jugador1.clear() # Limpia la tortuga del jugador 1
        self.t_jugador2.clear() # Limpia la tortuga del jugador 2
        self.t_mesa.clear() # Limpia la tortuga de la mesa
        self.t_info.clear() # Limpia la tortuga de información

        # Mostrar cartas en la mesa
        self.t_mesa.goto(-100, 100) # Establece la posición de la tortuga de la mesa
        self.t_mesa.write(str(carta1), align="center", font=("Arial", 24, "bold")) # Escribe la carta del jugador 1
        self.t_mesa.goto(100, 100) # Establece la posición de la tortuga de la mesa
        self.t_mesa.write(str(carta2), align="center", font=("Arial", 24, "bold")) # Escribe la carta del jugador 2

        # Mostrar conteo de cartas y nombre del jugador
        self.t_jugador1.goto(-300, 0) # Establece la posición de la tortuga del jugador 1
        self.t_jugador1.write(f"Jugador 1\nCartas: {len(self.mazo_1)}\nGanadas: {self.jugador1_ganadas}", # Escribe la información del jugador 1
                            align="center", font=("Arial", 16, "normal")) # Establece la alineación y la fuente
        self.t_jugador2.goto(300, 0) # Establece la posición de la tortuga del jugador 2
        self.t_jugador2.write(f"Jugador 2\nCartas: {len(self.mazo_2)}\nGanadas: {self.jugador2_ganadas}", # Escribe la información del jugador 2
                            align="center", font=("Arial", 16, "normal")) # Establece la alineación y la fuente

        # Mostrar el turno actual
        self.t_info.goto(0, -200) # Establece la posición de la tortuga de información
        self.t_info.write(f"Turno: {self._turno}", # Escribe el número de turno
                            align="center", font=("Arial", 16, "normal")) # Establece la alineación y la fuente
        self.screen.update() # Actualiza la pantalla

    def _mostrar_guerra(self): # Define el método para mostrar el mensaje de guerra
        self.t_mesa.clear() # Limpia la tortuga de la mesa
        self.t_mesa.write("¡GUERRA!", align="center", font=("Arial", 32, "bold")) # Escribe el mensaje de guerra
        self.screen.update() # Actualiza la pantalla
        time.sleep(0.5) # Añade una pausa

    def _transferir_cartas(self, ganador): # Define el método para transferir las cartas al ganador
        for carta in self._cartas_en_la_mesa: # Itera sobre las cartas en la mesa
            ganador.poner_carta_abajo(carta) # Añade la carta al mazo del ganador
        self._cartas_en_la_mesa = [] # Reinicia la lista de cartas en la mesa
        self._guerra = False # No hay guerra

    def _mostrar_resultado_final(self): # Define el método para mostrar el resultado final
        self.t_mesa.clear() # Limpia la tortuga de la mesa
        ganador = "" # Inicializar con un valor por defecto
        if self.jugador1_ganadas >= JuegoGuerra.VICTORIA: # Comprueba si el jugador 1 ha ganado
            ganador = "Jugador 1" # El jugador 1 es el ganador
        elif self.jugador2_ganadas >= JuegoGuerra.VICTORIA: # Comprueba si el jugador 2 ha ganado
            ganador = "Jugador 2" # El jugador 2 es el ganador
        
        resultado_text = ( # Define el texto del resultado
            f"¡{ganador} gana!\n" # Añade el nombre del ganador
            f"Jugador 1 Ganadas: {self.jugador1_ganadas}\n" # Añade el número de victorias del jugador 1
            f"Jugador 2 Ganadas: {self.jugador2_ganadas}\n" # Añade el número de victorias del jugador 2
            f"Turnos Jugados: {self._turno}" # Añade el número de turnos jugados
        )

        self.t_mesa.write(resultado_text, align="center", font=("Arial", 20, "bold")) # Escribe el texto del resultado
        self.screen.update() # Actualiza la pantalla
        time.sleep(5) # Añade una pausa


if __name__ == "__main__": # Si el script se ejecuta directamente
    random_seed = random.randint(0, 1000) # Genera una semilla aleatoria
    juego = JuegoGuerra(random_seed) # Crea un objeto JuegoGuerra
    juego.iniciar_juego() # Inicia el juego

# Aplicación secundaria
