
import math

class Machine:
    def __init__(self) -> None:
        self.jobs = []
        self.load = 0
    
    def add(self, job):
        self.jobs.append(job)
        self.load += job

class Shelf:
    def __init__(self, height) -> None:
        self.jobs = []
        self.height = height
        self.remainingWidth = 1
        self.open = True

    def add(self, job):
        self.remainingWidth -= job[0]
        self.jobs.append(job)

def bestFit(input):
    machines = [Machine()]
    
    for job in input:
        d = math.inf
        candidate = machines[0]
        found = False
        for m in machines:
            if(1-m.load-job <= d and m.load+job <= 1):
                candidate = m
                d = 1-m.load-job
                found = True
                
        if(found):
            candidate.add(job)
        else:
            m = Machine()
            m.add(job)
            machines.append(m)
    
    return machines

def firstFit(input):
    machines = [Machine()]
    
    for job in input:
        found = False
        for m in machines:
            if(m.load+job <= 1):
                m.add(job)
                found = True
                break
        if(not found):
            m = Machine()
            m.add(job)
            machines.append(m)
    
    return machines

def nextFit(input):
    machines = [Machine()]
    idx = 0
    for job in input:
        if(machines[idx].load + job <= 1):
            machines[idx].add(job)
        else:
            m = Machine()
            m.add(job)
            idx += 1
            machines.append(m)
    return machines

def nextFitShelf(r, input):
    shelves = []
    for i in range(5):
        if(input[0][1] > r**(i+1) and input[0][1] <= r**i):
            s = Shelf(r**i)
            s.add(input[0])
            shelves.append(s)
    input = input[1:]
    print(input)
    
    height = 0
    for job in input:
        found = False
        #mekkorara fer ra
        for i in range(6): # zhba ez ugyis eleg lol
            # print(r**(i+1) <= job[1])
            # print(job[1])
            # print(job[1] < r**(i))
            if(job[1] > r**(i+1) and job[1] <= r**i):
                height = r**i
        for s in shelves:
            if(s.open == True):
                if(s.height == height):
                    if(s.remainingWidth >= job[0]):
                        print(s.remainingWidth)
                        s.add(job)
                        found = True
                        break
                    else:
                        s.open = False
                        new = Shelf(height)
                        new.add(job)
                        shelves.append(new)
                        found = True
                        break
                
        if(not found):
            new = Shelf(height)
            new.add(job)
            shelves.append(new)
            found = False
                
    
    return shelves
                

# scheduling = nextFit([0.5, 0.6, 0.3, 0.4, 0.2, 0.5, 0.4])
# print(len(scheduling))
# for m in scheduling:
#     print(m.jobs)

scheduling = nextFitShelf(0.5, [(0.4,0.6), (0.6, 0.6), (0.5,0.4), (0.5,0.3), (0.7,0.1), (0.2, 0.1)])
print(len(scheduling))
for s in scheduling:
    print(f"{s.jobs}, {s.height}")