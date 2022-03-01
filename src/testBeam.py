"""
(C) 2022: Hans Georg Schaathun <hasc@ntnu.no>

A basic, generic, GA implementation for testing and instruction.
"""

from BinaryChromosome import *
from BinaryBeam import Beam
import numpy as np
import sys

from TestFunctions import *

if __name__ == "__main__":
    r = BinaryRepresentation(-20,+20,16,dim=3)
    beam = Beam(r,f5d3)
    beam.initPopulation(100)
    beam.evolve(100)
    print( beam.getSolution() )
