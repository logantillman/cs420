import numpy as np
import matplotlib.pyplot as plt

def graph(fileParam, title, start, end, step):
    functions = ['Booth', 'Rosenbrock']
    for func in functions:
        allData = []
        noConvData = []
        xData = []
        for i in np.arange(start, end + (step / 2), step):
            i = round(i , 1)
            try:
                f = open('data/{}/{}{}{}'.format(fileParam, float(i), fileParam, func), 'r')
            except FileNotFoundError:
                noConvData.append(20)
                xData.append(i)
                allData.append(0)
                continue
            data = []
            for line in f:
                data.append(int(line))
            allData.append(data)
            noConvData.append(20 - len(data))
            xData.append(i)
            f.close()
        meanData = []
        for param in allData:
            meanData.append(np.mean(param))
        plt.boxplot(allData, positions=xData)
        plt.plot(xData, meanData)
        plt.title('Varying {} using {}'.format(title, func))
        plt.xlabel('{}'.format(title))
        plt.xticks(rotation=90, horizontalalignment='center')
        plt.ylabel('Epochs to Converge')
        # plt.show()
        plt.savefig('graphs/{}{}.pdf'.format(fileParam, func))
        plt.close()

        plt.title('Number of Runs That Did Not Coverge using {}'.format(func))
        plt.xlabel('{}'.format(title))
        plt.ylabel('Number That Did Not Coverge')
        plt.plot(xData, noConvData)
        # plt.show()
        plt.savefig('graphs/{}{}_2.pdf'.format(fileParam, func))
        plt.close()

graph('num_particles', 'Number of Particles', 10, 100, 10)
graph('cognition', 'Cognition Parameter', 0.1, 4.0, 0.1)
graph('inertia', 'Inertia Parameter', 0.1, 1.0, 0.1)
graph('social', 'Social Parameter', 0.1, 4.0, 0.1)