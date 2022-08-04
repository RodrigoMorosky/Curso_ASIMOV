import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
import plotly.express as px
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')
app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Graph(id='graph-with-slier',style={'margin-bottom':'15px'}),
    dcc.Slider(
        id='year-slider',
        min=df['year'].min(),
        max=df['year'].max(),
        value=df['year'].min(),
        marks={str(year): str(year) for year in df['year'].unique()},
        step=None
    )
])

@app.callback(
    Output('graph-with-slier','figure'),
    Input('year-slider','value')
)

def update_figure(selected_year):
    filtered_df = df[df.year == selected_year]

    fig = px.scatter(filtered_df, x='gdpPercap', y='lifeExp',
                    size='pop', color='continent', hover_name='country',
                    log_x=True, size_max=55)
    
    fig.update_layout(transition_duration=600)
    return fig

if __name__=='__main__':
    app.run_server(debug=True)
