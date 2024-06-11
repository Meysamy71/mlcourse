from dash import Dash, html, dcc, callback, Output, Input
import dash
import pandas as pd
import plotly.express as px
from mplsoccer.pitch import Pitch
import matplotlib.pyplot as plt
import base64
from io import BytesIO
import dash_bootstrap_components as dbc
import numpy as np

dash.register_page(__name__, path='/football')

df = pd.read_csv('data/train.csv')
Top5Goal = df[df["outcome"] == "گُل"].playerId.value_counts().head()

def myfig():
    pitch = Pitch(pitch_color='grass', line_color='white', stripe=True)
    fig, ax = pitch.draw()
    m1 = ax.set_title('Total Players In DataSet', fontsize = 25, pad = 20)
    m2 = ax.text(60,20,"Total Players:\n " + str(df.playerId.nunique()),ha='center', va='center', fontsize=34)
    buf = BytesIO()
    fig.savefig(buf, format="png")
    fig_data = base64.b64encode(buf.getbuffer()).decode("ascii")
    fig_bar_matplotlib = f'data:image/png;base64,{fig_data}'
    return fig_bar_matplotlib

def myfig1():
    pitch = Pitch(pitch_color='grass', line_color='white', stripe=True)
    fig, ax = pitch.draw()
    ax.set_title('Most Goals Scored', fontsize = 25, pad = 20)
    ax.text(60,15,"Player ID: " + Top5Goal.index[0] + "\nTotal Goals: " + str(Top5Goal.iloc[0]) ,ha='center', va='center', fontsize=34)
    buf = BytesIO()
    fig.savefig(buf, format="png")
    # Embed the result in the html output.
    fig_data = base64.b64encode(buf.getbuffer()).decode("ascii")
    fig_bar_matplotlib = f'data:image/png;base64,{fig_data}'
    return fig_bar_matplotlib

def myfig2():
    fig = px.bar(Top5Goal, title="Top 5 Players Goals", labels={"value": "Goals Count","variable": "Goals"},height=480,width=640)
    fig.update_layout(title_x=0.5,font=dict(
        size=18,
    ))
    return fig

def myfig3():
    Palyer18 = df[(df["playerId"] == "p_18")]
    fig = px.scatter(Palyer18, Palyer18.x, Palyer18.y, color='outcome',title="Player P_18", symbol="outcome")
    fig.update_layout(title={'y':0.9,'x':0.5,'xanchor': 'center','yanchor': 'top'})
    fig.update_traces(marker_size=10)
    return fig

def myfig4():
    Palyerp_147 = df[(df["playerId"] == "p_147")]
    fig = px.scatter(Palyerp_147, Palyerp_147.x, Palyerp_147.y, color='outcome', symbol='outcome',title="Player P_147")
    fig.update_layout(title={'y':0.9,'x':0.5,'xanchor': 'center','yanchor': 'top'})
    fig.update_traces(marker_size=10)
    return fig

def myfig5():
    dist = df['dist'] = np.sqrt(df['x']**2 + df['y']**2)
    pitch = Pitch(pitch_color='grass', line_color='white', stripe=True)
    fig, ax = pitch.draw()
    m1 = ax.set_title('Max Distance Shoots', fontsize = 25, pad = 20)
    m2 = ax.text(60,20,"Max Distance Shoot:\n " + str(dist.max().round(2)),ha='center', va='center', fontsize=34)
    buf = BytesIO()
    fig.savefig(buf, format="png")
    fig_data = base64.b64encode(buf.getbuffer()).decode("ascii")
    fig_bar_matplotlib = f'data:image/png;base64,{fig_data}'
    return fig_bar_matplotlib



layout = dbc.Container(children=[html.Div([
    html.H1('Section 2 Exercise 2'),
    html.Hr(),
    html.H3('Football Data Analyst'),
    dbc.Button("Check DataSet", color="warning", className="me-1", href='/footballd'),
    html.Hr(),
    html.H3('1- How many players are there in the dataset?', style={'color' : 'brown'}),
    html.Hr(),
    html.Img(src=myfig(),alt='Total Player'),
    html.Hr(),]),
    html.Div([
    html.H3('2- Which player scored the most goals?', style={'color' : 'brown'}),
    html.Hr(),
    html.Img(src=myfig1(),alt='Player Most Golas',style={'height':'480px','width':'640px'}),
    dcc.Graph(figure=myfig2(),style={'float':'right'}),
    html.Hr()]),
    html.Div([
    html.H3('3- Which players had the highest and lowest conversion rate of shots into goals, respectively?', style={'color' : 'brown'}),
    html.Hr(),
    dcc.Graph(figure=myfig3(),style={'float':'left'}),
    dcc.Graph(figure=myfig4(),style={'float':'right'}),
    html.Div(style={'clear':'both'}),
    html.Hr()]),
    html.Div([
    html.H3('4- What was the Euclidean distance of the farthest shot to the center of the goal?', style={'color' : 'brown'}),
    html.Hr(),
    html.Img(src=myfig5()),
    html.Hr()]),
],fluid=True,)
