from re import template
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from datas import countries_df, totals_df
from builders import make_tables

# stylesheets = ["https://cdn.jsdelivr.net/npm/reset-css@5.0.1/reset.min.css",
#                'https://fonts.googleapis.com/css2?family=Open+Sans:wght@600&display=swap']

style = ["/assets/style.css"]
app = dash.Dash(__name__, external_stylesheets=style)
map_figures = px.scatter_geo(countries_df,
                             title="Confirmed by Country",
                             size_max=40,
                             locations="Country Region",
                             locationmode="country names",
                             hover_name="Country Region",
                             hover_data={"Confirmed": ":,2f", "Deaths": ":,2f",
                                         "Recovered": ":,2f", "Country Region": False},
                             color="Confirmed",
                             color_continuous_scale=px.colors.sequential.Oryel,
                             size="Confirmed",
                             template="plotly_dark",

                             width=800,
                             height=500,

                             )
map_figures.update_layout(margin_l=10, margin_r=0, margin_t=60, margin_b=0)

fig = px.bar(totals_df,
             x="condition",
             y="count",
             title="Total Global Cases",
             template="plotly_dark",
             labels={"condition": "Condition",
                     "count": "Count", "color": "Condition"},
             hover_data={"count": ":,"},
             color=["Confirmed", "Deaths", "Recovered"])


# fig.update_layout(
#     xaxis={
#         "title": "Condition"
#     },
#     yaxis={
#         "title": "Count"
#     }
# )

app.layout = html.Div(
    children=[
        html.Header(
            children=[
                html.H1(
                    children=["Corona DashBoard"], className="dash-header", style={"fontFamily": "Open Sans, sans-serif"}
                )],
            className="header"
        ),
        html.Div(
            children=[
                html.Div(
                    [
                        dcc.Graph(id="graph", figure=map_figures)
                    ],
                    className="graph-div"
                ),
                html.Div(
                    children=[
                        html.Div(
                            children=[
                                make_tables(countries_df)
                            ],
                            className="table-div-div"
                        )

                    ],
                    className="table-div"
                ),
                html.Div(
                    [dcc.Graph(
                        id="figure", figure=fig
                    )],
                    className="figure-div"
                )
            ],
            className="dash-div"
        ),

    ],
    className="main"
)


if __name__ == '__main__':
    app.run_server(debug=True)
