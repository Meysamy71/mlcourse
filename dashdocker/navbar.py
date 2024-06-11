from dash import html
import dash_bootstrap_components as dbc


def create_navbar():
    navbar = dbc.NavbarSimple(
        children=[
            dbc.NavItem(
                dbc.NavLink(
                    [
                        html.I(className="fa-brands fa-github"),  # Font Awesome Icon
                        " Github"  # Text beside icon
                    ],
                    href="https://github.com/Meysamy71",
                    target="_blank"
                )

            ),
            dbc.NavItem(
                dbc.NavLink(
                    [
                        html.I(className="fa-brands fa-linkedin"),  # Font Awesome Icon
                        " Linkedin"  # Text beside icon
                    ],
                    href="https://www.linkedin.com/in/meysam-yavarikhoo-aaa906212/",
                    target="_blank"
                )
 
            ),
            dbc.NavItem(
                dbc.NavLink(
                    [
                        html.I(className="fa-solid fa-envelope"),  # Font Awesome Icon
                        " Email"  # Text beside icon
                    ],
                    href="m.yavarikhoo@gmail.com",
                    target="_blank"
                )
 
            ),

        ],
        brand='Home',
        brand_href="/",
        # sticky="top",  # Uncomment if you want the navbar to always appear at the top on scroll.
        color="dark",  # Change this to change color of the navbar e.g. "primary", "secondary" etc.
        dark=True,  # Change this to change color of text within the navbar (False for dark text)
        links_left=True,
        fluid=True,
        style={'padding-left': '10px'},
    )

    return navbar
