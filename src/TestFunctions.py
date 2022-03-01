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

def comparestring(a,b):
    na = len(a)
    nb = len(b)
    d = abs(na-nb)
    l = [ x == y for (x,y) in zip(a,b) ]
    c = l.count(False)
    return d + c

s1 = "Like a drunk in a midnight choir"

stringlearn1length = len(s1)
def stringlearn1(x): return comparestring(x,s1)
