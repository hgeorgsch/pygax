"""
(C) 2022: Hans Georg Schaathun <hasc@ntnu.no>

A basic, generic, GA implementation for testing and instruction.
"""

from BinaryChromosome import *
import numpy as np
import sys


# Default auxiliary functions
def simpleMutate(x,cprob=0.05,gprob=0.05):
    if np.random.rand() < cprob:
        l = len(x)
        bc = int(np.ceil(l*gprob))
        ic = np.random.randint(l,size=bc)
        x.flip(ic)
    return x
def simpleMutateFunction(cprob=0.05,gprob=0.05):
    return lambda x : simpleMutate(x,cprob,gprob)

def simpleMate(pop):
    r = []
    i = 0
    l = len(pop)
    for i in range(0,l-1,2):
        r.append( (pop[i],pop[i+1]) )
    return r
def simpleCrossover(x,y):
    l = len(x)
    assert l == len(y), "Chromosomes has to have the same length"
    cp = np.random.randint(l)
    x1 = np.hstack( [ x.gene[:cp], y.gene[cp:] ] )
    y1 = np.hstack( [ y.gene[:cp], x.gene[cp:] ] )
    return (BinaryChromosome(x1),BinaryChromosome(y1))


# The GA proper
class GA:
    def __len__(self): 
        if self.population == None: return 0
        else: return len(self.population)
    def __init__(self,representation,costfunction,
            mate=simpleMate,crossover=simpleCrossover,mutate=simpleMutate,selectionrate=0.5):
        """
        Initialise the GA with a given representation and cost function.

        Arguments:
            representation : representation object defining the mapping from variables to chromosomes
            costfunction : the costfunction to minimise
            mate : function to select mating pairs
            crossover : the crossover function
            mutate : the mutation function (must work in place)
            selectionrate : the fraction of the population to keep

        Note that if the selection rate is 1 or greater, the population
        is not sorted before mating.
        """
        self.costfunction = costfunction
        self.representation = representation
        self.mate = mate
        self.crossover = crossover
        self.mutate = mutate
        self.selectionrate = selectionrate
        self.population = None


    def initPopulation(self,size):
        "Initialise a population of the given size."
        self.population = self.representation.makePopulation(size)
        self.generation = 0
        self.populationsize = size
        self.Nselect = 2*np.ceil(self.selectionrate*size/2)

    def cost(self,x):
        v = self.representation.getFloat(x) 
        c = self.costfunction( v )
        print( f"{str(x.gene)} -> {v} -> {c}" )
        return c

    def evolve(self,ngen=1):
        """Evolve the given number of generations."""
        for i in range(ngen):
            self.nextGeneration()

    def nextGeneration(self):
        """Evolve one generation."""

        print(f"Evolving Generation {self.generation}. Population size {len(self)}.",file=sys.stderr)

        # Calculate the cost function; list of cost/chromosome pairs
        cost = [ (self.cost(x),x) for x in self.population ]

        # Sort and keep the best
        if self.Nselect >= len(self):
            cost.sort( key=lambda x : x[0] )
            cost = cost[:self.Nselect]
            print( cost[0], file=sys.stderr )
        # Note that we do not sort if we keep all the chromosomes

        print(f"Nselect {self.Nselect}.", file=sys.stderr)
        print(f"Best chromosome {cost[0]}. Population size {len(cost)}.",file=sys.stderr)

        # Make mating pairs
        pairs = self.mate(cost)

        # Make offspring with the crossover function
        offspring = [ self.crossover(x,y) for ((cx,x),(cy,y)) in pairs ]

        # Add the offspring to the population
        for x in offspring:
            self.population.extend(x)

        # Mutate
        for x in self.population:
            self.mutate(x)

        # Advance the generation count
        self.generation += 1

        return self.population

# Test function
def f1(x): return sum(np.abs(x) + np.cos(x))

def f5(x,n): 
    l = [ np.abs(x[i]) - 10*np.cos(np.sqrt(np.abs(10*x[i]))) for i in range(n) ]
    return sum( l )
f5d3 = lambda x : f5(x,3)

if __name__ == "__main__":
    r = BinaryRepresentation(-20,+20,16)
    ga = GA(r,f1)
    ga.initPopulation(20)
    for c in ga.population: print(str(c),file=sys.stderr)
    ga.evolve(20)
