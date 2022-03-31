# CS 420/CS 527 Lab 4: Neuroevolution with LEAP
# Catherine Schuman
# March 2022
import os
import sys
import gym
import matplotlib.pyplot as plt
import numpy as np
import argparse
from toolz import pipe
from leap_ec import Individual, Representation, test_env_var
from leap_ec import probe, ops, util
from leap_ec.algorithm import generational_ea
from leap_ec.real_rep.initializers import create_real_vector
from leap_ec.real_rep.ops import mutate_gaussian
from leap_ec.binary_rep.problems import ScalarProblem
from leap_ec.decoder import IdentityDecoder
from distributed import Client
from leap_ec.distrib import DistributedIndividual
from leap_ec.distrib import synchronous

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
            for i in range(5):
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
    parser = argparse.ArgumentParser(description="CS 420/CS 527: Neuroevolution")
    parser.add_argument("--environment", type=str, help="OpenAI Gym Environmetn")
    parser.add_argument("--inputs", type=int, help="Number of inputs")
    parser.add_argument("--hidden", type=int, help="Number of hidden")
    parser.add_argument("--outputs", type=int, help="Number of outputs")
    parser.add_argument("--trn_size", type=int, default=5, help="Tournament size")
    args = parser.parse_args() 
    max_generation = 50
    N = 100

    num_inputs = args.inputs 
    num_actions = args.outputs
    num_hidden = args.hidden
    layers = [num_inputs, num_hidden, num_actions]
    
    # Calculate the total length of the genome
    total_weights = 0
    for i in range(len(layers)-1):
        total_weights += layers[i]*layers[i+1]

    # Spin up Dask for distributed evaluation
    with Client() as client:
   
        # Set up the parents 
        parents = DistributedIndividual.create_population(N,
                                           initialize=create_real_vector(bounds=([[-1, 1]]*total_weights)),
                                           decoder=IdentityDecoder(),
                                           problem=OpenAIGymProblem(layers, args.environment))

        # Calculate initial fitness values for the parents
        parents = synchronous.eval_population(parents, client=client)

        # Loop over generations
        for current_generation in range(max_generation):
            offspring = pipe(parents,
                         ops.tournament_selection(k=5),
                         ops.clone,
                           mutate_gaussian(std=0.05, hard_bounds=(-1, 1), expected_num_mutations=int(0.01*total_weights)),
                         ops.uniform_crossover,
                         synchronous.eval_pool(client=client, size=len(parents)))

            fitnesses = [net.fitness for net in offspring]
            print("Generation ", current_generation, "Max Fitness ", max(fitnesses))
            parents = offspring

    # Find the best network in the final population
    index = np.argmax(fitnesses)
    best_net = parents[index]
    
    # TODO: You may want to change how you save the best network
    print("Best network weights:") 
    print(best_net.genome)
    with open('bestGenome_{}.txt'.format(args.hidden), 'w') as f:
        for weight in best_net.genome:
            f.write("%s\n" % weight)
    f.close()
