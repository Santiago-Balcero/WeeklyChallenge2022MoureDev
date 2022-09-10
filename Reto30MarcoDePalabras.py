# /*
#  * Crea una función que reciba un texto y muestre cada palabra en una línea,
#  * formando un marco rectangular de asteriscos.
#  * - ¿Qué te parece el reto? Se vería así:
#  *   **********
#  *   * ¿Qué   *
#  *   * te     *
#  *   * parece *
#  *   * el     *
#  *   * reto?  *
#  *   **********
#  */

def marcoPalabras(cadena):
    palabras = cadena.split(" ")
    largo = max([len(x) for x in palabras])
    print((largo + 4) * "*")
    for p in palabras:
        print(f"* {p}{(largo - len(p)) * ' '} *")
    print((largo + 4) * "*")
    
marcoPalabras("¿Qué te parece el reto?")