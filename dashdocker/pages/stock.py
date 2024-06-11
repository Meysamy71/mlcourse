from dash import Dash, html, dcc, Input, Output, callback
import plotly.express as px
import dash

df = px.data.stocks()

dash.register_page(__name__ ,path='/stock')

layout = html.Div(children=[
    html.H1('Stock Dataset'),
    html.Hr(),
    html.H3('Stock'),
    dcc.Dropdown(df.columns[1:], value=df.columns[1], id='input', multi=True),
    html.Br(),
    dcc.Graph(id='output_chart')
])


@callback(Output('output_chart', 'figure'),
              Input('input', 'value'))

def update_chart(x):
    fig = px.line(df, x='date', y=x)
    return fig
