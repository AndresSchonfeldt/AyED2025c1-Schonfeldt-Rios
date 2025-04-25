# 📝Documentación del proyecto
El código presentado simula el juego de cartas "Guerra", donde dos jugadores se enfrentan utilizando una baraja estándar. El objetivo es que un jugador gane todas las cartas. El juego se divide en varias etapas clave:
Inicialización: Se crean dos jugadores, cada uno con un mazo de 26 cartas. Los jugadores no pueden ver sus cartas.
Desarrollo del juego: En cada turno, los jugadores revelan la carta superior de su mazo. El jugador con la carta de mayor valor gana el turno y añade ambas cartas al final de su mazo.
Guerra: Si ambos jugadores revelan cartas del mismo valor, se declara una "guerra". En este caso, cada jugador pone tres cartas boca abajo y luego revela otra carta. El ganador de la guerra se lleva todas las cartas en juego. Este proceso se repite si hay empate de nuevo.
Finalización: El juego continúa hasta que un jugador gana todas las cartas, o si se alcanza un número máximo de turnos, resultando en un empate.
El código usa la librería turtle para proporcionar una representación visual del juego, mostrando las cartas, los mazos de los jugadores y otra información relevante. La librería random se utiliza para mezclar las cartas al principio del juego y para simular el azar inherente al juego. El objetivo principal del código es simular el juego de "Guerra" y proporcionar una interfaz visual interactiva.
