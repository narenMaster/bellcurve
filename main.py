import csv
import pandas as pd
import plotly.figure_factory as ff
import plotly_express as px 

df=pd.read_csv("data.csv")
fig=ff.create_distplot([df["Height(Inches)"].to_list()] , ["Height"] , show_hist=False)
fig.show()