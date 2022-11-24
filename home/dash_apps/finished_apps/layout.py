import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from django_plotly_dash import DjangoDash
from home.models import graphdata
import pandas as pd
import plotly.express as px
import numpy as np
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

querry_result = graphdata.objects.all()
graph_data = pd.DataFrame.from_records(querry_result.values())
MaxT = graph_data['MaxT'].to_numpy()
Humidity = graph_data['Humidity'].to_numpy()

app = DjangoDash('Dynamic', external_stylesheets=external_stylesheets)
app.layout = html.Div([
    html.H5('Dynamic Slider Graph'),
    dcc.Graph(id='slider-graph', animate=True, style={"backgroundColor": "#1a2d46", 'color': '#ffffff'}),
    dcc.Slider(
        id='input_graph',
        value=[MaxT,Humidity],
        step=1,
        updatemode='drag',
    ),
])


@app.callback(
               Output('slider-graph', 'figure'),
              [
                Input('input_graph', 'value'),
              ]
            )
def display_value(value):
    value_x = value[0]
    value_y = value[1]
    data = go.Scatter( x = value_x, y = value_y, name = 'MaxT', 
                         mode="markers", opacity=0.8 )
    
    plot_title = "MaxT" + " vs. " + "Humidity"
    
    layout = dict(title = plot_title, 
                  xaxis=dict(title = 'MaxT', ticklen=5, zeroline= False),
                  yaxis=dict(title = 'Humidity', side='left'),                                  
                  legend=dict(orientation="h", x=0.4, y=1.0),
                  autosize=False, width=750, height=500,
                 )

    return {'data': [data], 'layout': layout}
