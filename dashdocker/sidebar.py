import dash_bootstrap_components as dbc
from dash import html

def create_sidebar():

    # the style arguments for the sidebar. We use position:fixed and a fixed width
    SIDEBAR_STYLE = {
        "position": "absolute",
        "top": 56,
        "left": 0,
        "bottom": 0,
        "width": "16rem",
        "padding": "2rem 1rem",
        "background-color": "dark",

    }
    # the styles for the main content position it to the right of the sidebar and
    # add some padding.
    CONTENT_STYLE = {
        "margin-left": "18rem",
        "margin-right": "2rem",
        "padding": "2rem 1rem",
    }
    sidebar = html.Div(
        [
            html.H3("ML Course"),
            html.Hr(),
            html.Img(src='../assets/userimg.jfif', style={'vertical-align': 'middle','width': '50px','height': '50px','border-radius': '50%','float':'left'}),
            html.H5(
                "Meysam Yavarikhoo", style={'padding-left': '60px'}),
            html.Hr(),
            dbc.Nav(
                [
                    dbc.NavLink("Home", href="/", active="exact"),
                    dbc.NavLink("Health", href="/health", active="exact"),
                    dbc.NavLink("Football", href="/football", active="exact"),
                    dbc.NavLink("Image Process", href="/imgprocess", active="exact"),
                    dbc.NavLink("Stock", href="/stock", active="exact"),
                ],
                vertical=True,
                pills=True,
            ),
        ],
        style=SIDEBAR_STYLE,
    )
    return sidebar
