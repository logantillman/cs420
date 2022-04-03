# Logan Tillman
# Ltillma4

# To run this program, use the following command:
# python3 test_network.py --environment <environment name> --inputs <num inputs> --outputs <num outputs>

import sys
import gym
import numpy as np
import argparse
from leap_ec.binary_rep.problems import ScalarProblem

class Network:
    # The network constructor takes as input an array where
    # layers[0] is the number of neurons in the first (input) layer
    # layers[1] is the number of neurons in the hidden layer
    # layers[2] is the number of neurons in the output layer 
    def __init__(self, layers):
        self.layers = layers
   
    # TODO: This function will take as input a list of the weight values and 
    #       setup the weights in the network based on that list
    def set_weights(self, weights):
        # TODO: Complete this function

        # Setting up the weight matrices
        w1 = []
        row = []
        for i in range(self.layers[0] * self.layers[1]):
            if (i % self.layers[1] == 0 and i != 0):
                w1.append(row)
                row = []
            row.append(weights[i])
        w1.append(row)
        self.w1 = w1

        w2 = []
        row = []
        weights2 = weights[self.layers[0] * self.layers[1]:]
        for i in range(self.layers[1] * self.layers[2]):
            if (i % self.layers[2] == 0 and i != 0):
                w2.append(row)
                row = []
            row.append(weights2[i])
        w2.append(row)
        self.w2 = w2
        
    # TODO: This network will take as input the observation and it will
    #       calculate the forward pass of the network with that input value
    #       It should return the output vector
    def forward_pass(self, obs):
        # TODO: Complete this function
        hidden = np.zeros(self.layers[1])
        out = np.zeros(self.layers[2])

        # print('1', len(obs), len(hidden), 'ji', len(self.w1[0]), len(self.w1))

        for i in range(len(hidden)):
            runningTotal = 0
            for j in range(len(obs)):
                runningTotal += self.w1[j][i] * obs[j]
            hidden[i] = max(runningTotal, 0)

        # print('2', len(out), len(hidden), 'ij', len(self.w2), len(self.w2[0]))
        
        for i in range(len(out)):
            runningTotal = 0
            for j in range(len(hidden)):
                runningTotal += self.w2[j][i] * hidden[j]
            out[i] = max(runningTotal, 0)

        return out
    
# Implementation of a custom problem
class OpenAIGymProblem(ScalarProblem):
    def __init__(self, layers, env_name):
        super().__init__(maximize=True)
        self.layers = layers
        self.env_name = env_name
        self.net = Network(layers)

    # TODO: Implement the evaluate function as described in the write-up
    def evaluate(self, ind):
        try:
            self.net.set_weights(ind)
            env = gym.make(self.env_name)

            scores = []
            for i in range(100):
                score = 0
                observation = env.reset()
                while True:
                    action = np.argmax(self.net.forward_pass(observation))
                    observation, reward, done, info = env.step(action)
                    score += reward
                    if done:
                        break
                scores.append(score)
            return np.average(scores)
        except IndexError as ie:
            print(ie)
        except:
            print('ERROR', sys.exc_info()[0])

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="CS 420/CS 527: Neuroevolution Testing")
    parser.add_argument("--environment", type=str, help="OpenAI Gym Environmetn")
    parser.add_argument("--inputs", type=int, help="Number of inputs")
    parser.add_argument("--outputs", type=int, help="Number of outputs")
    args = parser.parse_args() 

    hiddenOptions = [10, 20, 30, 40, 50]
    
    for num_hidden in hiddenOptions:
        layers = [args.inputs, num_hidden, args.outputs]
        problem = OpenAIGymProblem(layers, args.environment)
        genome = []
        for i in range(10):
            f = open("data/{}_bestGenome_{}.txt".format(num_hidden, i), "r")
            for line in f:
                genome.append(float(line))
            f.close()

            averageFitness = problem.evaluate(genome)
            f = open('data/testAvgFitness_{}.txt'.format(num_hidden), 'a')
            f.write("%s\n" % str(averageFitness))
            f.close()