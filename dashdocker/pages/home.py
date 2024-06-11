import dash
from dash import html
import dash_bootstrap_components as dbc


dash.register_page(__name__, path='/')

layout = card_content = [
        dbc.CardHeader('Welcome to my Website'),

        dbc.CardBody(
            [
                html.H5('ML Course', className = "card-title"),
                html.Br(),
                html.P('Exercise ML Course'),
                html.Br(),
                dbc.Button(
                    "Github",href='https://github.com/Meysamy71', id="example-button",color="success", className="me-2"
                ),
                dbc.Button(
                    "Linkedin", href='https://www.linkedin.com/in/meysam-yavarikhoo-aaa906212/',id="example-button",color="success", className="me-2"
                )


                ]

            )  
        ]
