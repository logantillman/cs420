import os

dir = 'lab2_data'
sortedDir = sorted(os.listdir(dir), key=lambda fn: (int(fn.split("_")[1]), float(fn.split("_")[2]), float(fn.split("_")[3]), int(fn.split("_")[4]), int(fn.split("_")[5].split(".")[0])))

generation = 0
avgFitness = 0
bestFitness = 0
fitnessSum = 0
bestGenome = 0
solutionFound = 0
numSolutionsFound = 0
i = 0
fout = open('Master.csv', 'w')
fout.write('Logan Tillman\n')
fout.write('\n\n')
fout.write('N, p_m, p_c, tournament_size, iteration, generation, average_fitness, best_fitness, best_genome, solution_found, num_solutions_found, diversity_metric,,\n')

for fileName in sortedDir:
    fin = open('lab2_data/' + fileName, 'r')
    N = int(fileName.split('_')[1])
    pm = fileName.split('_')[2]
    pc = fileName.split('_')[3]
    trnSize = fileName.split('_')[4]
    iteration = fileName.split('_')[5].split('.')[0]
    for line in fin:
        splitLine = line.split(',')
        if splitLine[0] == 'step':
            avgFitness = fitnessSum / N
            if i != 0:
                # print(generation, avgFitness, bestFitness, bestGenome, solutionFound, numSolutionsFound)
                fout.write(str(N) + ',' + pm + ',' + pc + ',' + trnSize + ',' + iteration + ',' + str(generation) + ',' + str(avgFitness) + ',' + str(bestFitness) + ',' + str(bestGenome.split('\n')[0]) + ',' + str(solutionFound) + ',' + str(numSolutionsFound) + ',' + '0' + ',,\n')
            else:
                i += 1
            generation = 0
            avgFitness = 0
            bestFitness = 0
            fitnessSum = 0
            bestGenome = 0
            solutionFound = 0
            numSolutionsFound = 0
            continue

        generation = splitLine[0]
        fitness = float(splitLine[1])
        genome = splitLine[2]

        fitnessSum += fitness
        if fitness == 1.0:
            solutionFound = 1
            numSolutionsFound += 1

        if fitness > bestFitness:
            bestFitness = fitness
            bestGenome = genome
            
    # print(generation, avgFitness, bestFitness, bestGenome, solutionFound, numSolutionsFound)
    avgFitness = fitnessSum / N
    fout.write(str(N) + ',' + pm + ',' + pc + ',' + trnSize + ',' + iteration + ',' + str(generation) + ',' + str(avgFitness) + ',' + str(bestFitness) + ',' + str(bestGenome.split('\n')[0]) + ',' + str(solutionFound) + ',' + str(numSolutionsFound) + ',' + '0' + ',,\n') 
    fin.close()
fout.close()