
# coding: utf-8

# In[57]:


#! /usr/bin/env python

# imports of external packages to use in our code
import sys
import numpy as np

# import our Random class from RandomOrbitParmGenerator.py file
#sys.path.append(".")
from RandomOrbitParmGenerator import RandomOrbitElement

# main function for our Orbit stability Python code
if __name__ == "__main__":
    # if the user includes the flag -h or --help print the options
    if '-h' in sys.argv or '--help' in sys.argv:
        print ("Usage: %s [-seed number]" % sys.argv[0])
        print
        sys.exit(1)

    # default seed
    seed = 5555

    # default number of orbiting planets around the Sun
    Nplanets = 2

    # default number of system testing (per experiment)
    Nsystem = 1

    # default number of experiments
    Nexp = 1

    # output file defaults
    doOutputFile = False

    # read the user-provided seed from the command line (if there)
    if '-seed' in sys.argv:
        p = sys.argv.index('-seed')
        seed = sys.argv[p+1]
    if '-Nplanets' in sys.argv:
        p = sys.argv.index('-Nplanets')
        np = float(sys.argv[p+1])
        if np >= 0 and np <= 1:
            Nplanets = np
    if '-Nsystem' in sys.argv:
        p = sys.argv.index('-Nsystem')
        Ns = int(sys.argv[p+1])
        if Ns > 0:
            Nsystem = Ns
    if '-Nexp' in sys.argv:
        p = sys.argv.index('-Nexp')
        Ne = int(sys.argv[p+1])
        if Ne > 0:
            Nexp = Ne
    if '-output' in sys.argv:
        p = sys.argv.index('-output')
        OutputFileName = sys.argv[p+1]
        doOutputFile = True

    # class instance of our Random class using seed
    random = RandomOrbitElement(seed)

    if doOutputFile:
        outfile = open(OutputFileName, 'w')
        for e in range(0,Nexp):
            for t in range(0,Nsystem):
                outfile.write(str(random.hill_parms(Nplanets))+" ")
            outfile.write(" \n")
        outfile.close()
    else:
        for e in range(0,Nexp):
            for t in range(0,Nsystem):
                print(random.hill_parms(Nplanets), end=' ')
            print(" ")
