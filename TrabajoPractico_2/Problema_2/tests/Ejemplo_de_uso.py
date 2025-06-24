from modules.temperaturas_db import TemperaturasDB

if __name__ == "__main__":
    db = TemperaturasDB()

    print("📥 Guardando temperaturas...")
    db.guardar(25.5, "01/01/2023")
    db.guardar(28.0, "05/01/2023")
    db.guardar(22.1, "10/01/2023")
    db.guardar(26.8, "03/01/2023")
    db.guardar(24.0, "15/01/2023")
    db.guardar(30.2, "02/01/2023")
    db.guardar(20.0, "20/01/2023")
    db.guardar(27.5, "07/01/2023")

    print(f"\n🔢 Cantidad de muestras: {db.cantidad()}")

    print("\n📅 Temperatura para 05/01/2023:")
    print(db.obtener("05/01/2023"))  # Esperado: 28.0
    print("📅 Temperatura para 06/01/2023:")
    print(db.obtener("06/01/2023"))  # Esperado: None

    print("\n🌡️ Temperatura mínima entre 01/01/2023 y 10/01/2023:")
    print(db.extremos_en_rango("01/01/2023", "10/01/2023")[0])  # min

    print("\n🌡️ Temperatura máxima entre 01/01/2023 y 10/01/2023:")
    print(db.extremos_en_rango("01/01/2023", "10/01/2023")[1])  # max

    print("\n📈 Listado de temperaturas entre 01/01/2023 y 15/01/2023:")
    for linea in db.temperaturas_en_rango("01/01/2023", "15/01/2023"):
        print(linea)

    print("\n🗑️ Borrando temperatura del 05/01/2023...")
    db.borrar("05/01/2023")

    print(f"\n🔢 Muestras luego del borrado: {db.cantidad()}")
    print("Verificando borrado:")
    print(db.obtener("05/01/2023"))  # Esperado: None

    print("\n❌ Intentando borrar fecha inexistente (06/01/2023):")
    db.borrar("06/01/2023")

    print("\n🔁 Actualizando temperatura del 01/01/2023...")
    db.guardar(26.0, "01/01/2023")
    print(f"Temperatura actualizada: {db.obtener('01/01/2023')}")
    print(f"🔢 Muestras totales: {db.cantidad()}")
