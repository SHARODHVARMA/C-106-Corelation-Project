import plotly.express as px
import csv
import numpy as np

def getDataSource(data_path):
    IceCreamSales = []
    ColdDrinkSales = []

    with open(data_path) as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            IceCreamSales.append(float(row["Roll No"]))
            ColdDrinkSales.append(float(row["Marks In Percentage"]))

    return {"x":IceCreamSales, "y":ColdDrinkSales}

def findCorelation(dataSource):
    corelation = np.corrcoef(dataSource["x"],dataSource["y"])
    print("Corelation between the Roll.No and the Marks in Percentage : \n--->",corelation[0,1])

def setup():
    data_path = "Marks.csv"
    dataSource = getDataSource(data_path)
    findCorelation(dataSource)

setup()