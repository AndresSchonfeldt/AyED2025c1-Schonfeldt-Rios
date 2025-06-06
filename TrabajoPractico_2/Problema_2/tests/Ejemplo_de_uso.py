from TrabajoPractico_2.Problema_2.modules.ArbolAVL import Temperaturas_DB


if __name__ == "__main__":
    db = Temperaturas_DB()

    print("Guardando temperaturas...")
    db.guardar_temperatura(25.5, "01/01/2023")
    db.guardar_temperatura(28.0, "05/01/2023")
    db.guardar_temperatura(22.1, "10/01/2023")
    db.guardar_temperatura(26.8, "03/01/2023")
    db.guardar_temperatura(24.0, "15/01/2023")
    db.guardar_temperatura(30.2, "02/01/2023")
    db.guardar_temperatura(20.0, "20/01/2023")
    db.guardar_temperatura(27.5, "07/01/2023")


    print(f"\nCantidad de muestras: {db.cantidad_muestras()}")

    print("\nDevolviendo temperatura para 05/01/2023:")
    print(db.devolver_temperatura("05/01/2023")) # Esperado: 28.0
    print("Devolviendo temperatura para 06/01/2023:")
    print(db.devolver_temperatura("06/01/2023")) # Esperado: None

    print("\nTemperatura mínima en el rango 01/01/2023 a 10/01/2023:")
    print(db.min_temp_rango("01/01/2023", "10/01/2023")) # Esperado: 22.1

    print("\nTemperatura máxima en el rango 01/01/2023 a 10/01/2023:")
    print(db.max_temp_rango("01/01/2023", "10/01/2023")) # Esperado: 30.2

    print("\nTemperaturas extremas en el rango 01/01/2023 a 10/01/2023:")
    print(db.temp_extremos_rango("01/01/2023", "10/01/2023")) # Esperado: (22.1, 30.2)

    print("\nListado de temperaturas en el rango 01/01/2023 a 15/01/2023:")
    for item in db.devolver_temperaturas("01/01/2023", "15/01/2023"):
        print(item)
    # Salida esperada (fechas ordenadas):
    # 01/01/2023: 25.5°C
    # 02/01/2023: 30.2°C
    # 03/01/2023: 26.8°C
    # 05/01/2023: 28.0°C
    # 07/01/2023: 27.5°C
    # 10/01/2023: 22.1°C
    # 15/01/2023: 24.0°C

    print("\nBorrando temperatura para 05/01/2023...")
    db.borrar_temperatura("05/01/2023")
    print(f"Cantidad de muestras después de borrar: {db.cantidad_muestras()}")
    print("Verificando si 05/01/2023 existe:")
    print(db.devolver_temperatura("05/01/2023")) # Esperado: None

    print("\nIntentando borrar una fecha que no existe (06/01/2023):")
    db.borrar_temperatura("06/01/2023")

    print("\nActualizando temperatura para 01/01/2023...")
    db.guardar_temperatura(26.0, "01/01/2023")
    print(f"Temperatura para 01/01/2023: {db.devolver_temperatura('01/01/2023')}")
    print(f"Cantidad de muestras (no debería cambiar): {db.cantidad_muestras()}")