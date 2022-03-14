# GA Simulation

This directory contains demoes of economic simulations of populations
using Genetic Algorithms.  It is based on a paper by
[Dawid and Kopel 1998](https://link.springer.com/article/10.1007/s001910050066),
and it simulates a market of the cobweb type.
There is a rich literature on this topic, and the interested reader may find a 
lot of publications both on this specific cobweb model and other applications 
of evolutionary algorithms.


The `GASim.py` module provides two classes.  The `CobWeb` class representing
a market of the CobWeb type, and `GASim` which is an adaptation of the original
binary `GA` class to handle the case where the cost function changes for every
generation, depending on the market.

Extra utility functions have also been added to the `GASim` class to record
the evolution for subsequent analysis and plotting.
