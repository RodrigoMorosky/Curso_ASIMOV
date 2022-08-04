import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import dash_bootstrap_components as dbc

app = dash.Dash(external_stylesheets=[dbc.themes.CYBORG])
server = app.server

df_data = pd.read_csv('supermarket_sales.csv')
df_data['Date'] = pd.to_datetime(df_data['Date'])
df_data['City'].unique()
#-------------------Layout--------------#
app.layout = html.Div(children=[
    html.H4('Cidades:'),

    dcc.Checklist(df_data['City'].unique(),
    df_data['City'].unique(),
    id='check_city'),

    html.H4('Variável de análise', className='teste'),

    dcc.RadioItems(['gross income','Rating'],'gross income', id='main_variable'),

    dcc.Graph(id='city_fig'),
    dcc.Graph(id='pay_fig'),
    dcc.Graph(id='income_per_product_fig')

])



#-------------------Callback--------------#
@app.callback(
    [Output('city_fig','figure'),
    Output('pay_fig','figure'),
    Output('income_per_product_fig','figure')],

    [Input('check_city','value'),
    Input('main_variable','value'),]
)

def render_graph(cities,main_variable):
    operation = np.sum if main_variable == 'gross income' else np.mean
    df_filtred = df_data[df_data['City'].isin(cities)]

    df_city = df_filtred.groupby('City')[main_variable].apply(operation).to_frame().reset_index()
    df_city_payment = df_filtred.groupby('Payment')[main_variable].apply(operation).to_frame().reset_index()
    df_product_income = df_filtred.groupby(['City','Product line'])[main_variable].apply(operation).to_frame().reset_index()

    fig_city = px.bar(df_city, x='City', y=main_variable)
    fig_payment = px.bar(df_city_payment, y='Payment', x=main_variable, orientation='h')
    fig_product_income = px.bar(df_product_income, x=main_variable, y='Product line',color='City',orientation='h',barmode='group')

    fig_city.update_layout(template='plotly_dark')
    fig_payment.update_layout(template='plotly_dark')
    fig_product_income.update_layout(template='plotly_dark')

    return fig_city, fig_payment, fig_product_income
#-------------------Servidor--------------#

if __name__=='__main__':
    app.run_server(debug=True)