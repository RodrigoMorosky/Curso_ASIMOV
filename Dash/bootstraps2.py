import dash
from dash import html, dcc, dash_table
from dash.dependencies import Input, Output, State
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template

load_figure_template('cerulean')

app = dash.Dash(external_stylesheets=[dbc.themes.CERULEAN])
server = app.server

df_data = pd.read_csv(r'C:\Users\rodri\OneDrive\Documents\Cursos\ASIMOV\testes\Dash\supermarket_sales.csv')
df_data['Date'] = pd.to_datetime(df_data['Date'])
df_data['City'].unique()
df_teste = df_data.groupby('City')['Total'].sum()
#-------------------Layout--------------#
app.layout = html.Div(children=[
    dbc.Row([
        dbc.Col([
            dbc.Card([
                html.H4('Cidades:'),

                dcc.Checklist(df_data['City'].unique(),
                df_data['City'].unique(),
                id='check_city',
                inputStyle={'margin-right':'5px','margin-left':'20px'}),
                html.Hr(),

                html.H4('Variável de análise', className='teste'),

                dcc.RadioItems(['gross income','Rating'],'gross income', id='main_variable',inputStyle={'margin-right':'5px'})
            ], style={'height':'90vh','margin':'20px','padding':'10px'})
        ],sm=2),

        dbc.Col([
            dbc.Row([
                dbc.Col([dcc.Graph(id='city_fig'),],sm=4),
                dbc.Col([dcc.Graph(id='gender_fig')],sm=4),
                dbc.Col([dcc.Graph(id='pay_fig'),],sm=4),
            ]),
            dbc.Row([dcc.Graph(id='income_per_date')]),
            dbc.Row([dcc.Graph(id='income_per_product_fig')]),
            
            
        ],sm=10,style={'height':'90vh'}),
    ]),
    dbc.Row([
        dash_table.DataTable(df_teste.to_dict('records'),[{'name':i,'id':i} for i in df_data.columns]),
        dash_table.DataTable()
    ])
])



#-------------------Callback--------------#
@app.callback(
    [Output('city_fig','figure'),
    Output('pay_fig','figure'),
    Output('gender_fig','figure'),
    Output('income_per_date','figure'),
    Output('income_per_product_fig','figure')],

    [Input('check_city','value'),
    Input('main_variable','value'),]
)

def render_graph(cities,main_variable):
    operation = np.sum if main_variable == 'gross income' else np.mean
    df_filtred = df_data[df_data['City'].isin(cities)]

    df_city = df_filtred.groupby('City')[main_variable].apply(operation).to_frame().reset_index()
    df_gender = df_filtred.groupby(['Gender','City'])[main_variable].apply(operation).to_frame().reset_index()
    df_city_payment = df_filtred.groupby('Payment')[main_variable].apply(operation).to_frame().reset_index()
    df_income_time = df_filtred.groupby('Date')[main_variable].apply(operation).to_frame().reset_index()
    df_product_income = df_filtred.groupby(['City','Product line'])[main_variable].apply(operation).to_frame().reset_index()

    fig_city = px.bar(df_city, x='City', y=main_variable)
    fig_payment = px.bar(df_city_payment, y='Payment', x=main_variable, orientation='h')
    fig_gender = px.bar(df_gender, x='Gender', y=main_variable, color='City', barmode='group')
    fig_income_date = px.bar(df_income_time, y=main_variable, x='Date')
    fig_product_income = px.bar(df_product_income, x=main_variable, y='Product line',color='City',orientation='h',barmode='group')

    fig_city.update_layout(margin=dict(l=0,r=0,t=20,b=20),height=200,template='cerulean')
    fig_payment.update_layout(margin=dict(l=0,r=0,t=20,b=20),height=200,template='cerulean')
    fig_gender.update_layout(margin=dict(l=0,r=0,t=20,b=20),height=200,template='cerulean')
    fig_income_date.update_layout(margin=dict(l=0,r=0,t=20,b=20),height=200,template='cerulean')
    fig_product_income.update_layout(margin=dict(l=0,r=0,t=20,b=20),height=500,template='cerulean')

    return fig_city, fig_payment, fig_gender, fig_income_date, fig_product_income
#-------------------Servidor--------------#

if __name__=='__main__':
    app.run_server(debug=True)