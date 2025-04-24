import turtle
import random
import time

# Configuración de la pantalla
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("white")
screen.title("Juego de Guerra - Mejor de 3")
screen.tracer(0)  # Desactiva la actualización automática de la pantalla

# Registro de formas para las cartas (puedes personalizar esto)
screen.register_shape("carta_boca_abajo", ((-20, -30), (-20, 30), (20, 30), (20, -30)))

# Clase para representar una carta
class Carta:
    def __init__(self, valor='', palo=''):
        self.valor = valor
        self.palo = palo
        self.visible: bool = False

    @property
    def visible(self):
        return self._visible

    @visible.setter
    def visible(self, visible):
        self._visible = visible

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, valor):
        self._valor = valor

    @property
    def palo(self):
        return self._palo

    @palo.setter
    def palo(self, palo):
        self._palo = palo

    def _valor_numerico(self):
        valores = ['J', 'Q', 'K', 'A']
        if self.valor in valores:
            idx = valores.index(self.valor)
            return (11 + idx)
        return int(self.valor)

    def __gt__(self, otra):
        """2 cartas deben compararse por su valor numérico"""
        return self._valor_numerico() > otra._valor_numerico()

    def __str__(self):
        if not self.visible:
            return "-X"
        else:
            return self.valor + self.palo

    def __repr__(self):
        return str(self)

# Clase para representar un mazo (usando una lista simple en lugar de Deque)
class Mazo:
    def __init__(self):
        self.cartas = []

    def poner_carta_arriba(self, carta):
        self.cartas.append(carta)

    def sacar_carta_arriba(self, mostrar=False):
        if not self.cartas:
            raise IndexError("Mazo vacío")
        carta = self.cartas.pop()
        carta.visible = mostrar
        return carta

    def poner_carta_abajo(self, carta):
        self.cartas.insert(0, carta)

    def __len__(self):
        return len(self.cartas)

    def __str__(self):
        return ' '.join(str(carta) for carta in self.cartas)

