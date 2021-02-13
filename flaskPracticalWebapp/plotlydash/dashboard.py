import dash
import dash_html_components as html
from flaskPracticalWebapp.plotlydash import content_layout as cl
from flaskPracticalWebapp.models import Practical
from flask_login import current_user
def create_dashboard(server):
    dash_app = dash.Dash(__name__,
        server=server,
        routes_pathname_prefix='/dashapp/')

    practicals = Practical.query.all()

    dash_app.layout = html.Div(cl.base_layout(content=[cl.list_practical(practical) for practical in practicals],
                                            title='Dashboard'))
    return dash_app.server
