# pygax: Genetic Algorithm Exercises and Demoes in python

This code is created to support exercises and tutorials in a
taught module on artificial intelligence.  The implementation 
is meant to be conceptually simple and flexible, at the expense 
of speed.  Also, error checks have generally not been implemented,
and there has been no attempt to pack it up as a proper python
module for reuse.

The code is crude.  Please suggest improvements.

## Binary GA for floating point problems

The demo contains three classes.

### BinaryChromosome.BinaryRepresentation

The `BinaryRepresentation` class is used to map between 
floating point vectors in the solution space and binary
vectors in the chromosome space.

You set up a representation by instantiating `BinaryRepresentation` 
with three parameters, the minimum value, maximum value, and number
of bits for each dimension.  

The representation object provides two important methods:
`getFloat()` to map from chromosome to floating point vector,
and `getGene()` for the inverse mapping. It also has the
`makePopulation()` method to make a random population, using
`BinaryChromosome` objects as defined below.

### BinaryChromosome.BinaryChromosome

A `BinaryChromosome` object is a chromosome to be used with the
`GA` solver below.

There is a test script in the script section of the file,
testing and demonstrating the main principles.

### GA.GA

The `GA` class sets up a generic genetic algorithm.  Mating, crossover,
and mutation functions are given as arguments to the constructor.
The module also contains some simple default implementations of these
functions.

A `GA` object is intialised with a representation object (see above)
and a cost function.  The other critical methods are

1.  `initPopulation(size)` to initialise a population of a given size.
2.  `evolve(ngen)` to evolve the given number of generations
3.  `sortCost()` to get a sorted list of costs and chromosomes.

An example is given in the script section at the bottom of the file.

## Local Beam Search

For the sake of comparison we provide an implementation of Local Beam Search.

## BinaryBeam.Beam

This class follows the same structure as `GA`, assuming a binary 
representation.  As the test script shows, it is used in the same
way.

By using the binary representation, we have a finite number of 
neighbours at Hamming distance one, and every such neighbour is
considered.

Note that we can run the local beam search with a population size
of one to make a straight-forward hill climbing search.

## Testing

In addition to the test script sections in the modules themselves,
two additional test scripts `testGA.py` and `testBeam.py` are provided,
optimising a three-dimensional function.  The test functions are 
implemented in the `TestFunctions` module.
