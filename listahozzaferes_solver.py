# MTF, Move To Front
# BIT

import math

def step_move_to_front(lista, index):
    return [lista[index] if i==0 else (lista[i-1] if i<=index else lista[i]) for i in range(len(lista))]

def MTF(lista, input):
    cost = 0
    for i in input:
        index = lista.index(i)
        i_cost = index+1
        cost += i_cost
        lista = step_move_to_front(lista, index)
        print(f"input: {i}, válasz ktsg: {i_cost}, lista a move után: {lista}")
    print(f"Az algoritmus költsége {cost}. Ez 2 kompetitív, az opt >= {math.ceil(cost/2)}")

def BIT(lista, random_bitek, input):
    cost = 0
    for i in input:
        index = lista.index(i)
        i_cost = index+1
        cost += i_cost
        random_bitek[index]==1-random_bitek[index]
        if (random_bitek[index]==1):
            lista = step_move_to_front(lista, index)
        print(f"input: {i}, válasz ktsg: {i_cost}, a lista ez lett: {lista}")
    print(f"Az algoritmus költsége {cost}. Ez 1.75 kompetitív, az opt >= {math.ceil(cost/1.75)}")
    pass


# MTF([1,2,3,4,5], [4,2,3,2,1,4,2,5])
# BIT([1,2,3,4,5], [0,0,1,0,1], [4,2,3,2,1,4,3,2,5])