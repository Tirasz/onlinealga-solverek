# solver fuggetlen es osszefuggo gepekre vonatkozo 
# utemezesi feladatok megoldasara a lista algoritmussal

import math

class Gep:

    def __init__(self) -> None:
        self.munkak = []
        self.toltes = 0
        self.sebesseg = 1
    
    def utemez(self, munka, toltes):
        self.munkak.append(munka)
        self.toltes += toltes/self.sebesseg

    def getToltes(self):
        return self.toltes




def lista_fuggetlen(m, input):
    gepek = [Gep() for _ in range(m)]
    
    for j in input:
        # minden gepre nezzuk meg hogy mennyi lenne a load ha oda raknak a jobot
        # ebbol kell a legkisebb
        minimum = 100000000
        mingep = Gep()
        for g in gepek:
            if g.getToltes() + j[gepek.index(g)] < minimum:
                mingep = g
                
                minimum = g.getToltes() + j[gepek.index(g)]
        # rakjuk ide a jobot
        mingep.utemez(j, j[gepek.index(mingep)])
        print(mingep.munkak)
        print(minimum)
    
    for g in gepek:
        print(f"{gepek.index(g)}. gep: {g.munkak}, toltes: {g.getToltes()}")

def getMingep(gepek, j):
    mintoltes = gepek[0].getToltes()
    for g in gepek:
        if g.getToltes() < mintoltes:
            return g
    
    #return gepek[0]

def lista_osszefuggo(m, input, sebessegek = []):
    #rakjuk a legkisebb toltesu gepre az aktualis munkat
    # init gepek
    gepek = [Gep() for _ in range(m)]
    if len(sebessegek) != 0:
        for v in sebessegek:
            gepek[sebessegek.index(v)].sebesseg = v
    # az elso job fixen a leggyorsabb gepre kerul
    
    minimum = 100000
    for j in input:
        mingep = Gep()
        minimum = 100000
        for g in gepek:
            if g.getToltes() + j/g.sebesseg < minimum:
                mingep = g
                minimum = mingep.getToltes() + j/mingep.sebesseg
                print(f"mingep: {g.toltes}, minimum: {minimum}")
        mingep.utemez(j, j)
    
    for g in gepek:
        print(f"{gepek.index(g)}. gep munkai: {g.munkak},\ttoltese: {g.getToltes()}")

# eskunemlopott
# calculate every possible partition of a list recursively
def partition(collection):
    if len(collection) == 1:
        yield [ collection ]
        return

    first = collection[0]
    for smaller in partition(collection[1:]):
        # insert `first` in each of the subpartition's subsets
        for n, subset in enumerate(smaller):
            yield smaller[:n] + [[ first ] + subset]  + smaller[n+1:]
        # put `first` in its own subset 
        yield [ [ first ] ] + smaller

def makespan(input):
    # max of sum of jobs on machines
    M = 0
    
    for m in input:
        sum = 0
        for j in m:
            sum += j[0]
        if(sum > M):
            M = sum
    return M

def opt(input, m):
    if(len(input) <= m):
        return [[x] for x in input]
    M = math.inf
    C = [x for x in partition(input) if len(x) == m]
    optSched = []
    for scheduling in C:
        mkspn = makespan(scheduling)
        if(mkspn < M):
            optSched = scheduling
            M = mkspn

    return optSched

def INTV_OPT(input, m):
    ret = dict()
    collect = [job for job in input if job[1] == 0]
    ret[0] = opt(collect, m)
    start = 0
    nextEmptyAt = makespan(ret[0])
    input = input[len(collect):]
    collect = []
    
    for job in input:
        if(job[1] > start and job[1] <= nextEmptyAt):
            collect.append(job)
        else:
            ret[nextEmptyAt] = opt(collect, m)
            start = nextEmptyAt
            nextEmptyAt += makespan(ret[nextEmptyAt])
            collect = [job]

    if(len(collect) != 0):
        ret[nextEmptyAt] = opt(collect, m)

    return ret



def lpt(input, m):
    inputDecreasing = sorted(input, key=lambda x: x[0], reverse=True)
    gepek = [Gep() for _ in range(m)]
    
    for j in inputDecreasing:
        # minden gepre nezzuk meg hogy mennyi lenne a load ha oda raknak a jobot
        # ebbol kell a legkisebb
        minimum = 100000000
        mingep = Gep()
        for g in gepek:
            if g.getToltes() + j[0] < minimum:
                mingep = g
                
                minimum = g.getToltes() + j[0]
        # rakjuk ide a jobot
        mingep.utemez(j, j[0])
    
    return [gep.munkak for gep in gepek]

    
def INTV_LPT(input, m):
    ret = dict()
    collect = [job for job in input if job[1] == 0]
    ret[0] = lpt(collect, m)
    start = 0
    nextEmptyAt = makespan(ret[0])
    input = input[len(collect):]
    collect = []
    
    for job in input:
        if(job[1] > start and job[1] <= nextEmptyAt):
            collect.append(job)
        else:
            ret[nextEmptyAt] = lpt(collect, m)
            start = nextEmptyAt
            nextEmptyAt += makespan(ret[nextEmptyAt])
            collect = [job]

    if(len(collect) != 0):
        ret[nextEmptyAt] = lpt(collect, m)

    return ret


#lista_fuggetlen(2, input=[(1,4), (2, 4), (2, 4), (3, 1), (2, 1) ])
#lista_osszefuggo(3, [6, 6, 6, 12, 24, 18, 12], [1,2,3])
# lista_osszefuggo(3, [6, 6, 6, 12, 24, 18, 12], [1,2,3])

input = [(1, 0), (1, 0), (2, 0), (3, 0), (2, 1), (2, 2), (3, 2), (1, 3), (2, 4), (1, 5)]

result = INTV_LPT(input, 3)

fullMakespan = 0
for t in result.keys():
    print(f"{t}. időpillanat:")
    for idx, m in enumerate(result[t]):
        print(f"{idx+1}. gép: {m}")
    #fullMakespan += makespan(result[t])

print(f"\n\naz ütemezése makespan-je: {fullMakespan}")







