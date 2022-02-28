"""
A basic, generic, GA implementation for testing and instruction.
"""

from BinaryChromosome import *

class GA:
    def __init__(self,representation,costfunction,mate,crossover,mutate,selectionrate=0.5):
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
        self.Nselect = 2*ceil(self.selectionrate*size/2)

    def cost(self,x):
        return self.costfunction(x)

    def evolve(self,ngen=1):
        """Evolve the given number of generations."""
        for i in range(ngen):
            self.nextGeneration()

    def nextGeneration(self):
        """Evolve one generation."""
        # Calculate the cost function; list of cost/chromosome pairs
        cost = [ (self.cost(x),x) for x in self.population ]

        # Sort and keep the best
        if self.Nselect >= self.size:
            cost.sort( key=lambda x : x[0] )
            cost = cost[:self.Nselect]
        # Note that we do not sort if we keep all the chromosomes

        # Make mating pairs
        pairs = self.mate(self.cost)

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

