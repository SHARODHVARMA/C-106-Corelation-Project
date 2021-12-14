import plotly.express as px
import csv
import numpy as np

def getDataSource(data_path):
    IceCreamSales = []
    ColdDrinkSales = []

    with open(data_path) as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            IceCreamSales.append(float(row["week"]))
            ColdDrinkSales.append(float(row["Coffee in ml"]))

    return {"x":IceCreamSales, "y":ColdDrinkSales}

def findCorelation(dataSource):
    corelation = np.corrcoef(dataSource["x"],dataSource["y"])
    print("Corelation between the Week and the Coffee in ml : \n--->",corelation[0,1])

def setup():
    data_path = "Coffee.csv"
    dataSource = getDataSource(data_path)
    findCorelation(dataSource)

setup()