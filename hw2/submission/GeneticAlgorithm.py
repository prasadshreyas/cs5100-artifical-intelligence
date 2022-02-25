from random import randint
from random import random
from math import sqrt
from math import ceil


def newList(length, goal):
    lst = []
    while length > 0:
        lst.append(randint(0, ceil(sqrt(goal))))
        length -= 1
    return lst


def populationList(popSize, length, goal):

    popList = []

    while popSize > 0:
        popList.append(newList(length, goal))
        popSize -= 1
    return popList



def fitness(individual, goal):
    
    # Ideal fitness alue = 0
    
    squaredSum = 0
    
    for num in individual:
        squaredSum += num * num
    
    
    #print(abs(goal - squaredSum))
    return abs(goal - squaredSum)


def evolve(popList, goal, retain=0.2, random_select=0.05, mutate=0.01):

    popGrades = []
    parents = []
    for lst in popList:
        popGrades.append(fitness(lst, goal))

    # deep copy of population List
    population = list(popList)

    parentPopSize = round(len(popList) * retain)

    # adds the percentage specified of the population to the parents list
    while parentPopSize > 0:

        fit = popGrades[0]
        count = 0
        fittest = 0
        for g in popGrades:
            if g < fit:
                fit = g
                fittest = count
            count += 1

        parents.append(population[fittest])
        population.pop(fittest)
        popGrades.pop(fittest)
        parentPopSize -= 1

    # selects some random individuals and adds them to the population as well
    for lst in population:
        if random_select > random():
            parents.append(lst)

    # random muatations for more genetic diversity
    for parent in parents:
        if mutate > random():
            randPosition = randint(0, len(parent) - 1)
            parent[randPosition] = randint(0, ceil(sqrt(goal)))

    # crossing over
    parentsLength = len(parents)
    desiredLength = len(popList) - parentsLength

    children = []

    while len(children) < desiredLength:
        par1 = randint(0, parentsLength - 1)
        par2 = randint(0, parentsLength - 1)

        if par1 != par2:
            par1 = parents[par1]
            par2 = parents[par2]
            # each parentis weighed a random amount rather than a 50/50 split
            split = randint(0, len(par1))
            child = par1[:split] + par2[split:]
            children.append(child)

    children.extend(parents)

    return children


def listOfSquaredSums(length, goal, retain=0.25, random_select=0.1, mutate=0.05):

    popSize = 200

    popList = populationList(popSize, length, goal)

    solved = False
    count = 0

    while not solved:
        popList = (evolve(popList, goal, retain, random_select, mutate))
        print(popList)  # for troubleshooting
        for i in popList:
            if (fitness(i, goal) == 0):
                print("\n\nThe fitness has reached zero\n")
                print("\nThe final array is:\n")
                print(i)
                
                solved = True
                break
        if solved is True:
            break

        # will modify mutation, random_select and retain values to help leave a
        # local maxima. More randomness the longer it takes.
        if count % 20 == 0:
            if mutate < 0.5:
                mutate += 0.01
            if random_select < 0.5:
                random_select += 0.01
            if retain > 0.15:
                retain -= 0.01

        count += 1
    return


    
n = input("\nInput N\n")
v = input("\nInput V\n")
listOfSquaredSums(int(n), int(v))

