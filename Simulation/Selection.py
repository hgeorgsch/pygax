"""
Selection functions for GA.
"""

import numpy as np

def toscalar(x):
    if np.isscalar(x):
        return x
    else:
        return x.item()

def proportionalSelect(pop,size=None):
    "Proportional selection."

    # Scale costs to [0,1] range
    costs = [ toscalar(x[0]) for x in pop ] 
    c0 = min(costs)
    costs = [ c+c0 for c in costs ]
    max = sum( costs )
    probs = [ x/max for x in costs ]

    # Pick out the chromosomes
    pops = [ x[1] for x in pop ] 

    # Number of chromosomes to select
    if size == None:
        size = len(pop)

    # Pick mates
    newpop = np.random.choice(pops,size,p=probs)

    # Pair mates
    r = []
    for i in range(0,size-1,2):
        r.append( (newpop[i],newpop[i+1]) )
    return r


