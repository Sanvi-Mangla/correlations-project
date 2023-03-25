import csv 
import numpy as np
import plotly.express as px

datapath="students_days.csv"

def plotFig(datapath):
    with open (datapath) as f:
        df=csv.DictReader(f)
        fig=px.scatter(df,x="Marks In Percentage",y="Days Present")
        fig.show()


def get_data_source(datapath):
  percentage=[]
  days=[]
  with open(datapath) as f:
    csv_reader=csv.DictReader(f)
    for i in csv_reader:
      percentage.append(float(i["Marks In Percentage"]))
      days.append(float(i["Days Present"]))
  return{"x":percentage,"y":days}



def find_correlations(datasource):
  correlation=np.corrcoef(datasource["x"],datasource["y"])
  print(correlation[0,1])


datasource=get_data_source(datapath)
find_correlations(datasource)
