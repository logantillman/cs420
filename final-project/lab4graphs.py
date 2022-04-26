import matplotlib.pyplot as plt
import numpy as np

hiddenOptions = [10, 20, 30, 40, 50]

alldata = []
allavg = []
for hidden in hiddenOptions:
    f = open('data/maxFitness_{}.txt'.format(hidden), 'r')
    data = []
    for line in f:
        data.append(float(line))
    f.close()
    alldata.append(data)

plt.boxplot(alldata, labels=hiddenOptions)
plt.xlabel('Number of Hidden Neurons')
plt.ylabel('Fitness Value')
plt.title('Maximum Training Value Performance')
plt.savefig("graphs/trainingPerf.pdf")
# plt.show()
plt.close()

alldata = []
allavg = []
for hidden in hiddenOptions:
    f = open('data/testAvgFitness_{}.txt'.format(hidden), 'r')
    data = []
    for line in f:
        data.append(float(line))
    f.close()
    alldata.append(data)

plt.boxplot(alldata, labels=hiddenOptions)
plt.xlabel('Number of Hidden Neurons')
plt.ylabel('Fitness Value')
plt.title('Maximum Testing Value Performance')
plt.savefig("graphs/testingPerf.pdf")
# plt.show()
plt.close()

trnOptions = [2, 10, 20]

alldata = []
allavg = []
for trn in trnOptions:
    f = open('data/ECmaxFitness_{}.txt'.format(trn), 'r')
    data = []
    for line in f:
        data.append(float(line))
    f.close()
    alldata.append(data)

plt.boxplot(alldata, labels=trnOptions)
plt.xlabel('Tournament Size')
plt.ylabel('Fitness Value')
plt.title('Tournament Size Maximum Training Value Performance')
plt.savefig("graphs/trnTrainingPerf.pdf")
# plt.show()
plt.close()


for hidden in hiddenOptions:
    data = []
    for i in range(10):
        f = open('data/maxFitness_{}.txt'.format(hidden), 'r')
        for line in f:
            data.append(float(line))
        f.close()
    f = open('data/trainTableData.txt', 'a')
    f.write('{} MEAN: '.format(hidden) + str(np.mean(data)) + '\n')
    f.write('{} STD: '.format(hidden) + str(np.std(data)) + '\n')
    f.close()

    data = []
    for i in range(10):
        f = open('data/testAvgFitness_{}.txt'.format(hidden), 'r')
        for line in f:
            data.append(float(line))
        f.close()
        f = open('data/testTableData.txt', 'a')
    f.write('{} MEAN: '.format(hidden) + str(np.mean(data)) + '\n')
    f.write('{} STD: '.format(hidden) + str(np.std(data)) + '\n')
    f.close()
