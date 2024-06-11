import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from navbar import create_navbar
from sidebar import create_sidebar


SIDEBAR = create_sidebar()
NAVBAR = create_navbar()
FA621 = "https://use.fontawesome.com/releases/v6.2.1/css/all.css"
APP_TITLE = "ML Course"


app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True,
    external_stylesheets=[
        dbc.themes.CERULEAN,
        FA621, 
    ],
    title=APP_TITLE,
    use_pages=True,
)

app.layout = [dcc.Loading( 
    id='loading_page_content',
    children=[
        html.Div(
            [
                NAVBAR,
                
            ]
        ),
        html.Div([SIDEBAR,]),
        
    ],
    color='primary',
    fullscreen=True,
    
),
html.Div(dash.page_container,style={
  'width': 'auto',
  'height': 'auto',
  'padding': '10px',
  'margin-left': '240px',
},)]
server = app.server

if __name__ == '__main__':
    app.run_server(host='0.0.0.0',port='8080')
