# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

import data

test_df = data.countries_df.iloc[0:3]

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
# df = pd.DataFrame({
#     "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
#     "Amount": [4, 1, 2, 2, 4, 5],
#     "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
# })

df = pd.DataFrame({"Country": [j for i in test_df.index for j in test_df["Country_Region"]],
                   "Total": [j.iloc[i] for j in [test_df["Confirmed"],
                                                 test_df["Deaths"],
                                                 test_df["Recovered"]] for i in test_df.index],
                   "Status": [status for status in test_df.columns[1:4] for j in test_df.index]
                   })

fig = px.bar(df, x="Country", y="Total", color="Status", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Corona19 DashBoard'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
