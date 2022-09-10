# /*
#  * Enunciado: Crea un programa que calcule el daño de un attack durante
#  * una batalla Pokémon.
#  * - La fórmula será la siguiente: daño = 50 * (attack / defensa) * effectiveness
#  * - effectiveness: x2 (súper efectivo), x1 (neutral), x0.5 (no es muy efectivo)
#  * - Sólo hay 4 tipos de Pokémon: Water, Fire, Planta y Electric 
#  *   (buscar su effectiveness)
#  * - El programa recibe los siguientes parámetros:
#  *  - tipo del Pokémon atacante.
#  *  - tipo del Pokémon defensor.
#  *  - attack: Entre 1 y 100.
#  *  - Defensa: Entre 1 y 100.
#  */

class Pokemon:
    def __init__(self, type, attack, defense):
        self.type = type
        self.attack = attack
        self.defense = defense

    
    def toAttack(self, enemyPokemon):
        if self.type == "Water":
            effectiveness = WATER[enemyPokemon.type]
        elif self.type == "Earth":
            effectiveness = EARTH[enemyPokemon.type]
        elif self.type == "Fire":
            effectiveness = FIRE[enemyPokemon.type]
        elif self.type == "Electric":
            effectiveness = ELECTRIC[enemyPokemon.type]
        damage = 50 * (self.attack / enemyPokemon.defense) * effectiveness
        return damage
    
    
WATER = {"Earth": 2, "Fire": 2, "Water": 0.5, "Electric": 1}
EARTH = {"Earth": 1, "Fire": 2, "Water": 1, "Electric": 2}
FIRE = {"Earth": 1, "Fire": 0.5, "Water": 0.5, "Electric": 1}
ELECTRIC = {"Earth": 0.5, "Fire": 1, "Water": 2, "Electric": 0.5}

pikachu = Pokemon("Electric", 77, 50)
squirtle = Pokemon("Water", 60, 80)
print(pikachu.toAttack(squirtle))
