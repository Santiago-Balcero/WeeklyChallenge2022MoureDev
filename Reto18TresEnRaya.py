# /*
#  * Crea una función que analice una matriz 3x3 compuesta por "X" y "O"
#  * y retorne lo siguiente:
#  * - "X" si han ganado las "X"
#  * - "O" si han ganado los "O"
#  * - "Empate" si ha habido un empate
#  * - "Nulo" si la proporción de "X", de "O", o de la matriz no es correcta.
#  *   O si han ganado los 2.
#  * Nota: La matriz puede no estar totalmente cubierta.
#  * Se podría representar con un vacío "", por ejemplo.
#  */

def ganadorTresEnRaya(tablero):
    ganador = ganadorFilas(tablero)
    if ganador == "Nulo":
        return ganador
    ganador += ganadorColumnas(tablero)
    ganador += ganadorDiagonales(tablero)
    if len(set(ganador)) == 2:
        return "Nulo"
    elif len(ganador) == 0:
        return "Empate"
    elif len(set(ganador)) == 1:
        return ganador[0]
    return ganador

def ganadorFilas(tablero):
    ganador = []
    X = 0
    O = 0
    for i in range(3):
        if len(tablero[i]) != 3:
            return "Nulo"
        for j in range(3):
            if tablero[i][j] == "X":
                X += 1
            elif tablero[i][j] == "O":
                O += 1
        if tablero[i][0] == tablero[i][1] == tablero[i][2] and tablero[i][0] != "":
            ganador.append(tablero[i][0])
    if abs(X - O) > 1:
        return "Nulo"
    return ganador

def ganadorColumnas(tablero):
    ganador = []
    for i in range(3):
        if tablero[0][i] == tablero[1][i] == tablero[2][i] and tablero[0][i] != "":
            ganador.append(tablero[0][i])
    return ganador

def ganadorDiagonales(tablero):
    ganador = []
    for i in range(2):
        if (tablero[0][0] == tablero[1][1] == tablero[2][2] or tablero[0][2] == tablero[1][1] == tablero[2][0]) and tablero[1][1] != "":
            ganador.append(tablero[1][1])
    return ganador

tablero = [["O", "X", "X"], 
           ["O", "X", "O"], 
           ["X", "", "O"]]
print(ganadorTresEnRaya(tablero))