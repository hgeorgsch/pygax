"""
Class to represent binary chromosomes, including methods to encode
floating point numbers.
"""

import numpy as np



def makeInt(x,bl):
    "Convert a binary sequence to an integer, reading the least significant bit first."
    return sum( [ x[i]*2**i for i in range(bl) ] )

class BinaryChromosome:
    def __str__(self):
        "Make a compact display string of the the binary vector."
        return"".join([str(x) for x in self.gene])
    def getFloat(self):
        """
        Return the floating point vector represented by the chromosome.
        This is the representation which should be used in the cost function
        for a floating point problem.
        """
        ig = self.getIgene()
        ignorm = ig/2**self.bits
        p = ignorm*(self.pmax-self.pmin)+self.pmin
        return p
    def getIgene(self):
        """
        Return an integer vector representation of the binary chromosome.
        This is mainly an auxiliary for `getFloat()`.
        """
        # if self.igene != None: return self.igene
        ss = []
        s = 0
        for bl in self.bits:
            ss.append( (self.gene[s:s+bl],bl) )
            s += bl
        r = np.array( [ makeInt(x,bl) for (x,bl) in ss ] )
        print("getFloat returning:", r)
        self.igene = r
        return r
    def __init__(self,p=None,pmin=None,pmax=None,bits=None):
        """
        Creates a chromosome from the variable (vector) p.

        Arguments:
            p : The variable as a scalar or numpy array
            pmin : The minimum value of each variable in p
            pmax : The maximum value of each variable in p
            bits : The number of bits to encode each variable of p

        **Warning** No error checking is implemented.
        """
        gene = []

        # Mormalise p to [0,1] range
        pnorm = (p - pmin)/(pmax - pmin)
        # Quantise pnorm and represent as an integer of required length 
        pi = pnorm*2**bits
        pi = np.rint(pi).astype(int)
        # If bits is a scalar, turn it into an array
        if np.isscalar(bits):
            bits = bits*np.ones(pi.size,dtype=np.int8)
        # Binary code pi
        for (x,b) in zip(pi,bits):
            for i in range(b):
                # Note! least significant bit is first
                gene.append(x%2)
                x >>= 1
        self.pmax = pmax
        self.pmin = pmin
        self.bits = bits
        self.gene = gene
        self.igene = pi

# Test Data
Amin = np.array([0,0,0])
Amax = np.array([10,10,10])
A = np.array([1,9,4])

if __name__ == "__main__":
    b = BinaryChromosome(A,Amin,Amax,4)
    print("Original vector:", A)
    print("Integer representation:", b.igene)
    print("Chromosome representation:", b)
    print("Reconstructed after quantisation:", b.getFloat())

