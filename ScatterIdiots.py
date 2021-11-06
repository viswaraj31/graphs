import pandas as pd
import plotly.express as px

dataframe = pd.read_csv("covid.csv")

fig = px.scatter(dataframe,x = "date",y = "cases",color = "country")
fig.show()