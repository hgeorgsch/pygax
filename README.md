# pygax: Genetic Algorithm Exercises and Demoes in python

This code is created to support exercises and tutorials in a
taught module on artificial intelligence.  The implementation 
is meant to be conceptually simple and flexible, at the expense 
of speed.  Also, error checks have generally not been implemented.

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

### GA.GA

The `GA` class sets up a generic genetic algorithm.  Mating, crossover,
and mutation functions are given as arguments to the constructor.
The module also contains some simple default implementations of these
functions.
