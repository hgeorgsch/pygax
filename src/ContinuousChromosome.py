"""
(C) 2022: Hans Georg Schaathun <hasc@ntnu.no>

Class to represent continuous chromosomes.
"""

import numpy as np
from BinaryChromosome import BinaryChromosome 

class ContinuousRepresentation:
    def makePopulation(self,size):
        """
        Make a population of `size` chromosomes for this representation
        """
        pop = np.random.random_sample( size=( size, self.length ) )
        return [ ContinuousChromosome(gene) for gene in pop ]

    def __init__(self,pmin=None,pmax=None,dim=1):
        """
        Creates a mapping between floating point vectors and
        binary chromosomes, to optimise continuous functions with
        a binary GA.

        Arguments:
            pmin : The minimum value of each variable in p
            pmax : The maximum value of each variable in p
            dim : The length of a solution vector 
        
        The dimension `dim` is ignored if `pmin` is a vector,
        in which case its dimension is also the dimension of the
        solution.  If `pmin` or `pmax` are scalars, the same 
        minimum or maximum applies in all dimensions.

        **Warning** No error checking is implemented.
        """
        if np.isscalar(pmin):
            pmin = pmin*np.ones(dim)
        elif dim > 1:
            dim = len(pmin)
        self.pmin = pmin
        if np.isscalar(pmax):
            self.pmax = pmax*np.ones(dim)
        else:
            self.pmax = pmax
        size = self.pmin.size 
        assert size == self.pmax.size, "pmin and pmax must have the same size"
        self.length = size

    def getFloat(self,gene):
        "Map chromosome from [0,1] range to solution space."
        s = self.pmax - self.pmin
        return gene.gene*s + self.pmin
    def getGene(self,p):
        "Map solution to a chromosome with [0,1] range ."
        s = self.pmax - self.pmin
        return (p-self.pmin)/s

class ContinuousChromosome(BinaryChromosome):
    # def __len__(self):
    # def flip(self,ic):
    def copy(self):
        "Return a copy of the chromosome."
        return ContinuousChromosome(self.gene.copy())
    # def flipCopy(self,i):
    def __str__(self):
        "Make a compact display string of the the binary vector."
        return str(self.gene)
    def __init__(self,p=None,rep=None):
        """
        Creates a chromosome from the variable (vector) p.
        A representation object (e.g. `BinaryRepresentation`) is 
        used to map between the optimisation domain and the 
        chromosome space.

        Arguments:
            p : The variable as a scalar or numpy array
            rep : a representation object

        If p is omitted, a random chromosome is generated.
        IF rep is omitted, p is the chromosome without conversion.

        **Warning** No error checking is implemented.
        """
        if type(p) == np.ndarray:
          if rep == None:
            self.gene = p
          else:
            self.gene = rep.getGene(p)
        else:
            assert p == None, "p should be a numpy array or None"
            self.gene = np.random.random_sample( size=rep.length )


# Test Data
Amin = np.array([0,0,0])
Amax = np.array([10,10,10])
A = np.array([1,9,4])

if __name__ == "__main__":
    r = ContinuousRepresentation(Amin,Amax,4)
    b = ContinuousChromosome(A,r)
    print("Original vector:", A)
    print("Chromosome representation:", b)
    print("Reconstructed:", r.getFloat(b))

