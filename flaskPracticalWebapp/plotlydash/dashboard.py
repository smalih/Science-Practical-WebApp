import dash
import dash_html_components as html
from flaskPracticalWebapp.plotlydash import content_layout as cl
from flaskPracticalWebapp.models import Practical
from flask_login import current_user
def create_dashboard(server):
    dash_app = dash.Dash(
        server=server,
        routes_pathname_prefix='/dashapp/',
        external_stylesheets=['\static\css\\bootstrap.min.css']
    )

    practicals = Practical.query.all()

    dash_app.layout = html.Div([cl.list_practicals(practical) for practical in practicals])

    return dash_app.server