# Clase principal del juego
class JuegoGuerra:
    valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    palos = ['♠', '♥', '♦', '♣']
    N_TURNOS = 10000
    DELAY = 0.4  # Aumentar el delay para un juego más lento
    MAX_TIME_PER_GAME = 8  # Aumentar el tiempo máximo por partida

    def __init__(self, random_seed=None):
        if random_seed is None:
            self._seed = random.randint(0, 1000)  # Semilla aleatoria si no se proporciona
        else:
            self._seed = random_seed
        random.seed(self._seed)

        self._mazo_inicial = Mazo()
        self.mazo_1 = Mazo()
        self.mazo_2 = Mazo()
        self._guerra = False
        self._ganador = ''
        self.empate = False
        self._turno = 0
        self._cartas_en_la_mesa = []
        self.jugador1_turtle = turtle.Turtle()
        self.jugador2_turtle = turtle.Turtle()
        self.mesa_turtle = turtle.Turtle()
        self.carta1_turtle = turtle.Turtle()  # Tortuga para mostrar la carta del jugador 1
        self.carta2_turtle = turtle.Turtle()  # Tortuga para mostrar la carta del jugador 2
        self.marcador_turtle = turtle.Turtle()  # Tortuga para mostrar el marcador
        self.configurar_tortugas()
        self.puntaje_jugador1 = 0
        self.puntaje_jugador2 = 0

    def configurar_tortugas(self):
        # Configuración de la tortuga del jugador 1
        self.jugador1_turtle.speed(0)
        self.jugador1_turtle.hideturtle()
        self.jugador1_turtle.penup()
        self.jugador1_turtle.goto(-300, -100)
        self.jugador1_turtle.color("blue")

        # Configuración de la tortuga del jugador 2
        self.jugador2_turtle.speed(0)
        self.jugador2_turtle.hideturtle()
        self.jugador2_turtle.penup()
        self.jugador2_turtle.goto(300, -100)
        self.jugador2_turtle.color("red")

        # Configuración de la tortuga de la mesa
        self.mesa_turtle.speed(0)
        self.mesa_turtle.hideturtle()
        self.mesa_turtle.penup()
        self.mesa_turtle.goto(0, 100)  # Ajusta la posición vertical
        self.mesa_turtle.color("black")

        # Configuración de las tortugas para mostrar las cartas
        self.carta1_turtle.speed(0)
        self.carta1_turtle.hideturtle()
        self.carta1_turtle.penup()
        self.carta1_turtle.goto(-150, 0)  # Posición para la carta del jugador 1

        self.carta2_turtle.speed(0)
        self.carta2_turtle.hideturtle()
        self.carta2_turtle.penup()
        self.carta2_turtle.goto(150, 0)  # Posición para la carta del jugador 2

        # Configuración de la tortuga para mostrar el marcador
        self.marcador_turtle.speed(0)
        self.marcador_turtle.hideturtle()
        self.marcador_turtle.penup()
        self.marcador_turtle.goto(0, -200)
        self.marcador_turtle.color("black")

    def armar_mazo_inicial(self):
        """representa el mazo inicial, este mazo se crea al inicio
        de cada partida mediante combinación de los números y palos
        de la baraja para formar cartas
        """
        cartas = [Carta(valor, palo) for valor in JuegoGuerra.valores
                  for palo in JuegoGuerra.palos]

        random.shuffle(cartas)

        for carta in cartas:
            self._mazo_inicial.poner_carta_arriba(carta)

        return self._mazo_inicial

    def repartir_cartas(self):
        """reparte el mazo inicial entre los dos jugadores"""
        while len(self._mazo_inicial):
            carta_1 = self._mazo_inicial.sacar_carta_arriba()
            self.mazo_1.poner_carta_arriba(carta_1)
            carta_2 = self._mazo_inicial.sacar_carta_arriba()
            self.mazo_2.poner_carta_arriba(carta_2)

        return self.mazo_1, self.mazo_2

    def iniciar_juego(self, ver_partida=True):
        self.puntaje_jugador1 = 0
        self.puntaje_jugador2 = 0
        self.actualizar_marcador()

        while self.puntaje_jugador1 < 2 and self.puntaje_jugador2 < 2:
            ganador_partida = self.jugar_partida()
            if ganador_partida == 'jugador 1':
                self.puntaje_jugador1 += 1
            elif ganador_partida == 'jugador 2':
                self.puntaje_jugador2 += 1
            self.actualizar_marcador()
            time.sleep(1)  # Pausa entre partidas

        if self.puntaje_jugador1 > self.puntaje_jugador2:
            ganador_final = 'jugador 1'
        else:
            ganador_final = 'jugador 2'

        self.mostrar_ganador_final(ganador_final)

    def jugar_partida(self):
        self._mazo_inicial = Mazo()
        self.mazo_1 = Mazo()
        self.mazo_2 = Mazo()
        self._guerra = False
        self._ganador = ''
        self.empate = False
        self._turno = 0
        self._cartas_en_la_mesa = []

        self.armar_mazo_inicial()
        self.repartir_cartas()

        self.dibujar_mazos_iniciales()
        start_time = time.time()

        while len(self.mazo_1) and len(self.mazo_2) and (time.time() - start_time) < self.MAX_TIME_PER_GAME:
            try:
                # Sacar cartas para el turno actual
                carta_jugador1 = self.mazo_1.sacar_carta_arriba(mostrar=True)
                carta_jugador2 = self.mazo_2.sacar_carta_arriba(mostrar=True)
                self._cartas_en_la_mesa.append(carta_jugador1)
                self._cartas_en_la_mesa.append(carta_jugador2)
                self.dibujar_cartas_en_mesa(carta_jugador1, carta_jugador2)
                self.actualizar_pantalla()
                time.sleep(JuegoGuerra.DELAY)

            except IndexError:
                if len(self.mazo_1):
                    self._ganador = 'jugador 1'
                else:
                    self._ganador = 'jugador 2'
                self._guerra = False
                break
            else:
                # Determinar el ganador del turno
                if carta_jugador1 > carta_jugador2:
                    ganador = 1
                elif carta_jugador2 > carta_jugador1:
                    ganador = 2
                else:
                    ganador = 0  # Guerra

                # Resolver el turno o la guerra
                if ganador == 1:
                    self.resolver_turno(1)
                elif ganador == 2:
                    self.resolver_turno(2)
                else:
                    self._guerra = True
                    self.mostrar_guerra()
                    self.actualizar_pantalla()
                    time.sleep(JuegoGuerra.DELAY)

                self._turno += 1
                self.actualizar_mazos()
                self.actualizar_pantalla()
                time.sleep(JuegoGuerra.DELAY)

        # Si se agota el tiempo, determinar el ganador por la cantidad de cartas restantes
        if not self._ganador:
            if len(self.mazo_1) > len(self.mazo_2):
                self._ganador = 'jugador 1'
            elif len(self.mazo_2) > len(self.mazo_1):
                self._ganador = 'jugador 2'
            else:
                self._ganador = random.choice(['jugador 1', 'jugador 2'])  # Si hay empate, elige un ganador al azar

        self.mostrar_ganador_partida(self._ganador)
        return self._ganador

    def dibujar_mazos_iniciales(self):
        # Dibuja representaciones simples de los mazos iniciales
        self.jugador1_turtle.clear()
        self.jugador2_turtle.clear()
        self.jugador1_turtle.write(f"Mazo Jugador 1: {len(self.mazo_1)} cartas", align="center", font=("Arial", 12, "normal"))
        self.jugador2_turtle.write(f"Mazo Jugador 2: {len(self.mazo_2)} cartas", align="center", font=("Arial", 12, "normal"))
        self.actualizar_pantalla()

    def dibujar_cartas_en_mesa(self, carta_jugador1, carta_jugador2):
        # Limpia el área de las cartas y dibuja las cartas
        self.carta1_turtle.clear()
        self.carta2_turtle.clear()

        # Dibuja las cartas reveladas
        self.carta1_turtle.write(str(carta_jugador1), align="center", font=("Arial", 16, "normal"))
        self.carta2_turtle.write(str(carta_jugador2), align="center", font=("Arial", 16, "normal"))

        self.actualizar_pantalla()

    def resolver_turno(self, ganador):
        # Distribuye las cartas al ganador
        if ganador == 1:
            for carta in self._cartas_en_la_mesa:
                self.mazo_1.poner_carta_abajo(carta)
        else:
            for carta in self._cartas_en_la_mesa:
                self.mazo_2.poner_carta_abajo(carta)
        self._cartas_en_la_mesa = []
        self._guerra = False

    def actualizar_mazos(self):
        # Actualiza el texto de los mazos
        self.jugador1_turtle.clear()
        self.jugador2_turtle.clear()
        self.jugador1_turtle.write(f"Mazo Jugador 1: {len(self.mazo_1)} cartas", align="center", font=("Arial", 12, "normal"))
        self.jugador2_turtle.write(f"Mazo Jugador 2: {len(self.mazo_2)} cartas", align="center", font=("Arial", 12, "normal"))
        self.carta1_turtle.clear()
        self.carta2_turtle.clear()
        self.mesa_turtle.clear()

    def mostrar_ganador_partida(self, ganador):
        self.mesa_turtle.clear()
        self.mesa_turtle.write(f"¡{ganador} gana esta partida!", align="center", font=("Arial", 20, "bold"))
        self.actualizar_pantalla()

    def mostrar_ganador_final(self, ganador):
        self.mesa_turtle.clear()
        self.mesa_turtle.write(f"¡{ganador} es el ganador final!", align="center", font=("Arial", 24, "bold"))
        self.actualizar_pantalla()
        time.sleep(3)

    def mostrar_guerra(self):
        self.mesa_turtle.clear()
        self.mesa_turtle.write("¡Guerra!", align="center", font=("Arial", 20, "bold"))
        self.actualizar_pantalla()

    def actualizar_marcador(self):
        self.marcador_turtle.clear()
        self.marcador_turtle.write(f"Marcador: Jugador 1 = {self.puntaje_jugador1}, Jugador 2 = {self.puntaje_jugador2}",
                                  align="center", font=("Arial", 16, "normal"))
        self.actualizar_pantalla()

    def actualizar_pantalla(self):
        screen.update()

if __name__ == "__main__":
    juego = JuegoGuerra()  # No es necesario pasar la semilla, se genera automáticamente
    juego.iniciar_juego()
    turtle.done()  # Esto mantiene la ventana abierta hasta que se cierre manualmente
