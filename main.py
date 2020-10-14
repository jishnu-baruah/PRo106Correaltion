import csv
import plotly.express as px
import numpy as np


def getDataSource(dataPath, x, y):
    xList = []
    yList = []

    with open(dataPath) as f:
        reader = csv.DictReader(f)
        for row in reader:
            xList.append(float(row[x]))
            yList.append(float(row[y]))

    return {'x': xList, "y": yList}


def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource['x'], dataSource['y'])
    print(correlation[0, 1])


def main(dataPath, x, y):
    dataSource = getDataSource(dataPath, x, y)
    findCorrelation(dataSource)


main('./Pro106Corelation/data1.csv', 'Marks In Percentage', 'Days Present')
main('./Pro106Corelation/data2.csv', 'Coffee in ml', 'sleep in hours')
