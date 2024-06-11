from dash import Dash, html, dash_table
import pandas as pd
import dash_bootstrap_components as dbc
import dash

df = pd.read_csv('data/train.csv')
df_help = pd.read_csv('data/002.csv')
dash.register_page(__name__ ,path='/footballd')

layout = dbc.Container(children=[
    
    html.H1('Football Dataset'),
    dash_table.DataTable(data=df.to_dict('records'), page_size=10,
    style_table={'height': '350px', 'overflowY': 'auto'},
    style_data={
        'color': 'black',
        'backgroundColor': 'white'
    },
    style_data_conditional=[
        {
            'if': {'row_index': 'odd'},
            'backgroundColor': 'rgb(220, 220, 220)',
        }
    ],
    style_header={
        'backgroundColor': 'rgb(210, 210, 210)',
        'color': 'black',
        'fontWeight': 'bold'
    }
),
    html.H1('Dataset Information'),
    dash_table.DataTable(data=df_help.to_dict('records'), page_size=12,
    style_data={
        'whiteSpace': 'normal',
        'height': 'auto',
        'lineHeight': '15px',
        'color': 'black',
        'backgroundColor': 'white'
    },      
    style_header={
        'backgroundColor': 'rgb(210, 210, 210)',
        'color': 'black',
        'fontWeight': 'bold'
    },
        style_data_conditional=[
        {
            'if': {'row_index': 'odd'},
            'backgroundColor': 'rgb(220, 220, 220)',
        }
    ],            
                         ),],
    fluid=True,
    

)

