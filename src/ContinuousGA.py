"""
(C) 2022: Hans Georg Schaathun <hasc@ntnu.no>

A basic, generic, GA implementation for testing and instruction.
"""

from ContinuousChromosome import *
from GA import GA
from TestFunctions import *
import numpy as np
import sys

def ccross(x,y):
    beta = np.random.random_sample( size=len(x) )
    assert len(x) == len(y)
    r1 = beta*x.gene + (1-beta)*y.gene
    r2 = beta*y.gene + (1-beta)*x.gene
    return (ContinuousChromosome(r1),ContinuousChromosome(r2))

if __name__ == "__main__":
    r = ContinuousRepresentation(-20,+20)
    ga = GA(r,f1,crossover=ccross)
    ga.initPopulation(100)
    for c in ga.population: print(str(c),file=sys.stderr)
    ga.evolve(1000)
    print( ga.getSolution() )
