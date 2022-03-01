"""
Test functions from Haupt and Haupt Appendix I.
"""

import numpy as np

# Test function
def f1(x): return sum(np.abs(x) + np.cos(x))

def f5(x,n): 
    """
    This is F5 of Haupt&Haupt but the minimum they state is not correct,
    as can quickly be observed by checking that x=0 gives negative terms.
    """
    l = [ np.abs(x[i]) - 10*np.cos(np.sqrt(np.abs(10*x[i]))) for i in range(n) ]
    return sum( l )
f5d3 = lambda x : f5(x,3)
