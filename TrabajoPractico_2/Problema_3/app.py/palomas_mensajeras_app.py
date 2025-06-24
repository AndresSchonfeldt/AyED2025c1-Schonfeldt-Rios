import turtle
from modules.graph import Graph
from modules.aldeas_data import aldeas_rutas

def plot_graph_turtle(mst, aldeas):
    """Genera la visualización del grafo usando Turtle con ajustes para mejorar la legibilidad."""
    screen = turtle.Screen()
    screen.title("Red de Comunicación - Palomas Mensajeras")
    screen.bgcolor("white")
    screen.setup(width=800, height=600)

    drawer = turtle.Turtle()
    drawer.speed(0)
    drawer.penup()

    aldeas_pos = {}
    offset_x, offset_y = -300, 250

    for i, aldea in enumerate(aldeas):
        aldeas_pos[aldea] = (offset_x + (i % 5) * 150, offset_y - (i // 5) * 50)

    drawer.pencolor("gray")
    drawer.pensize(2)

    for aldea, origen in mst.items():
        if aldea in aldeas_pos and origen in aldeas_pos:
            start_x, start_y = aldeas_pos[aldea]
            end_x, end_y = aldeas_pos[origen]
            mid_x = (start_x + end_x) / 2
            mid_y = (start_y + end_y) / 2 - 10

            drawer.goto(start_x, start_y)
            drawer.pendown()
            drawer.goto(mid_x, mid_y)
            drawer.goto(end_x, end_y)
            drawer.penup()
        else:
            print(f"Advertencia: '{aldea}' o '{origen}' no tienen una posición asignada.")

    drawer.pencolor("black")
    drawer.hideturtle()

    for aldea, pos in aldeas_pos.items():
        drawer.goto(pos)
        drawer.dot(10, "blue")
        drawer.goto(pos[0] + 10, pos[1] - 5)
        drawer.write(aldea, font=("Arial", 10, "bold"), align="left")

    turtle.done()

def main():
    """Ejecuta el análisis del problema y la visualización con Turtle."""
    graph = Graph()

    for start, end, weight in aldeas_rutas:
        graph.add_edge(start, end, weight)

    aldeas = graph.get_nodes()
    print("Lista de aldeas en orden alfabético:")
    for aldea in aldeas:
        print(aldea)

    mst, total_distance = graph.find_min_spanning_tree("Peligros")

    print("\nCamino óptimo para la transmisión de la noticia:")
    for aldea, origen in mst.items():
        print(f"La aldea '{aldea}' recibe la noticia desde '{origen}'.")

    print("\nDistancia total recorrida por las palomas:", total_distance, "leguas")

    plot_graph_turtle(mst, aldeas)

if __name__ == "__main__":
    main()
