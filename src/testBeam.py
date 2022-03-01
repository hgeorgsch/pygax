"""
(C) 2022: Hans Georg Schaathun <hasc@ntnu.no>

A basic, generic, GA implementation for testing and instruction.
"""

from BinaryChromosome import *
from BinaryBeam import Beam
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
    beam = Beam(r,f5d3)
    beam.initPopulation(100)
    cs = beam.evolve(100)
    for c in cs: print( f"{c[0]} - {str(c[1])}" )
