import dash
import dash_html_components as html

from flaskPracticalWebapp.plotlydash import content_layout as cl
from flaskPracticalWebapp.models import Practical
from flask_login import current_user
def create_dashboard(server):
    dash_app = dash.Dash(__name__,
        server=server,
        routes_pathname_prefix='/dashapp/')
    page = 3
    practicals = Practical.query.filter_by(default=True).all()
    
    dash_app.layout = html.Div(cl.base_layout(title='Dashboard', content=cl.list_practical(practicals[0])))
    return dash_app.server
