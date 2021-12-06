# DC -- Double Coverage

import math
from collections.abc import Callable

class config:
    def __init__(self, config: list[int], distance: Callable[[int, int], int]) -> None:
        self.config = config
        self.actual_move_cost = 0
        self.total_cost = 0
        self.servers = len(config)
        self.d = distance
        self.input=-1


    def get_closest_2(self, input: int) -> tuple[int, int, int]:
        closest = 0
        second_closest = 0
        closest_dist = 0
        for i in range(self.servers):
            if (self.d(self.config[i], input) <= self.d(self.config[closest], input)):
                second_closest = closest
                closest = i
                closest_dist = self.d(self.config[i], input)
            elif (self.d(self.config[i], input) <= self.d(self.config[second_closest], input)):
                second_closest = i
        #print(closest, second_closest, closest_dist)
        return (closest, second_closest, closest_dist)

    def DC_move(self, input: int) -> None:
        self.input=input
        closest, second_closest, closest_dist = self.get_closest_2(input)
        self.config[closest] = input
        if self.config[second_closest] - input <= 0:
            self.config[second_closest] += closest_dist
        else: 
            self.config[second_closest] -= closest_dist
        self.total_cost += 2*closest_dist

    def DC_lazy_move(self, input: int) -> None:
        self.input=input
        closest, _, dist = self.get_closest_2(input)
        self.config[closest] = input
        self.actual_move_cost = dist
        self.total_cost += dist

    def __str__(self) -> str:
        return f"Az input: {self.input}. A config most: {self.config}, az összköltség: {self.total_cost}."
    

def distance(x: int, y: int)->int:
    return abs(x-y)

def DC(init_config: list[int], input: list[int], distance: Callable[[int, int], int]) -> None:
    c = config(init_config, distance)
    for i in input:
        c.DC_move(i)
        print(c)

def DC_lazy(init_config: list[int], input: list[int], distance: Callable[[int, int], int]) -> None:
    c = config(init_config, distance)
    for i in input:
        c.DC_lazy_move(i)
        print(c)

DC([0,3,5], [2,3,0,2,0,2,5], distance)
#DC_lazy([0,3,5], [2,3,0,2,0,2,5], distance)