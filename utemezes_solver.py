# solver fuggetlen es osszefuggo gepekre vonatkozo 
# utemezesi feladatok megoldasara a lista algoritmussal

class Gep:

    def __init__(self) -> None:
        self.munkak = []
        self.toltes = 0
    
    def utemez(self, munka, toltes):
        self.munkak.append(munka)
        self.toltes += toltes

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

def getMingep(gepek):
    mintoltes = gepek[0].getToltes()
    for g in gepek:
        if g.getToltes() < mintoltes:
            return g
    return gepek[0]

def lista_osszefuggo(m, input):
    #rakjuk a legkisebb toltesu gepre az aktualis munkat
    gepek = [Gep() for _ in range(m)]
    mingep = gepek[0]
    for j in input:
        mingep.utemez(j, j)
        mingep = getMingep(gepek)
    
    for g in gepek:
        print(f"{gepek.index(g)}. gep munkai: {g.munkak},\ttoltese: {g.getToltes()}")



#lista_fuggetlen(3, input=[(1,2,3), (5,2,2), (4,5,4), (4,2,1)])
lista_osszefuggo(3, [1, 2, 3, 4, 5, 6, 7, 8, 9])

