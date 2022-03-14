# pygax: Genetic Algorithm Exercises and Demoes in python

This code is created to support exercises and tutorials in a
taught module on artificial intelligence.  The implementation 
is meant to be conceptually simple and flexible, at the expense 
of speed.  Also, error checks have generally not been implemented,
and there has been no attempt to pack it up as a proper python
module for reuse.

The code is crude.  Please suggest improvements.

## Subdirectories

+ [BinaryGA]()
    - all the necessary demoes to optimise floating point functions 
      using a binary GA
+ [ContinuousGA]()
    - builds on BinaryGA adding demoes for floating point chromosomes
+ [TournamentGA]()
    - this variant demonstrates tournament selection.  The API of the
      mating function is not compatible, and the population is not
      sorted.
+ [Simulation]()
    - demo of GA to simulate economic markets

## Releases

- v0.1.0 - prepared for session 3 March 2022
    - the branch v0.1 contains bugfixes

