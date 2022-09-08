# /*
#  * Crea un programa que sea capaz de transformar texto natural a código
#  * morse y viceversa.
#  * - Debe detectar automáticamente de qué tipo se trata y realizar
#  *   la conversión.
#  * - En morse se soporta raya "—", punto ".", un espacio " " entre letras
#  *   o símbolos y dos espacios entre palabras "  ".
#  * - El alfabeto morse soportado será el mostrado en
#  *   https://es.wikipedia.org/wiki/Código_morse.
#  */

def whatIs(code):
    for s in code:
        if s.isalnum() or s == "?" or s == "/" or s == "'":
            return "LETTERS"
    return "MORSE"

def processItems(code, w):
    #Returns a 2D array with [[letters] words]
    letters = []
    if w == "LETTERS":
        words = code.upper().split(" ")
        for w in words:
            letters.append([l for l in w])
    elif w == "MORSE":
        words = code.split("  ")
        for w in words:
            letters.append(w.split(" "))
    return letters

def wordsToMorse(code):
    morse = ".-,-...,-.-.,----,-..,.,..-.,--.,....,..,.---,-.-,.-..,--,-.,--.--,---,.--.,--.-.,.-.,...,-,..-,...-,.--,-..-,-.--,--..,-----,.----,..---,...--,....-,.....,-....,--...,---..,----.,.-.-.-,--..--,..--..,.-..-.,-..-.".split(",")
    letters = "A B C CH D E F G H I J K L M N Ñ O P Q R S T U V W X Y Z 0 1 2 3 4 5 6 7 8 9 . , ? ' /".split(" ")
    toMorse = dict(zip(letters, morse))
    toWords = dict(zip(morse, letters))
    result = []
    w = whatIs(code)
    info = processItems(code, w)
    #print(info) for debug
    #Iterates 2D array and translates to morse/words
    if w == "LETTERS":
        for word in info:
            w = []
            for l in word:
                w.append(toMorse[l])
            result.append(" ".join(w))
        return "  ".join(result)
    elif w == "MORSE":
        for word in info:
            w = []
            for l in word:
                w.append(toWords[l])
            result.append("".join(w))
        return " ".join(result)

print(wordsToMorse("... --- ... --..--  .- -- .. --. ---"))