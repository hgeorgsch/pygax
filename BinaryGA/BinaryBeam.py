"""
(C) 2022: Hans Georg Schaathun <hasc@ntnu.no>

A basic local beam search using a binary representation.
This is built on the `GA` implementation, using the same
structure and much of the same logic.
"""

from BinaryChromosome import *
from TestFunctions import *
from GA import GA
import numpy as np
import sys


# The GA proper
class Beam(GA):
    # def __len__(self): 
    def __init__(self,representation,costfunction,debug=1):
        """
        Initialise the Beam Search with a given representation and cost function.

        Arguments:
            representation : representation object defining the mapping from variables to chromosomes
            costfunction : the costfunction to minimise
        """
        self.costfunction = costfunction
        self.representation = representation
        self.population = None
        self.debug = debug


    # def initPopulation(self,size):
    # def evolve(self,ngen=1):

    def _init(self,*args,**kw):
        "Initialisations specific to Beam Searches."
        # We override this to be able to use a generic `initPopulation` method
        pass
    def nextGeneration(self):
        """Evolve one generation."""

        if self.debug > 0: 
            print(f"Evolving Generation {self.generation}. Population size {len(self)}.",
                    file=sys.stderr)

        k = self.populationsize

        offspring = []
        for chrom in self.population:
            for i in range(len(chrom)):
                offspring.append(chrom.flipCopy(i))

        # Calculate the cost function; list of cost/chromosome pairs
        cost = [ (self.cost(x),x) for x in offspring ]
        # Note that we have not included the old population here.
        # It could be a good idea to include that, to avoid oscilating
        # between an optimal solution and its neighbours.

        cost.sort( key=lambda x : x[0] )
        if self.debug > 0: 
            print(f"Mimimum {cost[0][0]} - {cost[0][1]} out of {len(cost)} chromosomes.",
                    file=sys.stderr)

        # Extract new population
        self.population = [ y for (x,y) in cost[:k] ]

        # Advance the generation count
        self.generation += 1

        return cost

if __name__ == "__main__":
    r = BinaryRepresentation(-20,+20,16)
    beam = Beam(r,f1)
    beam.initPopulation(100)
    for c in beam.population: print(str(c),file=sys.stderr)
    beam.evolve(100)
    print( beam.getSolution() )
