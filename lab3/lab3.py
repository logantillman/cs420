# Name: Logan Tillman
# NetID: Ltillma4

# Instructions for running: "python3 lab3.py <Number of neurons> <Number of patterns>"


import sys
from random import randrange
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import math

# Check to make sure the correct command line arguments are used
if (len(sys.argv) != 3):
    print("Usage: python3 lab3.py <N> <P>")
    exit()

N = int(sys.argv[1])
P = int(sys.argv[2])

# Imprinting p patterns onto the network
def imprintPatterns(p, vectors, weights, P, N):
    for i in range(N):
        for j in range(N):
            weight = 0
            if i != j:
                for a in range(p):

                    # Calculating the weight
                    weight += vectors[a][i] * vectors[a][j]
                weight *= (1 / N)
            weights[i][j] = weight

# Testing p patterns for stability
def testStability(p, vectors, weights, numStableVec):
    numStable = 0
    for a in range(p):
        networkState = vectors[a]
        newState = []
        isStable = True

        # Computing the new state
        for i in range(len(weights)):
            h = 0
            for j in range(len(weights[i])):
                h += weights[i][j] * networkState[j]
            if h < 0:
                newState.append(-1)
            else:
                newState.append(1)

        # Checking to see if the pattern is stable
        for i, j in zip(networkState, newState):
            if i != j:
                isStable = False
        if isStable:
            numStable += 1
    numStableVec.append(numStable)

# Calculates the average for each number in a list
def average(data):
    result = []
    for col in range(len(data[0])):
        runningSum = 0
        for row in range(len(data)):
            runningSum += data[row][col]
        result.append(runningSum / len(data))
    return result

# Calculates the standard deviation for each number in a list
def stdev(plot2Data, plot2DataAvg):
    result = []
    tmp = np.ndarray(shape=(len(plot2Data),len(plot2Data[0])))
    for col in range(len(plot2Data[0])):
        for row in range(len(plot2Data)):
            tmp[row][col] = (plot2Data[row][col] - plot2DataAvg[col]) ** 2
   
    for col in range(len(tmp[0])):
        runningSum = 0
        for row in range(len(tmp)):
            runningSum += tmp[row][col]
        mean = runningSum / len(tmp)
        result.append(math.sqrt(mean))
    return result

# Adds two lists together
def add(avg, dev):
    result = np.ndarray(shape=(len(avg)))
    for i in range(len(avg)):
        result[i] = avg[i] + dev[i]
    return result

# Subtracts two lists from each other
def sub(avg, dev):
    result = np.ndarray(shape=(len(avg)))
    for i in range(len(avg)):
        result[i] = avg[i] - dev[i]
    return result

plot1Data = []
plot2Data = []

# Repeats the process for 5 collections of patterns
for run in range(5):
    vectors = []
    weights = np.ndarray(shape=(N,N))
    numStableVec = []

    # Generating bipolar vectors
    for i in range(P):
        bipolarVector = []
        for j in range(N):
            rand = randrange(-1, 2, 2)
            bipolarVector.append(rand)
        vectors.append(bipolarVector)

    # Imprinting p patterns and testing the stability
    for p in range(P):
        imprintPatterns(p+1, vectors, weights, P, N)
        testStability(p+1, vectors, weights, numStableVec)

    # Calculating the unstable probabilities
    unstableProbs = []
    for i, numStable in enumerate(numStableVec):
        prob = numStable / (i + 1)
        unstableProbs.append(1 - prob)

    # Getting x data for graphing
    x = []
    for i in range(len(unstableProbs)):
        x.append(i+1)
    
    # Saving the results for later graphing
    plot1Data.append(unstableProbs)
    plot2Data.append(numStableVec)


# Creating the graphs
colors = cm.rainbow(np.linspace(0, 1, 5))

for i, run in enumerate(plot1Data):
    plt.plot(x, run, color=colors[i], alpha=0.5, label='Experiment {}'.format(i+1))
plt.title("Probability of Unstable Imprints N={} P={}".format(N, P))
plt.xlabel("Number of Imprints (p)")
plt.ylabel("Fraction of Unstable Imprints")
plt.legend()
plt.savefig("{}_{}_UNSTABLE1.pdf".format(N, P))
# plt.show()
plt.close()

plot1DataAvg = average(plot1Data)
plot1DataDev = stdev(plot1Data, plot1DataAvg)
plot1Add = add(plot1DataAvg, plot1DataDev)
plot1Sub = sub(plot1DataAvg, plot1DataDev)
plt.plot(x, plot1DataAvg, color=colors[0], alpha=0.5, label='Average')
plt.plot(x, plot1Add, color=colors[1], alpha=0.5, label='Average + STDev')
plt.plot(x, plot1Sub, color=colors[2], alpha=0.5, label='Average - STDev')
plt.title("Number of Unstable Imprints N={} P={}".format(N, P))
plt.xlabel("Number of Imprints (p)")
plt.ylabel("Number of Unstable Imprints")
plt.legend()
plt.savefig("{}_{}_UNSTABLE2.pdf".format(N, P))
# plt.show()
plt.close()

for i, run in enumerate(plot2Data):
    plt.plot(x, run, color=colors[i], alpha=0.5, label='Experiment {}'.format(i+1))
plt.title("Number of Stable Imprints N={} P={}".format(N, P))
plt.xlabel("Number of Imprints (p)")
plt.ylabel("Number of Stable Imprints")
plt.legend()
plt.savefig("{}_{}_STABLE1.pdf".format(N, P))
# plt.show()
plt.close()

plot2DataAvg = average(plot2Data)
plot2DataDev = stdev(plot2Data, plot2DataAvg)
plot2Add = add(plot2DataAvg, plot2DataDev)
plot2Sub = sub(plot2DataAvg, plot2DataDev)
plt.plot(x, plot2DataAvg, color=colors[0], alpha=0.5, label='Average')
plt.plot(x, plot2Add, color=colors[1], alpha=0.5, label='Average + STDev')
plt.plot(x, plot2Sub, color=colors[2], alpha=0.5, label='Average - STDev')
plt.title("Number of Stable Imprints N={} P={}".format(N, P))
plt.xlabel("Number of Imprints (p)")
plt.ylabel("Number of Stable Imprints")
plt.legend()
plt.savefig("{}_{}_STABLE2.pdf".format(N, P))
# plt.show()
plt.close()