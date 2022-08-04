from turtle import color
import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd

# folha de estilos externas
# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Com a pasta "assets" existente o Dash já entende que em qualquer arquivo terminado por ".css" estará o estilo  a ser seguido por ele
app = dash.Dash(__name__)

# Fazendo um  Dataframe
df = pd.DataFrame({
    "Frutas": ["Maça","Laranja", "Bananas", "Maça","Laranja", "Bananas"],
    "Quantidade": [4,1,2,2,4,5],
    "Cidade": ["SF","SF","SF","Montreal","Montreal","Montreal"]
})
# Fazendo um gráfico
fig = px.bar(df, x="Frutas", y="Quantidade", color="Cidade")

# Fazendo o layout
app.layout = html.Div(id='div1',
    children=[
        html.H1('Olá Dash!', id='H1', style={'color':'#808080'}), # terceira forma de estilo é colocar o atributo style dentro do componente html
        html.Div("Dash: Um framework web para python", id='div2'),
        dcc.Graph(figure=fig, id='grafico1', style={'color':'#fafad2'}),
        html.H4('Teste de colocar mais coisas na Div principal para ver se dá certo!',id='h4') #aqui eu tentei colcoar mais coisa depois do gráfico
    ]
)


# Rodar o servidor
if __name__ == '__main__':
    app.run_server(debug=True, port='8051')