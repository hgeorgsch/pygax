"""
(C) 2022: Hans Georg Schaathun <hasc@ntnu.no>

A basic, generic, GA implementation for testing and instruction.
"""

from BinaryChromosome import *
from GA import GA
import numpy as np
import sys

from TestFunctions import *

if __name__ == "__main__":
    r = BinaryRepresentation(-20,+20,16,dim=3)
    ga = GA(r,f5d3)
    ga.initPopulation(100)
    ga.evolve(100)
    print( ga.getSolution() )
