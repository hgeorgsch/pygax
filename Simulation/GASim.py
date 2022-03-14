"""
(C) 2022: Hans Georg Schaathun <hasc@ntnu.no>

A GA simulation of the cobweb model.
"""

import sys,getopt
sys.path.append("../BinaryGA/")
from GA import *
from BinaryChromosome import BinaryRepresentation

import numpy as np
import matplotlib.pyplot as plt

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
    """
    A variant of the `GA` class to simulate economic markets.
    In this case the cost function changes from generation to 
    generation, depending on the player strategies (chromosomes).
    Only a few methods are overridden, to keep a reference to the
    market model instance and to update the cost function at
    the start of each generation, before the costs are evaluated.
    """
    def __init__(self,representation,market,
            mate=simpleMate,crossover=simpleCrossover,mutate=simpleMutate,selectionrate=0.5,debug=2):
        """
        Initialise the GA with a given representation and cost function.

        Arguments:
            representation : representation object defining the mapping from variables to chromosomes
            market : an instance of a market model, such as CobWeb.
            mate : function to select mating pairs
            crossover : the crossover function
            mutate : the mutation function (must work in place)
            selectionrate : the fraction of the population to keep

        Note that if the selection rate is 1 or greater, the population
        is not sorted before mating.
        """
        self.market = market
        return GA.__init__(self,representation,market.cost,mate,crossover,mutate,selectionrate,debug)

    def setprice(self):
        "Set the price given the current population of strategies."
        q = [ self.representation.getFloat(x) for x in self.population ]
        self.market.setprice(q)
    def getpop(self):
        "Return the decoded chromosomes (player strategies)."
        return [ self.representation.getFloat(x) for x in self.population ]
    def sortcost(self):
        """
        Calculate costs and sort chromosome.
        The return value is a list of cost/chromosome pairs.
        """
        self.setprice()
        return GA.sortcost(self)
    def nextGeneration(self):
        """Evolve one generation."""
        self.setprice()
        return GA.nextGeneration(self)
    def sim(self,ngen=100):
        """
        Run a simulation over `ngen` generations, recording prices and
        player strategies for each generation. These data can be retrieved
        for plotting.
        """
        self.setprice()
        self.pricelist = [ self.market.price ]
        self.poplist = [ self.getpop() ]
        for i in range(ngen):
            r = self.nextGeneration()
            self.pricelist.append( self.market.price )
            self.poplist.append( self.getpop() )
        return r
    def getplotdata(self):
        "Prepare dataset for plotting"
        x = range(self.generation+1)
        price = self.pricelist
        sol = self.poplist
        sol = [ [ (x,y) for y in z ] for (x,z) in zip(x,sol) ]
        sol = sum(sol,[])
        xsol = [ x for (x,y) in sol ]
        ysol = [ y for (x,y) in sol ]
        return ( x,price, xsol,ysol )


if __name__ == "__main__":
    ngen = 100
    hstring='GASim.py --alpha avalue -o <outputfile>'
    alpha = 0.25
    outputfile = None
    print("System arguments:", sys.argv)
    try:
        opts, args = getopt.getopt(sys.argv[1:],"A:o:g:",["alpha=","file=","ngen="])
    except getopt.GetoptError:
      print(hstring)
      sys.exit(2)
    print("Options:", opts, args)
    for opt, arg in opts:
      if opt == '-h':
          print(hstring)
          sys.exit()
      elif opt in ("-A", "--alpha"):
          alpha = float(arg)
      elif opt in ("-o", "--file"):
          outputfile = arg
          print(f"Output file: {outputfile}")
      elif opt in ("-g", "--ngen"):
          ngen = int(arg)
    print(f"alpha={alpha}")
    print(f"Number of Generations: {ngen}")

    cobweb = CobWeb(alpha=alpha)
    r = BinaryRepresentation(0,1,bits=12)
    ga = GASim(r,cobweb)
    ga.initPopulation(200)
    ga.sim(ngen)
    (xprice,yprice,xsol,ysol) = ga.getplotdata()
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.scatter(xsol,ysol,color="red",marker=".",s=0.1,label="Strategies")
    ax1.plot(xprice,yprice,color="green",label="Price")
    plt.legend(loc="lower right")
    if outputfile != None:
       plt.savefig(outputfile)
    else:
        plt.show()


