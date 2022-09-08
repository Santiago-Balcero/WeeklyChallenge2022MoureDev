# /*
#  * Crea un programa que calcule quien gana más partidas al piedra,
#  * papel, tijera.
#  * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
#  * - La función recibe un listado que contiene pares, representando cada jugada.
#  * - El par puede contener combinaciones de "R" (piedra), "P" (papel)
#  *   o "S" (tijera).
#  * - Ejemplo. Entrada: [("R","S"), ("S","R"), ("P","S")]. Resultado: "Player 2".
#  */

def ganadorJugada(jugada: tuple):
    #Determina el ganador por cada jugada
    if jugada[0] == jugada[1]:
        return "Tie"
    if (jugada[0] == "R" and jugada[1] == "S") or (jugada[0] == "P" and jugada[1] == "R") or (jugada[0] == "S" and jugada[1] == "P"):
        return "Player 1"
    else:
        return "Player 2"

def ganadorPiedraPapelTijera(jugadas: list):
    resultados = {"Player 1": 0, "Player 2": 0, "Tie": 0}
    for j in jugadas:
        resultados[ganadorJugada(j)] += 1
    #Recorre los resultados para determinar el ganador
    max = 0
    winner = ""
    for p in resultados:
        if resultados[p] > max:
            max = resultados[p]
            winner = p
    return winner
    
print(ganadorPiedraPapelTijera([("R","S"), ("S","R"), ("P","S")]))