"""
(C) 2022: Hans Georg Schaathun <hasc@ntnu.no>

A basic, generic, GA implementation for testing and instruction.
"""

from BinaryChromosome import *
from GA import GA
import numpy as np
import sys

# Test function
def f1(x): return sum(np.abs(x) + np.cos(x))

def f5(x,n): 
    l = [ np.abs(x[i]) - 10*np.cos(np.sqrt(np.abs(10*x[i]))) for i in range(n) ]
    return sum( l )
f5d3 = lambda x : f5(x,3)

if __name__ == "__main__":
    r = BinaryRepresentation(-20,+20,16,dim=3)
    ga = GA(r,f5d3)
    ga.initPopulation(100)
    ga.evolve(100)
