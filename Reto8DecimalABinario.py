# /*
#  * Crea un programa se encargue de transformar un número
#  * decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
#  */

def intToBin(n):
    res = ""
    while n > 0:
        bi = n % 2
        n //= 2
        res = str(bi) + res
    return res

print(intToBin(17))
print(intToBin(4))
print(intToBin(17432))
print(intToBin(1989))
print(intToBin(2022))