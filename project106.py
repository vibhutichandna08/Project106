import numpy as np
import csv
import plotly_express as px
import pandas as pd


def getDataSource(data_path):
    Marks = []
    Days = []
    with open(data_path) as f:
        df = csv.DictReader(f)
        for row in df:
            Marks.append(float(row['Marks In Percentage']))
            Days.append(float(row['Days Present']))
        return {'x': Marks, 'y': Days}


def findCorrelation(datasource):
    correlation = np.corrcoef(datasource['x'], datasource['y'])
    print(correlation[0, 1])


def plotFigure(data_path):
    with open(data_path) as f:
        reader = pd.read_csv(f)
        fig = px.scatter(reader, x='Roll No', y='Marks In Percentage')
        fig.show()


def setup():
    data_path = './student.csv'
    data_source = getDataSource(data_path)
    findCorrelation(data_source)
    plotFigure(data_path)


setup()
