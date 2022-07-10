import pandas as pd
import csv
import plotly.graph_objects as go
import plotly.express as px
data=pd.read_csv('Average Distance of Sports.csv')
graph=px.scatter(data,x='Sports',y='Distance(km)')
graph.show()
