import csv
from numpy import False_
import pandas as pd
import plotly.figure_factory as ff

df=pd.read_csv("data.csv")
fig=ff.create_distplot([df["Weight(Pounds)"].to_list()],["Weight"],show_hist=False)
fig.show()
