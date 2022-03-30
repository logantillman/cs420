import gym
import numpy as np

def evaluate(self, ind):
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

genome = []

f = open('bestGenome_10.txt', 'r')
for line in f:
    genome.append(float(line))

for i in range(100):
    evaluate(genome)