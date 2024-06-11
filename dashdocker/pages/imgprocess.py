from dash import Dash, html, dcc, callback, Output, Input
import dash
import plotly.express as px
import matplotlib.pyplot as plt
import dash_bootstrap_components as dbc
import numpy as np
from PIL import Image
from dash_canvas import DashCanvas

dash.register_page(__name__, path='/imgprocess')

num0= Image.open('assets/mask/num0.jpg')
num0_hist= Image.open('assets/img/0.jpg')
num1 = Image.open('assets/mask/num1.jpg')
num1_hist= Image.open('assets/img/1.jpg')
num2= Image.open('assets/mask/num2.jpg')
num2_hist= Image.open('assets/img/2.jpg')
num3= Image.open('assets/mask/num3.jpg')
num3_hist= Image.open('assets/img/3.jpg')
num4= Image.open('assets/mask/num4.jpg')
num4_hist= Image.open('assets/img/4.jpg')
num5= Image.open('assets/mask/num5.jpg')
num5_hist= Image.open('assets/img/5.jpg')
num6= Image.open('assets/mask/num6.jpg')
num6_hist= Image.open('assets/img/6.jpg')
num7= Image.open('assets/mask/num7.jpg')
num7_hist= Image.open('assets/img/7.jpg')
num8= Image.open('assets/mask/num8.jpg')
num8_hist= Image.open('assets/img/8.jpg')
num9= Image.open('assets/mask/num9.jpg')
num9_hist= Image.open('assets/img/9.jpg')

fileimg = Image.open('assets/img.jpg')
fileimg = fileimg.rotate(90)
fileimg = fileimg.resize((680,420))

fileimggray = Image.open('assets/imggray.jpg')
fileimggray = fileimggray.resize((680,420))

fig = px.imshow(fileimggray)
fig.update_layout(dragmode="drawrect")
config = {
    "modeBarButtonsToAdd": [
        "drawline",
        "drawopenpath",
        "drawclosedpath",
        "drawcircle",
        "drawrect",
        "eraseshape",
    ]
}

fileimgmask = Image.open('assets/imgmask.jpg')
fileimgmask = fileimgmask.resize((680,420))

fig1 = px.imshow(fileimgmask, binary_string=True)
fig1.update_layout(dragmode="drawrect")



layout = dbc.Container(children=[html.Div([
    html.H1('Image Processing'),
    html.Hr(),
    html.H3('Original image'),
    html.Hr(),
    DashCanvas(id='canvaas_image',
               tool='line',
               lineWidth=5,
               lineColor='red',
               filename=fileimg,
               width=680),
    html.Hr(),]),
    html.Div([
    html.H3('Gray Image'),
    html.Hr(),
    dcc.Graph(figure=fig, config=config),
    html.Hr()]),
    html.Div([
    html.H3('Mask Image'),
    html.Hr(),
    dcc.Graph(figure=fig1),
    html.Hr()]),
    html.Div([
    html.H3('HeatMap Image'),
    html.Hr(),
    html.Img(src=num0),
    html.Img(src=num0_hist),
    html.Hr()]),
    html.Div([
    html.Hr(),
    html.Img(src=num1),
    html.Img(src=num1_hist),
    html.Hr()]),
    html.Div([
    html.Hr(),
    html.Img(src=num2),
    html.Img(src=num2_hist),
    html.Hr()]),
    html.Div([
    html.Hr(),
    html.Img(src=num3),
    html.Img(src=num3_hist),
    html.Hr()]),
    html.Div([
    html.Hr(),
    html.Img(src=num4),
    html.Img(src=num4_hist),
    html.Hr()]),
    html.Div([
    html.Hr(),
    html.Img(src=num5),
    html.Img(src=num5_hist),
    html.Hr()]),
    html.Div([
    html.Hr(),
    html.Img(src=num6),
    html.Img(src=num6_hist),
    html.Hr()]),
    html.Div([
    html.Hr(),
    html.Img(src=num7),
    html.Img(src=num7_hist),
    html.Hr()]),
    html.Div([
    html.Hr(),
    html.Img(src=num8),
    html.Img(src=num8_hist),
    html.Hr()]),
    html.Div([
    html.Hr(),
    html.Img(src=num9),
    html.Img(src=num9_hist),
    html.Hr()]),
    ])
