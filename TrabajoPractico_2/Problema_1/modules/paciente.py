import datetime
from random import randint, choices

nombres = ['Leandro', 'Mariela', 'Gastón', 'Andrea', 'Antonio', 'Estela', 'Jorge', 'Agustina']
apellidos = ['Perez', 'Colman', 'Rodriguez', 'Juarez', 'García', 'Belgrano', 'Mendez', 'Lopez']
niveles_de_riesgo = [1, 2, 3]
descripciones_de_riesgo = ['crítico', 'moderado', 'bajo']
probabilidades = [0.1, 0.3, 0.6]

class Paciente:
    _contador = 0

    def __init__(self):
        self._nombre = nombres[randint(0, len(nombres)-1)]
        self._apellido = apellidos[randint(0, len(apellidos)-1)]
        self._riesgo = choices(niveles_de_riesgo, probabilidades)[0]
        self._descripcion = descripciones_de_riesgo[self._riesgo-1]
        self._hora_ingreso = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        self._orden_llegada = Paciente._contador
        Paciente._contador += 1

    def get_riesgo(self): return self._riesgo
    def get_orden(self): return self._orden_llegada
    def get_hora(self): return self._hora_ingreso

    def __lt__(self, otro):
        if self._riesgo == otro._riesgo:
            return self._orden_llegada < otro._orden_llegada
        return self._riesgo < otro._riesgo

    def __str__(self):
        return f"{self._nombre} {self._apellido} -> {self._riesgo}-{self._descripcion} (ingresó {self._hora_ingreso})"
