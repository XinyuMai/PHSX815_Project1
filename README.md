# PHSX815_Project1
## Stability simulation of planetary system using Hill criterion (e..g. Chambers et al. 1996)

This repository contains several types of programs: 

* Random.py [Python] 
* OrbitCounter.py [Python]   
* OrbitAnalysis.py [Python] 
* MySort.py [Python] 

## Usage 
* Random.py [Python] is imported to generate list of random chosen orbit parameter values for each planet around star [in the program, assuming two planets orbiting our sun in circular orbit (e=0)], Orbit parameter values are generated to calculate fractional orbital separation for examination of stability of two bodies system, Hill stability Criterion \citep{Gladman:1993, Chambers:1996}. The default critical value of 1 is taken to indicate mutual close encounter for a two bodies system. H > 1 indicating stable configuration of two pairs, whereas H < 1 indicating unstabe configuration. 

* OrbitCounter.py [Python] can be called from the command line with the -h or --help flag, which will print the options. One can set up Hill criterion parameter value in rejecting stable orbit, number of systems per experiment and number of experiements. It will examine each system's stability with 'criterion value' specified and returen integer 0 or 1 as stable system or unstable system. The output file is stored and passed to OrbitAnalysis.py for analysis.

* OrbitAnalysis.py [Python] will take different hypthesis of 'Criterion value' in the system and compare each case stability distribution. It performs hypothesis testing on each dataset by computing LogLiklihood Ratio and find false negative rate.  


## For reviewer (expired)
what sort of review/ feedback would be useful:
* Code Improvement on simulation and other ways of implementing probability distribution
* Any ideas on interpreting simulated result (visualization/approach of hypothesis testing)
