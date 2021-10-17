# solver fuggetlen es osszefuggo gepekre vonatkozo 
# utemezesi feladatok megoldasara a lista algoritmussal

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



#lista_fuggetlen(2, input=[(1,4), (2, 4), (2, 4), (3, 1), (2, 1) ])
lista_osszefuggo(3, [6, 6, 6, 12, 24, 18, 12], [1,2,3])

