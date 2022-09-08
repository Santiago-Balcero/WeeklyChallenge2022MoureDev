# /*
#  * Crea una función que evalúe si un/a atleta ha superado correctamente una
#  * carrera de obstáculos.
#  * - La función recibirá dos parámetros:
#  *      - Un array que sólo puede contener String con las palabras
#  *        "run" o "jump"
#  *      - Un String que represente la pista y sólo puede contener "_" (suelo)
#  *        o "|" (valla)
#  * - La función imprimirá cómo ha finalizado la carrera:
#  *      - Si el/a atleta hace "run" en "_" (suelo) y "jump" en "|" (valla)
#  *        será correcto y no variará el símbolo de esa parte de la pista.
#  *      - Si hace "jump" en "_" (suelo), se variará la pista por "x".
#  *      - Si hace "run" en "|" (valla), se variará la pista por "/".
#  * - La función retornará un Boolean que indique si ha superado la carrera.
#  * Para ello tiene que realizar la opción correcta en cada tramo de la pista.
#  */

def carreraSuperada(acciones: list, pista: str):
    recorrido = ""
    for i in range(len(pista)):
        if acciones[i] == "run":
            if pista[i] == "_":
                recorrido += "_"
            else:
                recorrido += "/"
        else:
            if pista[i] == "|":
                recorrido += "|"
            else:
                recorrido += "x"
    print(f"El recorrido del atleta fue: {recorrido}")
    return recorrido == pista

acciones = ["run", "jump", "run", "run", "jump"]
pista = "__|_|"
print(carreraSuperada(acciones, pista))
            
