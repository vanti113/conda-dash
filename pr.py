import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from data import countries_df


lists = [1, 2, 3, 4, 5, 6, 7, 8, 9]

z = (x for x in lists for y in lists)

a = []
for x in lists:
    for y in lists:
        a.append(x)
