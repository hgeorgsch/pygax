"""
Selection functions for GA.
"""

import numpy as np

def proportionalSelect(pop,size=None):
    "Proportional selection.
    costs = [ x[0] for x in pop ] 
    max = sum( costs )
    probs = [ x/max for x in costs ]
    if size == None:
        size = len(pop)
    newpop = pop[npr.choice(size,p=probs)]
    r = []
    for i in range(0,size-1,2):
        r.append( (newpop[i],newpop[i+1]) )
    return r


