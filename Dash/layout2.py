import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd
from requests import options

app = dash.Dash(__name__)

app.layout = html.Div([
    html.Label('Dropdow'),
    dcc.Dropdown(
        id='dp_1',
        options=[{'label':'Rio Grande do Sul', 'value':'RS'},
                {'label':'Santa Cataria', 'value':'SC'},
                {'label':'Paraná', 'value':'PR'}],
            value='RS', style={'margin-bottom':'25px'}
    ),

    html.Label('Checklist',style={'margin-bottom':'15px'}),
    dcc.Checklist(
        id='cl_1',
        options=[{'label':'Rio Grande do Sul', 'value':'RS'},
                {'label':'Santa Cataria', 'value':'SC'},
                {'label':'Paraná', 'value':'PR'}],
        value=['RS'],
        style={'margin-bottom':'25px'}
    ),

    html.Label('Text Input'),
    dcc.Input(value='SC', type='text', style={'margin-bottom':'25px'}),

    html.Label('Slider'),
    dcc.Slider(
        min=0,
        max=9,
        marks={i:'Label {}'.format(i) if i==1 else str(i) for i in range(1,6)},
        value=5,
    )

])


if __name__ == '__main__':
    app.run_server(debug=True)