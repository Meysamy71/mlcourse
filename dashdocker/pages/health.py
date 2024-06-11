from dash import Dash, html, dcc, callback, Output, Input
import dash
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import dash_bootstrap_components as dbc
import plotly.figure_factory as ff

dash.register_page(__name__, path='/health')

df = pd.read_csv('data/insurance.csv')
smoker1 = df[df['smoker'] == 'yes']
fig1 = px.histogram(smoker1, y='region',color='region').update_yaxes(categoryorder='total ascending')

north = df[(df['region'] == 'northwest') | ((df['region'] == 'northeast'))]
female = north[north['sex'] == 'female']
desc = female['charges'].describe()
df_desc = pd.DataFrame(desc)
fig2 = px.bar(df_desc[1:], y='charges').update_xaxes(categoryorder='mean ascending')

corr = df[['age','bmi','children','charges']]
fig3 = px.imshow(corr.corr().round(1), text_auto=True)

fig4 = ff.create_distplot([df['bmi']], ['bmi'])

fig5 = px.box(df, x=df['charges'])
fig6 = px.histogram(df, y=df['region'], color='smoker', orientation='h',color_discrete_sequence=['blue', 'red'],category_orders={'smoker': ["no",'yes']})

fig7 = px.scatter(df, x='age', y='charges', color='smoker',color_discrete_sequence=['red', 'blue'])

df_1 = df[df['children'] < 2]

fig8 = px.scatter(df_1, x='bmi', y='charges', color='smoker',color_discrete_sequence=['red', 'blue'])

layout = dbc.Container(children=[html.Div([
    html.H1('US Health Insurance Dataset'),
    html.Hr(),
    html.H3('US Health Insurance'),
    dbc.Button("Check DataSet", color="warning", className="me-1", href='/healthd'),
    html.Hr(),
    html.H3('1. Which region has the greatest number of smokers?', style={'color' : 'brown'}),
    html.Hr(),
    dcc.Graph(figure=fig1),
    html.Hr(),]),
    html.Div([
    html.H3('2. What are the average charges of a female living in the north?', style={'color' : 'brown'}),
    html.Hr(),
    dcc.Graph(figure=fig2)]),
    html.Hr(),
    html.Div([
    html.H3('3. Make a heatmap showing the correlation of all the numeric columns in the data', style={'color' : 'brown'}),
    html.Hr(),
    dcc.Graph(figure=fig3)]),
    html.Hr(),
    html.Div([
    html.H3('4. Distribution of BMI using Histogram', style={'color' : 'brown'}),
    html.Hr(),
    dcc.Graph(figure=fig4)]),
    html.Hr(),
    html.Div([
    html.H3('5. Make a boxplot of charges. Output the median value of charges', style={'color' : 'brown'}),
    html.Hr(),
    dcc.Graph(figure=fig5)]),
    html.Hr(),
    html.Div([
    html.H3('6. Make a horizontal bar chart of region vs smoker. Make the legend smaller', style={'color' : 'brown'}),
    html.Hr(),
    dcc.Graph(figure=fig6)]),
    html.Hr(),
    html.Div([
    html.H3('7. Make a scatterplot of age with charges and colorcode using the smoker values. Also provide the legends', style={'color' : 'brown'}),
    html.Hr(),
    dcc.Graph(figure=fig7)]),
    html.Hr(),
    html.Div([
    html.H3('8. Make a scatterplot of bmi with charges and colorcode using the smoker values.Add legends and use only data of people who have less than 2 children', style={'color' : 'brown'}),
    html.Hr(),
    dcc.Graph(figure=fig8)]),
],fluid=True,)
