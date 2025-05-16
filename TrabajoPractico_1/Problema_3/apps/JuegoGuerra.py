import turtle
import random
import time

from modules.carta import Carta
from modules.mazo import Mazo, DequeEmptyError

class JuegoGuerra:
    valores = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    palos = ['♠', '♥', '♦', '♣']
    VICTORIA = 10

    def __init__(self, random_seed=0):
        self._mazo_inicial = Mazo()
        self.mazo_1 = Mazo()
        self.mazo_2 = Mazo()
        self._guerra = False
        self._ganador = ''
        self.empate = False
        self._turno = 0
        self._cartas_en_la_mesa = []
        self._seed = random_seed
        self.jugador1_ganadas = 0
        self.jugador2_ganadas = 0
        self._setup_turtle()

    @property
    def mazo_1(self):
        return self._mazo_1

    @mazo_1.setter
    def mazo_1(self, valor):
        self._mazo_1 = valor

    @property
    def mazo_2(self):
        return self._mazo_2

    @mazo_2.setter
    def mazo_2(self, valor):
        self._mazo_2 = valor

    @property
    def empate(self):
        return self._empate

    @empate.setter
    def empate(self, valor):
        self._empate = valor

    @property
    def ganador(self):
        return self._ganador

    def _setup_turtle(self):
        self.screen = turtle.Screen()
        self.screen.setup(width=800, height=600)
        self.screen.title("Juego de Guerra")
        self.screen.bgcolor("white")
        self.screen.tracer(0)  # Control manual del refresco

        self.t_jugador1 = turtle.Turtle()
        self.t_jugador2 = turtle.Turtle()
        self.t_mesa = turtle.Turtle()
        self.t_info = turtle.Turtle()
        self._configurar_tortugas()

    def _configurar_tortugas(self):
        for t in [self.t_jugador1, self.t_jugador2, self.t_mesa, self.t_info]:
            t.hideturtle()
            t.penup()
            t.speed(0)

        self.t_jugador1.goto(-300, 0)
        self.t_jugador2.goto(300, 0)
        self.t_mesa.goto(0, 200)
        self.t_info.goto(0, -200)

    def armar_mazo_inicial(self):
        random.seed(self._seed)
        cartas = [Carta(valor, palo) for valor in JuegoGuerra.valores for palo in JuegoGuerra.palos]
        random.shuffle(cartas)
        for carta in cartas:
            self._mazo_inicial.poner_carta_arriba(carta)
        return self._mazo_inicial

    def repartir_cartas(self):
        while len(self._mazo_inicial):
            carta_1 = self._mazo_inicial.sacar_carta_arriba()
            self.mazo_1.poner_carta_arriba(carta_1)
            if len(self._mazo_inicial):
                carta_2 = self._mazo_inicial.sacar_carta_arriba()
                self.mazo_2.poner_carta_arriba(carta_2)
        return self.mazo_1, self.mazo_2

    def iniciar_juego(self, ver_partida=True):
        self.jugador1_ganadas = 0
        self.jugador2_ganadas = 0
        self.armar_mazo_inicial()
        self.repartir_cartas()
        self._cartas_en_la_mesa = []
        self._turno = 0

        while self.jugador1_ganadas < JuegoGuerra.VICTORIA and self.jugador2_ganadas < JuegoGuerra.VICTORIA:
            self._turno += 1
            try:
                if self._guerra:
                    for _ in range(3):
                        self._cartas_en_la_mesa.append(self.mazo_1.sacar_carta_arriba())
                        self._cartas_en_la_mesa.append(self.mazo_2.sacar_carta_arriba())
                        self._actualizar_display(None, None)
                        time.sleep(0.3)

                carta1 = self.mazo_1.sacar_carta_arriba(mostrar=True)
                carta2 = self.mazo_2.sacar_carta_arriba(mostrar=True)
                self._cartas_en_la_mesa.extend([carta1, carta2])

            except DequeEmptyError:
                if len(self.mazo_1):
                    self._ganador = 'jugador 1'
                else:
                    self._ganador = 'jugador 2'
                self._guerra = False
                break

            else:
                self._actualizar_display(carta1, carta2)
                time.sleep(1.0)

                if carta1 > carta2:
                    self._transferir_cartas(self.mazo_1)
                    self._guerra = False
                    self.jugador1_ganadas += 1
                elif carta2 > carta1:
                    self._transferir_cartas(self.mazo_2)
                    self._guerra = False
                    self.jugador2_ganadas += 1
                else:
                    self._guerra = True
                    self._mostrar_guerra()

            time.sleep(0.7)

        self._mostrar_resultado_final()
        turtle.done()

    def _actualizar_display(self, carta1, carta2):
        self.t_jugador1.clear()
        self.t_jugador2.clear()
        self.t_mesa.clear()
        self.t_info.clear()

        # Mostrar cartas en la mesa
        if carta1 is not None:
            self.t_mesa.goto(-100, 100)
            self.t_mesa.write(str(carta1), align="center", font=("Arial", 24, "bold"))
        if carta2 is not None:
            self.t_mesa.goto(100, 100)
            self.t_mesa.write(str(carta2), align="center", font=("Arial", 24, "bold"))

        self.t_jugador1.goto(-300, 0)
        self.t_jugador1.write(f"Jugador 1\nCartas: {len(self.mazo_1)}\nGanadas: {self.jugador1_ganadas}",
                              align="center", font=("Arial", 16, "normal"))
        self.t_jugador2.goto(300, 0)
        self.t_jugador2.write(f"Jugador 2\nCartas: {len(self.mazo_2)}\nGanadas: {self.jugador2_ganadas}",
                              align="center", font=("Arial", 16, "normal"))
        self.t_info.goto(0, -200)
        self.t_info.write(f"Turno: {self._turno}",
                          align="center", font=("Arial", 16, "normal"))
        self.screen.update()

    def _mostrar_guerra(self):
        self.t_mesa.clear()
        self.t_mesa.goto(0, 100)
        self.t_mesa.write("¡GUERRA!", align="center", font=("Arial", 32, "bold"))
        self.screen.update()
        time.sleep(0.7)

    def _transferir_cartas(self, ganador):
        for carta in self._cartas_en_la_mesa:
            ganador.poner_carta_abajo(carta)
        self._cartas_en_la_mesa = []
        self._guerra = False

    def _mostrar_resultado_final(self):
        self.t_mesa.clear()
        ganador = ""
        if self.jugador1_ganadas >= JuegoGuerra.VICTORIA:
            ganador = "Jugador 1"
        elif self.jugador2_ganadas >= JuegoGuerra.VICTORIA:
            ganador = "Jugador 2"
        resultado_text = (
            f"¡{ganador} gana!\n"
            f"Jugador 1 Ganadas: {self.jugador1_ganadas}\n"
            f"Jugador 2 Ganadas: {self.jugador2_ganadas}\n"
            f"Turnos Jugados: {self._turno}"
        )
        self.t_mesa.goto(0, 0)
        self.t_mesa.write(resultado_text, align="center", font=("Arial", 20, "bold"))
        self.screen.update()
        time.sleep(5)

if __name__ == "__main__":
    random_seed = random.randint(0, 1000)
    juego = JuegoGuerra(random_seed)
    juego.iniciar_juego()
