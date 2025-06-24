import datetime
from modules.arbol_avl import ArbolAVL

class TemperaturasDB:
    def __init__(self):
        self._arbol = ArbolAVL()

    def guardar(self, temp, fecha_str):
        fecha = datetime.datetime.strptime(fecha_str, "%d/%m/%Y").date()
        self._arbol.insertar(fecha, temp)

    def obtener(self, fecha_str):
        fecha = datetime.datetime.strptime(fecha_str, "%d/%m/%Y").date()
        return self._arbol.buscar(fecha)

    def borrar(self, fecha_str):
        fecha = datetime.datetime.strptime(fecha_str, "%d/%m/%Y").date()
        exito = self._arbol.eliminar(fecha)
        if not exito:
            print(f"No se encontró temperatura para {fecha_str}.")
        else:
            print(f"Temperatura de {fecha_str} eliminada correctamente.")

    def cantidad(self):
        return self._arbol.cantidad()

    def temperaturas_en_rango(self, f1_str, f2_str):
        f1 = datetime.datetime.strptime(f1_str, "%d/%m/%Y").date()
        f2 = datetime.datetime.strptime(f2_str, "%d/%m/%Y").date()
        if f1 > f2:
            f1, f2 = f2, f1
        datos = self._arbol.recorrido_rango(f1, f2)
        return [f"{f.strftime('%d/%m/%Y')}: {t}°C" for f, t in datos]

    def extremos_en_rango(self, f1_str, f2_str):
        f1 = datetime.datetime.strptime(f1_str, "%d/%m/%Y").date()
        f2 = datetime.datetime.strptime(f2_str, "%d/%m/%Y").date()
        if f1 > f2:
            f1, f2 = f2, f1
        datos = self._arbol.recorrido_rango(f1, f2)
        if not datos:
            return (None, None)
        temp_min = min(t for _, t in datos)
        temp_max = max(t for _, t in datos)
        return (temp_min, temp_max)
