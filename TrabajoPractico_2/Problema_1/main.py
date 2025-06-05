# -*- coding: utf-8 -*-
"""
Sala de emergencias - Simulación con cola de prioridad
"""

import time
import datetime
import random
from modules.paciente import Paciente
from modules.cola_prioridad import ColaPrioridad

n = 20  # cantidad de ciclos de simulación

cola_de_espera = ColaPrioridad()

# Ciclo que gestiona la simulación
for i in range(n):
    ahora = datetime.datetime.now()
    fecha_y_hora = ahora.strftime('%d/%m/%Y %H:%M:%S')
    print('-*-'*15)
    print('\n', fecha_y_hora, '\n')

    # 🚑 Generar entre 1 y 3 nuevos pacientes por ciclo
    cantidad_nuevos = random.randint(1, 3)
    for _ in range(cantidad_nuevos):
        paciente = Paciente()
        cola_de_espera.agregar(paciente)
        print(f"🆕 Paciente ingresó: {paciente}")

    # 🏥 Atender entre 1 y 2 pacientes si hay en la cola
    cantidad_atender = random.randint(1, 2)
    for _ in range(cantidad_atender):
        if len(cola_de_espera) > 0:
            paciente_atendido = cola_de_espera.atender()
            print('*'*40)
            print(f'✅ Se atiende paciente con riesgo {paciente_atendido.riesgo}, ingresado a las {paciente_atendido.fecha_ingreso}')
            print('*'*40)

    # 📢 Último ciclo: asegurarse de vaciar la cola antes de terminar
    if i == n - 1:
        print("\n⚠️ Último ciclo: Atendiendo a todos los pacientes restantes...")
        while len(cola_de_espera) > 0:
            paciente_atendido = cola_de_espera.atender()
            print(f'✅ Se atiende paciente con riesgo {paciente_atendido.riesgo}, ingresado a las {paciente_atendido.fecha_ingreso}')
        
        print("\n🚑 Sala de emergencias vacía. No quedan pacientes por atender.")

    print()
    print('-*-'*15)
    
    time.sleep(1)