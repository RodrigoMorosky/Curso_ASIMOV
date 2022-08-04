from distutils.log import debug
import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd
from sqlalchemy import true

app=dash.Dash(__name__)

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
        html.H1('Olá Dash!', id='H1'),
        html.Div("Dash: Um framework web para python", id='div2'),
        dcc.Graph(figure=fig, id='grafico1'),
        html.H4('Teste de colocar mais coisas na Div principal para ver se dá certo!',id='h4') #aqui eu tentei colcoar mais coisa depois do gráfico
    ]
)


# Rodar o servidor
if __name__ == '__main__':
    app.run_server(debug=True)