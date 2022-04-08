import os


# •Number of particles: 10 to 100, in increments of 10
# •Inertia: 0.1 to 1, in increments of 10
# •Cognition parameter: 0.1 to 4 in increments of 0.1
# •Social parameter: 0.1 to 4 in increments of 0.1

numParticles = 10
inertia = 0.1
cog = 0.1
soc = 0.1
functions = ["Rosenbrock", "Booth"]

for i in range(20):
            command = "python3 pso.py " + "--function " + "Rosenbrock" + " --inertia " + str(1) + " --varying inertia"
            os.system(command)

# while numParticles <= 100:
#     for function in functions:
#         for i in range(20):
#             command = "python3 pso.py " + "--function " + function + " --num_particles " + str(numParticles) + " --varying num_particles"
#             os.system(command)
#     numParticles += 10

# while inertia <= 1.0:
#     for function in functions:
#         for i in range(20):
#             command = "python3 pso.py " + "--function " + function + " --inertia " + str(inertia) + " --varying inertia"
#             os.system(command)
#     inertia += 0.1

# while cog <= 4.0:
#     for function in functions:
#         for i in range(20):
#             command = "python3 pso.py " + "--function " + function + " --cognition " + str(cog) + " --varying cognition"
#             os.system(command)
#     cog += 0.1

# while soc <= 4.0:
#     for function in functions:
#         for i in range(20):
#             command = "python3 pso.py " + "--function " + function + " --social " + str(soc) + " --varying social"
#             os.system(command)
#     soc += 0.1