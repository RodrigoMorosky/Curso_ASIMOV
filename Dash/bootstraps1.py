import dash_bootstrap_components as dbc
from dash import html
import dash

app = dash.Dash(__name__,external_stylesheets=[dbc.themes.COSMO])
server = app.server

card_content = [
    dbc.CardHeader("Card header"),
    dbc.CardBody(
        [
            html.H5("Card title", className="card-title"),
            html.P(
                "This is some card content that we'll reuse",
                className="card-text",
            ),
        ]
    ),
]

app.layout = html.Div([
    dbc.Row([
        dbc.Col([
            dbc.Card(card_content,color='primary',inverse=True, style={'height':'27vh'})
        ]),
        dbc.Col([
            dbc.Row([dbc.Card(card_content,color='secondary',inverse=True)]),
            dbc.Row([dbc.Card(card_content,color='info',inverse=True)])
        ]),
    ])
])




if __name__ == '__main__':
    app.run_server(debug=True)