import dash_bootstrap_components as dbc
from dash import html
import dash

app = dash.Dash(__name__,external_stylesheets=[dbc.themes.COSMO])
server = app.server

app.layout = html.Div([
    dbc.Row([
        dbc.Col(html.Div('Column1'), style={'background':'#ff0000'}, md=6),
        dbc.Col(html.Div('Column2'), md=3),
        dbc.Col(html.Div('Column3'), md=3),
    ]),
    dbc.Row([
        dbc.Card(
    dbc.CardBody(
        [
            html.H4("Title", className="card-title"),
            html.H6("Card subtitle", className="card-subtitle"),
            html.P(
                "Some quick example text to build on the card title and make "
                "up the bulk of the card's content.",
                className="card-text",
            ),
            dbc.CardLink("Card link", href="#"),
            dbc.CardLink("External link", href="https://google.com"),
        ]
    ),
    style={"width": "18rem"},
)
    ]),

    dbc.Row(
        html.Div(
    [
        dbc.Button("Primary", color="primary", className="me-1"),
        dbc.Button("Secondary", color="secondary", className="me-1"),
        dbc.Button("Success", color="success", className="me-1"),
        dbc.Button("Warning", color="warning", className="me-1"),
        dbc.Button("Danger", color="danger", className="me-1"),
        dbc.Button("Info", color="info", className="me-1"),
        dbc.Button("Light", color="light", className="me-1"),
        dbc.Button("Dark", color="dark", className="me-1"),
        dbc.Button("Link", color="link"),
    ]
)
    )
])



if __name__ == '__main__':
    app.run_server(debug=True)