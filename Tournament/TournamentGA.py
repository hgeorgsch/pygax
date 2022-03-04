"""
(C) 2022: Hans Georg Schaathun <hasc@ntnu.no>

THis is a variant of the GA in BinaryGA, using tournament selection
by default.  The API for the selection function has been changed,
and the GA does not sort the population, nor do parents carry over
to the next generation.

Elitism is not supported, as this would require sorting.
"""

import numpy as np

import sys
sys.path.append("../BinaryGA/")
from BinaryChromosome import *
from GA import *
from TestFunctions import *

def tournamatch(x,y):
    if x[0] > y[0]: return y[1]
    else: return x[1]
def tournamate(cost,count=None):
    n = len(cost)
    if count == None: count = n 
    r1 = cost[np.random.randint(n,size=count)]
    r2 = cost[np.random.randint(n,size=count)]
    return [ tournamatch(x,y) for (x,y) in zip(r1,r2) ]


# The GA proper
class TournamentGA(GA):

    def __init__(self,representation,costfunction,
            mate=tournamate,crossover=simpleCrossover,mutate=simpleMutate,debug=2):
        GA.__init__(self,representation,costfunction,mate,crossover,mutate,debug)
    def nextGeneration(self):
        """Evolve one generation."""

        if self.debug > 0: 
            print(f"Evolving Generation {self.generation}. Population size {len(self)}.",
                    file=sys.stderr)

        # Calculate the cost function; list of cost/chromosome pairs
        cost = [ (self.cost(x),x) for x in self.population ]

        # Make mating pairs
        pairs = self.mate(cost)

        # Make offspring with the crossover function
        self.population = [ self.crossover(x,y) for (x,y) in pairs ]

        # Mutate
        for x in self.population:
            self.mutate(x)

        # Advance the generation count
        self.generation += 1

        return self.population


if __name__ == "__main__":
    r = BinaryRepresentation(-20,+20,16)
    ga = GA(r,f1)
    ga.initPopulation(100)
    for c in ga.population: print(str(c),file=sys.stderr)
    ga.evolve(100)
    print( ga.getSolution() )
