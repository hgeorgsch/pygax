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
    print(pop)
    costs = [ toscalar(x[0]) for x in pop ] 
    print(costs)
    max = sum( costs )
    probs = [ x/max for x in costs ]
    print(probs)
    if size == None:
        size = len(pop)
    newpop = pop[np.random.choice(len[pop],size,p=probs)]
    print( "Size", len(pop), size, len(newpop) )
    r = []
    for i in range(0,size-1,2):
        r.append( (newpop[i],newpop[i+1]) )
    return r


