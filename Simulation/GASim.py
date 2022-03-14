"""
(C) 2022: Hans Georg Schaathun <hasc@ntnu.no>

A GA simulation of the cobweb model.
"""

import sys
sys.path.append("../BinaryGA/")
from GA import GA
from BinaryChromosome import BinaryRepresentation

import numpy as np

class CobWeb:
    """
    A rudimentary implementation of the cost function in the 
    CobWeb model according to Dawid and Kopel 1998.
    The `setprice()` method must be called with a vector/list
    of all the player strategies before the `cost()` method is
    called to calculate the cost (negative fitness) of a given 
    strategy.
    """
    def __init__(self,a=5,alpha=0.5,beta=1,gamma=5):
        """
        Instantiate a CobWeb model.  The parameters are as used
        by Dawid and Kopel (1998), see Equations (8) and (9).
        To replicate their experiments, alpha should be set to
        0.25 and to 1, while the other parameters should be
        as given by default.
        """
        self.a = a
        self.alpha = alpha
        self.beta = beta
        self.gamma = gamma
        self.price = 0
        # This is the correction term in Equation (7) (Dawid and Kopel 1998)
        self.profitcorrection = alpha + beta*(a/gamma)**2
    def setprice(self,q):
        """
        Given a list q of all player strategies, set the price for 
        which the market clears.
        """
        # This is Equation (2) in Dawid and Kopel (1998), with
        # $\gamma = bn$ as defined just after Equation (5). 
        self.price = self.a - self.gamma*sum(q)/len(q)
    def cost(self,x):
        "Calculate the cost function for the given strategy x."
        # Profit and Cost are defined by Dawid and Kopel (1998) at
        # the start of Section 3.1
        cost = self.alpha+self.beta*x**2
        if x > 0:
            profit = x*self.price - cost
        else:
            profit = 0
        return -profit


class GASim(GA):
    def __init__(self,representation,market,
            mate=simpleMate,crossover=simpleCrossover,mutate=simpleMutate,selectionrate=0.5,debug=2):
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

        Hint. To change the mutation rate in the default mutation function,
        you can use lambda functions.  For example,
        `mutate=lambda x : simpleMutate(x,cprob=0.01,gprob=0.1)`.
        """
        self.market = market
        return GA.__init__(self,representation,market.cost,mate,crossover,mutate,selectionrate,debug)

    def nextGeneration(self):
        """Evolve one generation."""
        q = [ self.representation.getFloat(x) for x in self.population ]
        self.market.setprice(q)
        return GA.nextGeneration(self)


if __name__ == "__main__":
    cobweb = CobWeb(alpha=0.25)
    r = BinaryRepresentation(0,1,bits=12)
    ga = GASim(r,cobweb)
    ga.initPopulation(1000)
    for c in ga.population: print(str(c),file=sys.stderr)
    # Evolve step by step
    print( ga.getSolution() )
