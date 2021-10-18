# det
# randomizalt

import os
import sys
import argparse
from sympy import *
from fractions import *

# 8 3 5 1
def all_params_tostr(B, An, n, R=1):
    An_alg = (An-1 * R) + B if n >= An else n * R
    sym_mul = min(An-1, n)
    return  An_alg, f'A_{An} algoritmus költsége {An_alg} = {sym_mul}*{R}{"+" if n>=An else ""}{B if n>=An else ""}'

    
def compute(B, An, n, R=1):
    An_alg, str_An = all_params_tostr(B, An, n, R)
    str_optdet_text = f'Az opt. det. online algoritmus A_B, azaz amelyik a B-edik napon veszi meg.'
    optdet, str_opt_det = all_params_tostr(B, B, n, R)

    print(str_An)
    print()
    print(str_optdet_text)
    print(str_opt_det)

    opt = min(B, n)
    str_komp_h_An = f'A_{An} algoritmus kompetitív hányadosa ebben az esetben C(A_{An})/opt = {An_alg}/{opt} = {Fraction(An_alg, opt)}'
    str_komp_h_Aopt = f'Opt. det. online algoritmus kompetitív hányadosa ebben az esetben C(A_{B})/opt = {optdet}/{opt} = {Fraction(optdet, opt)}'

    print()
    print(str_komp_h_An)
    print(str_komp_h_Aopt)
    
    
# A1 = B/mennyi?
# A2 = B/mennyi?
def randomized(p, A1, A2=1):
    B = symbols('B')
    N = symbols('n')
    # n<A1, ratio = 1
    print(f'Ha n < B/{A1} akkor a hányados 1, költség: n, ami < B\n')
    # A1<n<A2 ez csak felso korlat, mert B/A1 < n <= B-1, 
    eq_between = p*(1/A1*N + N) + (1-p)*(N)

    print(f'Ha B/{A1} <= n < B/{A2} akkor a költségre egy felső korlát {eq_between}')
    print(f'A kompetitív hányadosra alsó korlát lesz a: {simplify(eq_between/N)}\n') # Ha A2==1!
    # A2<n
    eq_greater = p*(B/A1 + B) + (1-p)*(B + B) # konstansok eldobva! p*(B/A1 -1 + B) + (1-p)*(B-1 + B) 
    print(f'Ha B/{A2} <= n akkor a költségre egy felső korlát {eq_greater}')
    print(f'A kompetitív hányadosra alsó korlát lesz a:{simplify(eq_greater/B)}\n') # Ha A2==1!

    print(f'Ezek közül a legrosszabb / az optimum lesz a kompetitív hányados a legnagyobb lesz, ami: [ÍRJ BE]')

    print('\n=======================================================\n')

    P = symbols('p')
    str_all = f'p={p} esetben '

    print("\nEzekből az egyenletekből p in [0,1] kell minimaxot kihozni, megtalálni p-t, ami fv-értékénél minden egyenlet alatta megy, és minimális.")
    f1 = 1
    f2 = simplify((P*(1/A1*N + N) + (1-P)*(N))/N)
    f3 = simplify((P*(B/A1 + B) + (1-P)*(B + B))/B) # konstansok eldobalva

    print(f'f1(p) =\t {f1}')
    print(f'f2(p) =\t {f2}')
    print(f'f3(p) =\t {f3}')

# minta zh / 1. feladat
compute(8, 3 ,5, 1)

print("\n=======================================================\n")

# 1. zh, tavalyi / 2. feladat
randomized(0.5, 3, 1)