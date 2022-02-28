"""
Class to represent binary chromosomes, including methods to encode
floating point numbers.
"""

import numpy as np



def makeInt(x,bl):
    "Convert a binary sequence to an integer, reading the least significant bit first."
    return sum( [ x[i]*2**i for i in range(bl) ] )

class BinaryRepresentation:
    def makePopulation(self,size):
        """
        Make a population of `size` chromosomes of dimension `dim`.
        """
        return np.random.randint(2, size=( size, self.length ) )
    def __init__(self,pmin=None,pmax=None,bits=None):
        """
        Creates a mapping between floating point vectors and
        binary chromosomes, to optimise continuous functions with
        a binary GA.

        Arguments:
            pmin : The minimum value of each variable in p
            pmax : The maximum value of each variable in p
            bits : The number of bits to encode each variable of p

        **Warning** No error checking is implemented.
        """
        self.pmax = pmax
        self.pmin = pmin
        assert pmin.size == pmax.size, "pmin and pmax must have the same size"
        # If bits is a scalar, turn it into an array
        if np.isscalar(bits):
            bits = bits*np.ones(pmax.size,dtype=np.int8)
        self.bits = bits
        self.length = sum(bits)
    def getFloat(self,gene):
        """
        Return the floating point vector represented by the chromosome.
        This is the representation which should be used in the cost function
        for a floating point problem.
        """
        ig = self.getIgene(gene.gene)
        ignorm = ig/2**self.bits
        p = ignorm*(self.pmax-self.pmin)+self.pmin
        return p
    def getIgene(self,gene):
        """
        Return an integer vector representation of the binary chromosome.
        This is mainly an auxiliary for `getFloat()`.
        """
        ss = []
        s = 0
        for bl in self.bits:
            ss.append( (gene[s:s+bl],bl) )
            s += bl
        r = np.array( [ makeInt(x,bl) for (x,bl) in ss ] )
        print("getFloat returning:", r)
        return r
    def getGene(self,p):
        """
        Get the binary chromosome representting the floating point
        vector p.
        """
        gene = []

        # Mormalise p to [0,1] range
        pnorm = (p - self.pmin)/(self.pmax - self.pmin)
        # Quantise pnorm and represent as an integer of required length 
        pi = pnorm*2**self.bits
        pi = np.rint(pi).astype(int)
        # Binary code pi
        for (x,b) in zip(pi,self.bits):
            for i in range(b):
                # Note! least significant bit is first
                gene.append(x%2)
                x >>= 1
        return gene

class BinaryChromosome:
    def __str__(self):
        "Make a compact display string of the the binary vector."
        return"".join([str(x) for x in self.gene])
    def makePopulation(size,dim):
        """
        Make a population of `size` chromosomes of dimension `dim`.
        """
        pop = np.random.randint(2, size( size, dim ) )
        return [ BinaryChromosome(gene) for gene in pop ]
    def __init__(self,p=None,rep=None):
        """
        Creates a chromosome from the variable (vector) p.
        A representation object (e.g. `BinaryRepresentation`) is 
        used to map between the optimisation domain and the 
        chromosome space.

        Arguments:
            p : The variable as a scalar or numpy array
            rep : a representation object

        If p is omitted, a random chromosome is generated.
        IF rep is omitted, p is the chromosome without conversion.

        **Warning** No error checking is implemented.
        """
        if type(p) == np.ndarray:
          if rep == None:
            self.gene = p
          else:
            self.gene = rep.getGene(p)
        else:
            assert p == None, "p should be a numpy array or None"
            self.gene = np.random.randint(2,size=rep.length)


# Test Data
Amin = np.array([0,0,0])
Amax = np.array([10,10,10])
A = np.array([1,9,4])

if __name__ == "__main__":
    r = BinaryRepresentation(Amin,Amax,4)
    b = BinaryChromosome(A,r)
    print("Original vector:", A)
    # print("Integer representation:", b.igene)
    print("Chromosome representation:", b)
    print("Reconstructed after quantisation:", r.getFloat(b))

