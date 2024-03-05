import pandas as pd
import dash
from dash import html, dash_table, dcc
import plotly.graph_objects as go


dash.register_page(__name__, path="/dataset", name="Dataset")


titanic_df = pd.read_csv("titanic.csv")

layout = html.Div(children=[
    html.Br(),
    dash_table.DataTable(data=titanic_df.to_dict("records"),
                          page_size=15,
                          style_cell={"background-color": "lightgrey", "border": "1px solid white", "color": "black", "font-size": "11px", "text-align": "left"},
                          style_header={"background-color": 'dodgerblue', "font-weight": "bold","color": "white", "padding": "10px", "font-size": "18px"}
    )
])