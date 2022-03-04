# Continuous GA

The `ContinuousChromosome` module is provided for continuous GA.
The API replicates that of `BinaryChromosome`, so that they can be
used almost interchangeably.  
The `ContinuousGA` module demonstrates this, using the original GA
with continuous chromosomes..
An alternative cross-over (mating) function to get decent results,
but the original single-point cross-over could be used.
The most critical difference when adapting binary test scripts
to continuous chromosomes is that the continuous representation
object does not take the `bits` argument to the constructor.
