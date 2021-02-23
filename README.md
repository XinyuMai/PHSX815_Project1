# PHSX815_Project1
## stability simulation of planetary system using Hill criterion (e..g. Chambers et al. 1996): >1 => stable

This repository contains severeal types of programs:
RandomOrbitParmGenerator.py [Python]
OrbitCounter.py [Python]
OrbitAnalysis.py [Python]
Constants.py [Python]

## Usage
RandomOrbitParmGenerator.py [Python] is imported to generate list of random chosen orbit parameter values for each planet around star [in the program, default as our sun], Orbit parameter values are generated to calculate fractional orbital separation for examination of stability of two bodies system, Hill stability Criterion \citep{Gladman:1993, Chambers:1996}. The critical value of 1 is taken to indicate mutual close encounter for a two bodies system. H > 1 indicating stable configuration of two pairs, whereas H < 1 indicating unstabe configuration. 

OrbitCounter.py [Python] can be called from the command line with the -h or --help flag, which will print the options. One can set up number of planets orbiting the sun, number of systems per experiment and number of experiements. It will examine each system's stability with N_planets specified and returen integer 0 or 1 as stable system or unstable system. The output file is stored and passed to OrbitAnalysis.py for result analysis.

OrbitAnalysis.py [Python] will take different hypthesis of N_planets in the system and compare each case stability. (In development)

Constants.py [Python] includes used constants in calculation, can be imported from file.
