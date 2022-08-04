import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H5('Altere o valor na caixa abaixo para testar o callback!', style={'margin-bottom':'15px'}),
    html.Div(['Entrada:',
                dcc.Input(id='my-input', value='Valor inicial', type='text')]),
    html.Br(),
    html.Div(id='my-output'),
    
])

@app.callback(
    Output(component_id='my-output',component_property='children'),
    Input(component_id='my-input',component_property='value'),  
)

def update_output_div(value):
    return 'Saída: {}'.format(value)

if __name__ == '__main__':
    app.run_server(debug=True)