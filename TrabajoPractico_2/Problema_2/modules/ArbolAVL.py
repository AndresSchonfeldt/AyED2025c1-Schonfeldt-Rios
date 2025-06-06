import datetime

class NodoAVL:
    """
    Representa un nodo en el árbol AVL.
    Almacena la fecha, temperatura, y punteros a los hijos izquierdo/derecho, y altura.
    """
    def __init__(self, fecha, temperatura):
        if not isinstance(fecha, datetime.date):
            raise TypeError("La fecha debe ser un objeto datetime.date.")
        self.fecha = fecha
        self.temperatura = temperatura
        self.izquierda = None
        self.derecha = None
        self.altura = 1  # Un nuevo nodo inicialmente tiene altura 1

class Temperaturas_DB:
    """
    Gestiona las mediciones de temperatura utilizando un árbol AVL para un almacenamiento
    y recuperación eficientes.
    """
    def __init__(self):
        self.raiz = None
        self._cantidad_muestras = 0

    def _obtener_altura(self, nodo):
        """Función auxiliar para obtener la altura de un nodo."""
        return nodo.altura if nodo else 0

    def _actualizar_altura(self, nodo):
        """Función auxiliar para actualizar la altura de un nodo."""
        if nodo:
            nodo.altura = 1 + max(self._obtener_altura(nodo.izquierda), self._obtener_altura(nodo.derecha))

    def _obtener_balance(self, nodo):
        """Función auxiliar para obtener el factor de equilibrio de un nodo."""
        return self._obtener_altura(nodo.izquierda) - self._obtener_altura(nodo.derecha) if nodo else 0

    def _rotar_derecha(self, y):
        """Realiza una rotación a la derecha."""
        x = y.izquierda
        T2 = x.derecha

        # Realizar rotación
        x.derecha = y
        y.izquierda = T2

        # Actualizar alturas
        self._actualizar_altura(y)
        self._actualizar_altura(x)

        return x

    def _rotar_izquierda(self, x):
        """Realiza una rotación a la izquierda."""
        y = x.derecha
        T2 = y.izquierda

        # Realizar rotación
        y.izquierda = x
        x.derecha = T2

        # Actualizar alturas
        self._actualizar_altura(x)
        self._actualizar_altura(y)

        return y

    def _insertar(self, nodo, fecha, temperatura):
        """Función auxiliar recursiva para insertar un nuevo nodo."""
        if not nodo:
            self._cantidad_muestras += 1
            return NodoAVL(fecha, temperatura)

        if fecha < nodo.fecha:
            nodo.izquierda = self._insertar(nodo.izquierda, fecha, temperatura)
        elif fecha > nodo.fecha:
            nodo.derecha = self._insertar(nodo.derecha, fecha, temperatura)
        else:  # La fecha ya existe, actualizar la temperatura
            nodo.temperatura = temperatura
            return nodo

        self._actualizar_altura(nodo)
        balance = self._obtener_balance(nodo)

        # Caso Izquierda-Izquierda
        if balance > 1 and fecha < nodo.izquierda.fecha:
            return self._rotar_derecha(nodo)

        # Caso Derecha-Derecha
        if balance < -1 and fecha > nodo.derecha.fecha:
            return self._rotar_izquierda(nodo)

        # Caso Izquierda-Derecha
        if balance > 1 and fecha > nodo.izquierda.fecha:
            nodo.izquierda = self._rotar_izquierda(nodo.izquierda)
            return self._rotar_derecha(nodo)

        # Caso Derecha-Izquierda
        if balance < -1 and fecha < nodo.derecha.fecha:
            nodo.derecha = self._rotar_derecha(nodo.derecha)
            return self._rotar_izquierda(nodo)

        return nodo

    def _nodo_valor_minimo(self, nodo):
        """Función auxiliar para encontrar el nodo con el valor mínimo en un subárbol."""
        actual = nodo
        while actual.izquierda is not None:
            actual = actual.izquierda
        return actual

    def _eliminar(self, nodo, fecha):
        """Función auxiliar recursiva para eliminar un nodo."""
        if not nodo:
            return nodo

        if fecha < nodo.fecha:
            nodo.izquierda = self._eliminar(nodo.izquierda, fecha)
        elif fecha > nodo.fecha:
            nodo.derecha = self._eliminar(nodo.derecha, fecha)
        else:  # Nodo con esta fecha encontrado
            if nodo.izquierda is None or nodo.derecha is None:
                temp = nodo.izquierda if nodo.izquierda else nodo.derecha
                nodo = None  # Efectivamente elimina el nodo
                if temp:
                    nodo = temp  # Si había un hijo, lo reemplaza con él
                self._cantidad_muestras -= 1
            else:
                # Nodo con dos hijos: obtener el sucesor en orden
                temp = self._nodo_valor_minimo(nodo.derecha)
                nodo.fecha = temp.fecha
                nodo.temperatura = temp.temperatura
                nodo.derecha = self._eliminar(nodo.derecha, temp.fecha)

        if not nodo:
            return nodo

        self._actualizar_altura(nodo)
        balance = self._obtener_balance(nodo)

        # Rebalancear el árbol
        # Caso Izquierda-Izquierda
        if balance > 1 and self._obtener_balance(nodo.izquierda) >= 0:
            return self._rotar_derecha(nodo)

        # Caso Izquierda-Derecha
        if balance > 1 and self._obtener_balance(nodo.izquierda) < 0:
            nodo.izquierda = self._rotar_izquierda(nodo.izquierda)
            return self._rotar_derecha(nodo)

        # Caso Derecha-Derecha
        if balance < -1 and self._obtener_balance(nodo.derecha) <= 0:
            return self._rotar_izquierda(nodo)

        # Caso Derecha-Izquierda
        if balance < -1 and self._obtener_balance(nodo.derecha) > 0:
            nodo.derecha = self._rotar_derecha(nodo.derecha)
            return self._rotar_izquierda(nodo)

        return nodo

    def _recorrido_en_orden(self, nodo, fecha_inicio, fecha_fin, lista_resultado):
        """Función auxiliar para el recorrido en orden para recolectar nodos dentro de un rango."""
        if not nodo:
            return

        # Recorrer subárbol izquierdo
        if fecha_inicio < nodo.fecha:
            self._recorrido_en_orden(nodo.izquierda, fecha_inicio, fecha_fin, lista_resultado)

        # Visitar el nodo actual si está dentro del rango
        if fecha_inicio <= nodo.fecha <= fecha_fin:
            lista_resultado.append((nodo.fecha, nodo.temperatura))

        # Recorrer subárbol derecho
        if fecha_fin > nodo.fecha:
            self._recorrido_en_orden(nodo.derecha, fecha_inicio, fecha_fin, lista_resultado)

    def guardar_temperatura(self, temperatura, fecha_str):
        """
        Guarda la medida de temperatura asociada a la fecha.
        La fecha espera el formato "dd/mm/aaaa" (string).
        """
        try:
            fecha = datetime.datetime.strptime(fecha_str, "%d/%m/%Y").date()
        except ValueError:
            raise ValueError("Formato de fecha inválido. Use 'dd/mm/aaaa'.")
        self.raiz = self._insertar(self.raiz, fecha, temperatura)

    def devolver_temperatura(self, fecha_str):
        """
        Devuelve la medida de temperatura en la fecha determinada.
        La fecha espera el formato "dd/mm/aaaa" (string).
        Retorna None si no se encuentra.
        """
        try:
            fecha = datetime.datetime.strptime(fecha_str, "%d/%m/%Y").date()
        except ValueError:
            raise ValueError("Formato de fecha inválido. Use 'dd/mm/aaaa'.")

        actual = self.raiz
        while actual:
            if fecha < actual.fecha:
                actual = actual.izquierda
            elif fecha > actual.fecha:
                actual = actual.derecha
            else:
                return actual.temperatura
        return None

    def min_temp_rango(self, fecha1_str, fecha2_str):
        """
        Devuelve la temperatura mínima entre los rangos fecha1 y fecha2 inclusive.
        Las fechas esperan el formato "dd/mm/aaaa" (string).
        """
        try:
            fecha1 = datetime.datetime.strptime(fecha1_str, "%d/%m/%Y").date()
            fecha2 = datetime.datetime.strptime(fecha2_str, "%d/%m/%Y").date()
        except ValueError:
            raise ValueError("Formato de fecha inválido. Use 'dd/mm/aaaa'.")

        if fecha1 > fecha2:
            fecha1, fecha2 = fecha2, fecha1  # Asegurar que fecha1 sea siempre menor o igual

        temperaturas_en_rango = []
        self._recorrido_en_orden(self.raiz, fecha1, fecha2, temperaturas_en_rango)

        if not temperaturas_en_rango:
            return None  # No hay temperaturas en el rango dado
        return min(temp for _, temp in temperaturas_en_rango)

    def max_temp_rango(self, fecha1_str, fecha2_str):
        """
        Devuelve la temperatura máxima entre los rangos fecha1 y fecha2 inclusive.
        Las fechas esperan el formato "dd/mm/aaaa" (string).
        """
        try:
            fecha1 = datetime.datetime.strptime(fecha1_str, "%d/%m/%Y").date()
            fecha2 = datetime.datetime.strptime(fecha2_str, "%d/%m/%Y").date()
        except ValueError:
            raise ValueError("Formato de fecha inválido. Use 'dd/mm/aaaa'.")

        if fecha1 > fecha2:
            fecha1, fecha2 = fecha2, fecha1  # Asegurar que fecha1 sea siempre menor o igual

        temperaturas_en_rango = []
        self._recorrido_en_orden(self.raiz, fecha1, fecha2, temperaturas_en_rango)

        if not temperaturas_en_rango:
            return None  # No hay temperaturas en el rango dado
        return max(temp for _, temp in temperaturas_en_rango)

    def temp_extremos_rango(self, fecha1_str, fecha2_str):
        """
        Devuelve la temperatura mínima y máxima entre los rangos fecha1 y fecha2 inclusive.
        Las fechas esperan el formato "dd/mm/aaaa" (string).
        Retorna una tupla (min_temp, max_temp) o (None, None) si no hay datos.
        """
        try:
            fecha1 = datetime.datetime.strptime(fecha1_str, "%d/%m/%Y").date()
            fecha2 = datetime.datetime.strptime(fecha2_str, "%d/%m/%Y").date()
        except ValueError:
            raise ValueError("Formato de fecha inválido. Use 'dd/mm/aaaa'.")

        if fecha1 > fecha2:
            fecha1, fecha2 = fecha2, fecha1  # Asegurar que fecha1 sea siempre menor o igual

        temperaturas_en_rango = []
        self._recorrido_en_orden(self.raiz, fecha1, fecha2, temperaturas_en_rango)

        if not temperaturas_en_rango:
            return (None, None)

        min_temp = min(temp for _, temp in temperaturas_en_rango)
        max_temp = max(temp for _, temp in temperaturas_en_rango)
        return (min_temp, max_temp)

    def borrar_temperatura(self, fecha_str):
        """
        Recibe una fecha y elimina del árbol la medición correspondiente a esa fecha.
        La fecha espera el formato "dd/mm/aaaa" (string).
        """
        try:
            fecha = datetime.datetime.strptime(fecha_str, "%d/%m/%Y").date()
        except ValueError:
            raise ValueError("Formato de fecha inválido. Use 'dd/mm/aaaa'.")

        conteo_inicial = self._cantidad_muestras
        self.raiz = self._eliminar(self.raiz, fecha)
        if self._cantidad_muestras == conteo_inicial:
            print(f"Advertencia: No se encontró temperatura para la fecha {fecha_str}.")
        else:
            print(f"Temperatura para la fecha {fecha_str} eliminada exitosamente.")

    def devolver_temperaturas(self, fecha1_str, fecha2_str):
        """
        Devuelve un listado de las mediciones de temperatura en el rango recibido por parámetro
        con el formato "dd/mm/aaaa: temperatura °C", ordenado por fechas.
        Las fechas esperan el formato "dd/mm/aaaa" (string).
        """
        try:
            fecha1 = datetime.datetime.strptime(fecha1_str, "%d/%m/%Y").date()
            fecha2 = datetime.datetime.strptime(fecha2_str, "%d/%m/%Y").date()
        except ValueError:
            raise ValueError("Formato de fecha inválido. Use 'dd/mm/aaaa'.")

        if fecha1 > fecha2:
            fecha1, fecha2 = fecha2, fecha1

        temperaturas_en_rango = []
        self._recorrido_en_orden(self.raiz, fecha1, fecha2, temperaturas_en_rango)

        # Ordenar por fecha (el recorrido en orden ya lo hace, pero es bueno ser explícito)
        temperaturas_en_rango.sort(key=lambda x: x[0])

        lista_formateada = [
            f"{fecha.strftime('%d/%m/%Y')}: {temp}°C" for fecha, temp in temperaturas_en_rango
        ]
        return lista_formateada

    def cantidad_muestras(self):
        """
        Devuelve la cantidad de muestras de la BD.
        """
        return self._cantidad_muestras