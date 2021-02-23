
# coding: utf-8

# In[57]:


#! /usr/bin/env python

# imports of external packages to use in our code
import sys
import math
import numpy as np
import matplotlib.pyplot as plt

# import our Random class
#sys.path.append(".")
from RandomOrbitParmGenerator import RandomOrbitElement

# main function for our Orbit stability Python code
if __name__ == "__main__":
    # if the user includes the flag -h or --help print the options
    if '-h' in sys.argv or '--help' in sys.argv:
        print ("Usage: %s [-seed number]" % sys.argv[0])
        print
        sys.exit(1)
        
    # default Number of planets for hypothesis 0
    Nplanets0 = 2

    # default Number of planets for hypothesis 1
    Nplanets1 = 4

    haveH0 = False
    haveH1 = False

    if '-Nplanets0' in sys.argv:
        p = sys.argv.index('-Nplanets0')
        np = float(sys.argv[p+1])
        if np >= 0 and np <= 1:
            n0 = np
    if '-Nplanets1' in sys.argv:
        p = sys.argv.index('-Nplanets1')
        np = float(sys.argv[p+1])
        if np >= 0 and np <= 1:
            n1 = np
    if '-input0' in sys.argv:
        p = sys.argv.index('-input0')
        InputFile0 = sys.argv[p+1]
        haveH0 = True
    if '-input1' in sys.argv:
        p = sys.argv.index('-input1')
        InputFile1 = sys.argv[p+1]
        haveH1 = True
    if '-h' in sys.argv or '--help' in sys.argv or not haveH0:
        print ("Usage: %s [options]" % sys.argv[0])
        print ("  options:")
        print ("   --help(-h)          print options")
        print ("   -input0 [filename]  name of file for H0 data")
        print ("   -input1 [filename]  name of file for H1 data")
        print ("   -Nplanets0 [number] number of planets orbiting for H0")
        print ("   -Nplanets1 [number] number of planets orbiting for H1")
        print
        sys.exit(1)
    
    Nsystem = 1
    Npass0 = []
    LogLikeRatio0 = []
    Npass1 = []
    LogLikeRatio1 = []

    Npass_min = 1e8
    Npass_max = -1e8
    LLR_min = 1e8
    LLR_max = -1e8
        
    with open(InputFile0) as ifile:
        for line in ifile:
            lineVals = line.split()
            Nsystem = len(lineVals)
            Npass = 0
            LLR = 0
            for v in lineVals:
                Npass += float(v)
                # adding LLR for this system
                if float(v) >= 1:
                    LLR += math.log( Nplanets1/Nplanets0  )
                else:
                    LLR += math.log( (1.-Nplanets1)/(1.-Nplanets0) )
                    
            if Npass < Npass_min:
                Npass_min = Npass
            if Npass > Npass_max:
                Npass_max = Npass
            if LLR < LLR_min:
                LLR_min = LLR
            if LLR > LLR_max:
                LLR_max = LLR
            Npass0.append(Npass)
            LogLikeRatio0.append(LLR)

    if haveH1:
        with open(InputFile1) as ifile:
            for line in ifile:
                lineVals = line.split()
                Nsystem = len(lineVals)
                Npass = 0
                LLR = 0
                for v in lineVals:
                    Npass += float(v);
                    # adding LLR for this toss
                    if float(v) >= 1:
                        LLR += math.log( Nplanets1/Nplanets0)
                    else:
                        LLR += math.log( (1.-Nplanets1)/(1.-Nplanets0) )

                if Npass < Npass_min:
                    Npass_min = Npass
                if Npass > Npass_max:
                    Npass_max = Npass
                if LLR < LLR_min:
                    LLR_min = LLR
                if LLR > LLR_max:
                    LLR_max = LLR
                Npass1.append(Npass)
                LogLikeRatio1.append(LLR)

    title = str(Nsystem) +  " Number of system(s) / experiment"
    
    # make Npass figure
    plt.figure()
    plt.hist(Npass0, Nsystem+1, density=True, facecolor='b', alpha=0.5, label="assuming $\\mathbb{H}_0$")
    if haveH1:
        plt.hist(Npass1, Nsystem+1, density=True, facecolor='g', alpha=0.7, label="assuming $\\mathbb{H}_1$")
        plt.legend()

    plt.xlabel('$\\lambda = N_{pass}$')
    plt.ylabel('Stability')
    plt.title(title)
    plt.grid(True)

    plt.show()

    # make LLR figure
    plt.figure()
    plt.hist(LogLikeRatio0, Nsystem+1, density=True, facecolor='b', alpha=0.5, label="assuming $\\mathbb{H}_0$")
    if haveH1:
        plt.hist(LogLikeRatio1, Nsystem+1, density=True, facecolor='g', alpha=0.7, label="assuming $\\mathbb{H}_1$")
        plt.legend()

    plt.xlabel('$\\lambda = \\log({\\cal L}_{\\mathbb{H}_{1}}/{\\cal L}_{\\mathbb{H}_{0}})$')
    plt.ylabel('Probability')
    plt.title(title)
    plt.grid(True)

    plt.show()
