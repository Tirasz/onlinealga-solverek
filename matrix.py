# nashpy, fraction

import nashpy as nash
import numpy as np
from fractions import Fraction
import sys

def input_data(path="matrix_input.txt"):
    with open(path, "r") as f:
        game_type = int(f.readline().split()[1])
        matrix = [[int(i) for i in j.split()] for j in f.readlines()]
        return game_type, matrix


def nash_eq(game):
    eq = game.support_enumeration()
    sol = [[[Fraction(k).limit_denominator(50) for k in list(i)] for i in j] for j in list(eq)][0]
    
    return sol

def print_eq(eq):
    row = True
    for k in eq:
        if row: print("Optimal for row:", end="\t")
        if not row: print("Optimal for column:", end="\t")
        row=False
        for j in k:
            print(j, end=' ')
        print()
    
def value_of_game(eq, game):
    row = game[eq[0], eq[1]][0]
    print(f"Value of the game for row player: {row}")

def nyeregpont(matrix):
    m = np.array(matrix)
    m1 = m.transpose()
    if (max([min(i) for i in matrix])) == (min([max(i) for i in m1])):
        return (max([min(i) for i in matrix]))
    else:
        return "Nincs nyeregpont"



if __name__ == "__main__":
    game_type, matrix = input_data()
    game = nash.Game(np.array(matrix))
    eq = nash_eq(game)

    if game_type == 0:
        ny = nyeregpont(matrix)
        print(f"A nyeregpont értéke: {ny}")
    elif game_type == 1:
        print_eq(eq)
    elif game_type == 2:
        value_of_game(eq, game)
    else:
        print("Invalid type number!")
        exit(0)