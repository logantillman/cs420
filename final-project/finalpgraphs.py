import matplotlib.pyplot as plt
import numpy as np

selectionTypes = ["cyc", "elite", "prop", "rand", "trn", "trunc"]
typedOut = ["Cyclic Selection", "Elitist Survival", "Proportional Selection", "Random Selection", "Tournament Selection", "Truncation Selection"]
xData = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i, selType in enumerate(selectionTypes):
    yData = []
    f = open('data/{}_train_maxFitness.txt'.format(selType))
    for line in f:
        yData.append(float(line))
    f.close()
    plt.plot(xData, yData, '.-', label=typedOut[i])

plt.legend(title='Selection Method', loc='center left', bbox_to_anchor=(1, 0.5))
plt.xlabel('Test Run #')
plt.xticks(xData)
plt.ylabel('Fitness Value')
plt.title('Maximum Training Fitness Value In Last Epoch')
# plt.show()
plt.savefig("graphs/traningPerf.pdf", bbox_inches="tight")
plt.close()


for i, selType in enumerate(selectionTypes):
    yData = []
    f = open('test/{}_testAvgFitness.txt'.format(selType))
    for line in f:
        yData.append(float(line))
    f.close()
    plt.plot(xData, yData, '.-', label=typedOut[i])

plt.legend(title='Selection Method', loc='center left', bbox_to_anchor=(1, 0.5))
plt.xlabel('Test Run #')
plt.xticks(xData)
plt.ylabel('Fitness Value')
plt.title('Average Testing Fitness Value')
# plt.show()
plt.savefig("graphs/testingPerf.pdf", bbox_inches="tight")
plt.close()



selectionTypes = ["prop", "trn"]

for selType in selectionTypes:
    # allData = []
    xData = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    numbers = []
    legendLabel = ""
    title = ""
    if selType == "prop":
        numbers = [2, 3, 5]
        legendLabel = "Exponent"
        title = "Proportional Selection"
    else:
        numbers = [2, 5, 10]
        legendLabel = "Tournament Size"
        title = "Tournament Selection"
    for number in numbers:
        yData = []
        f = open('test/{}{}_testAvgFitness.txt'.format(selType, number), 'r')
        for line in f:
            yData.append(float(line))
        f.close()
        plt.plot(xData, yData, '.-', label=number)
        # allData.append(data)

    # plt.boxplot(allData, labels=numbers)
    plt.xlabel('Test Run #')
    plt.xticks(xData)
    plt.ylabel('Fitness Value')
    plt.legend(title=legendLabel, loc='center left', bbox_to_anchor=(1, 0.5))
    plt.title('{} Average Testing Performance'.format(title))
    # plt.show()
    plt.savefig("graphs/{}TestingPerf.pdf".format(selType), bbox_inches="tight")
    plt.close()