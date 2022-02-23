import os
import math 

dir = 'lab2_data'
sortedDir = sorted(os.listdir(dir), key=lambda fn: (int(fn.split("_")[1]), float(fn.split("_")[2]), float(fn.split("_")[3]), int(fn.split("_")[4]), int(fn.split("_")[5].split(".")[0])))
# sortedDir = sortedDir[:2]

generation = 0
avgFitness = 0
bestFitness = 0
fitnessSum = 0
bestGenome = 0
solutionFound = 0
numSolutionsFound = 0
i = 0
j = 0
fout = open('Master.csv', 'w')
fout.write('Logan Tillman\n')
fout.write('\n\n')
fout.write('N, p_m, p_c, tournament_size, iteration, generation, average_fitness, best_fitness, best_genome, solution_found, num_solutions_found, diversity_metric,,\n')

generationList = []
iterationList = []
popDistances = []
popDisAvg = []
stepAverage = []

for fileName in sortedDir:
    fin = open('lab2_data/' + fileName, 'r')
    N = int(fileName.split('_')[1])
    pm = fileName.split('_')[2]
    pc = fileName.split('_')[3]
    trnSize = fileName.split('_')[4]
    itar = fileName.split('_')[5].split('.')[0]

    tmp = 0
    for line in fin:
        splitLine = line.split(',')
        if splitLine[0] == 'step':
            if tmp == 0:
                tmp += 1
            else:
                iterationList.append(generationList)
                generationList = []
            continue
        genome = splitLine[2]
        genomeArray = genome.replace(' ', ',').split('[')[1].split(']')[0].split(',')
        genomeArray = [int(i) for i in genomeArray]
        generationList.append(genomeArray)
    iterationList.append(generationList)
    generationList = []
    
    it = 0
    for iteration in iterationList:
        ge = 0
        for generation in iteration:
            co = 0
            for compare in iteration:
                runningSum = 0
                if co == ge:
                    co += 1
                    continue
                for u, v in zip(generation, compare):
                    runningSum += (u-v) ** 2
                co += 1
                dis = math.sqrt(runningSum)
                popDistances.append(dis)
            # print(len(popDistances))
            runningSum = 0
            for dis in popDistances:
                runningSum += dis
            popDisAvg.append(runningSum / len(popDistances))
            popDistances = []
            ge += 1

        runningSum = 0
        # print(len(popDisAvg))
        for avg in popDisAvg:
            runningSum += avg
        totAvg = runningSum / len(popDisAvg)
        stepAverage.append(totAvg)
        popDisAvg = []
        it += 1
    # print(stepAverage)
    fin.seek(0)

    for line in fin:
        splitLine = line.split(',')
        if splitLine[0] == 'step':
            avgFitness = fitnessSum / N
            if i != 0:
                # print(genar, avgFitness, bestFitness, bestGenome, solutionFound, numSolutionsFound)
                fout.write(str(N) + ',' + pm + ',' + pc + ',' + trnSize + ',' + itar + ',' + str(genar) + ',' + str(avgFitness) + ',' + str(bestFitness) + ',' + str(bestGenome.split('\n')[0]) + ',' + str(solutionFound) + ',' + str(numSolutionsFound) + ',' + str(stepAverage[genar]) + ',,\n')
            else:
                i += 1
            genar = 0
            avgFitness = 0
            bestFitness = 0
            fitnessSum = 0
            bestGenome = 0
            solutionFound = 0
            numSolutionsFound = 0
            iterationList = []
            j = 0
            continue

        genar = int(splitLine[0])
        fitness = float(splitLine[1])
        genome = splitLine[2]

        fitnessSum += fitness
        genCopy = genome
        genomeArray = genome.replace(' ', ',').split('[')[1].split(']')[0].split(',')
        genomeArray = [int(i) for i in genomeArray]

        # print(j, generation, genomeArray)
        if fitness == 1.0:
            solutionFound = 1
            numSolutionsFound += 1

        if fitness > bestFitness:
            bestFitness = fitness
            bestGenome = genCopy
        
        # iterationList.append(genomeArray)
        j += 1
    
    # print(genar, avgFitness, bestFitness, bestGenome, solutionFound, numSolutionsFound)
    avgFitness = fitnessSum / N

    fout.write(str(N) + ',' + pm + ',' + pc + ',' + trnSize + ',' + itar + ',' + str(genar) + ',' + str(avgFitness) + ',' + str(bestFitness) + ',' + str(bestGenome.split('\n')[0]) + ',' + str(solutionFound) + ',' + str(numSolutionsFound) + ',' + str(stepAverage[genar]) + ',,\n') 
    genar = 0
    avgFitness = 0
    bestFitness = 0
    fitnessSum = 0
    bestGenome = 0
    solutionFound = 0
    numSolutionsFound = 0
    iterationList = []
    stepAverage = []
    j = 0
    i = 0
    fin.close()
fout.close()