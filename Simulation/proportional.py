"""
(C) 2022: Hans Georg Schaathun <hasc@ntnu.no>

A GA simulation of the cobweb model.
"""

import sys,getopt
sys.path.append("../BinaryGA/")
from BinaryChromosome import BinaryRepresentation

from GASim import *
from Selection import *

import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    ngen = 100
    size = 200
    hstring='GASim.py --alpha avalue -o <outputfile>'
    alpha = 0.25
    outputfile = None
    print("System arguments:", sys.argv)

    try:
        opts, args = getopt.getopt(sys.argv[1:],"A:o:g:p:",["alpha=","file=","ngen=","size="])
    except getopt.GetoptError:
      print(hstring)
      sys.exit(2)
    print("Options:", opts, args)
    for opt, arg in opts:
      if opt == '-h':
          print(hstring)
          sys.exit()
      elif opt in ("-A", "--alpha"):
          alpha = float(arg)
      elif opt in ("-o", "--file"):
          outputfile = arg
          print(f"Output file: {outputfile}")
      elif opt in ("-g", "--ngen"):
          ngen = int(arg)
      elif opt in ("-p", "--size"):
          size = int(arg)
    print(f"alpha={alpha}")
    print(f"Number of Generations: {ngen}")

    cobweb = CobWeb(alpha=alpha)
    r = BinaryRepresentation(0,1,bits=64)
    ga = GASim(r,cobweb,mate=proportionalSelect)
    ga.initPopulation(size)
    ga.sim(ngen)
    (xprice,yprice,xsol,ysol,xavg,yavg) = ga.getplotdata()
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.scatter(xsol,ysol,color="red",marker=".",s=0.1,label="Strategies")
    ax1.plot(xprice,yprice,color="green",label="Price")
    ax1.plot(xavg,yavg,color="black",linestyle="dotted",label="Average strategy")
    plt.legend(loc="upper right")
    if outputfile != None:
       plt.savefig(outputfile)
    else:
        plt.show()


