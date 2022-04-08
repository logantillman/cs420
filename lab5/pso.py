# CS 420/CS 527 Lab 5: Particle Swarm Optimization 
# Catherine Schuman
# April 2022

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import argparse

class Particle:
    def __init__(self, position, function):
        self.position = np.array(position)
        self.v = np.array([0,0])
        self.best_position = self.position.copy()
        self.function = function
        
    def update(self, pso):
        self.v = pso.inertia*self.v+pso.phi_1*np.random.random(2)*(np.subtract(self.best_position,self.position))+pso.phi_2*np.random.random(2)*np.subtract(pso.global_best,self.position)
            
        if (self.v[0]**2+self.v[1]**2 > pso.max_vel**2):
            self.v = (pso.max_vel/np.sqrt(self.v[0]**2+self.v[1]**2))*self.v
        
        self.position = np.add(self.position, self.v)
            
        val = pso.Q(self.position, self.function)
        if (val < self.best_val):
            self.best_val = val
            self.best_position = self.position.copy()
        
        if (val < pso.global_best_val):
            pso.global_best_val = val
            pso.global_best = self.position.copy()
        
class PSO:
    def __init__(self, num_particles, inertia, phi_1, phi_2, ww, wh, max_vel, function):
        self.num_particles = num_particles
        self.inertia = inertia
        self.phi_1 = phi_1
        self.phi_2 = phi_2
        self.ww = ww
        self.wh = wh
        self.max_vel = max_vel
        self.function = function
        self.global_best = np.array([0,0])
        self.global_best_val = None
        self.particles = []
        
        for i in range(num_particles):
            p = []
            p.append(np.random.random()*ww-ww/2)
            p.append(np.random.random()*wh-wh/2)
            particle = Particle(p, self.function)
            particle.best_val = self.Q(p, self.function)
            if (self.global_best_val == None or self.global_best_val > particle.best_val):
                self.global_best_val = particle.best_val
                self.global_best[:] = p[:]
            self.particles.append(particle)
            
    
    def Q(self, position, function):
        x = position[0]
        y = position[1]
        # Rosenbrock (banana) function
        val = 0
        if function == "Rosenbrock":
            val=(1-x)**2+100*(y-x**2)**2
        if function == "Booth":
            val=(x + (2 * y) - 7)**2 + ((2 * x) + y - 5)**2

        return val
    
    def update(self):
        for i in range(self.num_particles):
            p = self.particles[i]
            p.update(self)
            
    def scatter_plot(self):
        x = []
        y = []
        for i in range(self.num_particles):
            x.append(self.particles[i].position[0])
            y.append(self.particles[i].position[1])
        return x,y

parser = argparse.ArgumentParser(description="CS 420/CS 527 Lab 5: PSO")
parser.add_argument("--num_particles", default=40, type=int, help="Number of particles")
parser.add_argument("--inertia", default=0.5, type=float, help="Inertia")
parser.add_argument("--cognition", default=1, type=float, help="Cognition parameter")
parser.add_argument("--social", default=1, type=float, help="Social parameter")
parser.add_argument("--function", default="Rosenbrock", type=str, help="Function")
parser.add_argument("--varying", type=str, help="Varying parameter")
    
args = parser.parse_args()
# Print all of the command line arguments
param = ""
d = vars(args)
# for k in d.keys():
#     print(k + str(":") + str(d[k]))
    

# Create PSO
pso = PSO(args.num_particles, args.inertia, args.cognition, args.social, 100, 100, 2, args.function)

for i in range(1000):
    pso.update()
    x,y = pso.scatter_plot()
    error_x = np.sum([(pso.particles[k].position[0]-pso.global_best[0])**2 for k in range(args.num_particles)])
    error_y = np.sum([(pso.particles[k].position[1]-pso.global_best[1])**2 for k in range(args.num_particles)])
    error_x = np.sqrt((1.0/(2*args.num_particles))*error_x)
    error_y = np.sqrt((1.0/(2*args.num_particles))*error_y)
    if (error_x < 0.00001 and error_y < 0.00001):
        break

# print("epoch_stop:", i)
# print("solution_found:", pso.global_best)
# print("fitness:", pso.global_best_val)

if pso.global_best_val <= 1e-10:
    print('yes')
    f = open('data/{:.1f}{}{}'.format(d[args.varying], args.varying, args.function), 'a')
    f.write(str(i) + '\n')
    f.close()
else:
    print("nope")