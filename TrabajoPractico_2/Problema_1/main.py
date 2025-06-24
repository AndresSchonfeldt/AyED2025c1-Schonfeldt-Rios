import time
import datetime
import random
from modules.paciente import Paciente
from modules.cola_prioridad import ColaDePrioridad

n = 20
cola = ColaDePrioridad()

for i in range(n):
    ahora = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    print('-*-'*15)
    print('\n', ahora, '\n')

    nuevos_pacientes = random.randint(1, 3)
    for _ in range(nuevos_pacientes):
        paciente = Paciente()
        cola.agregar(paciente)
        print(f"🆕 Ingresó paciente: {paciente}")

    a_atender = random.randint(1, 2)
    for _ in range(a_atender):
        if len(cola) > 0:
            atendido = cola.atender()
            print('*'*40)
            print(f"✅ Se atiende paciente: {atendido}")
            print('*'*40)

    if i == n - 1:
        print("\n⚠️ Último ciclo: Atendiendo todos los pacientes restantes...")
        while len(cola) > 0:
            atendido = cola.atender()
            print(f"✅ Se atiende paciente: {atendido}")
        print("\n🚑 Sala de emergencias vacía. No quedan pacientes.\n")

    print()
    print('Pacientes en espera:', len(cola))
    for p in cola.mostrar_pacientes():
        print('  🕓', p)

    print()
    print('-*-'*15)
    time.sleep(1)
