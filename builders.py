def make_tables(dataframe, max_rows=None):
    import dash_html_components as html
    df = dataframe
    return html.Table(children=[html.Thead(children=[html.Tr(children=[html.Th(i) for i in df.columns])]), html.Tbody(children=[html.Tr(children=[html.Td(j) for j in i]) for i in df.to_numpy()])])
