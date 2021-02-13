import dash
import dash_html_components as html
from flask import url_for
from flask_login import current_user

### Dash Application Mode ###


def practical_page(practical):
    pass

def edit_practical(practical):
    pass



























def base_layout(title, content):
    display_in_user =  'INSERT PROFILE PIC'
    authenticated_html = html.Div([
                            html.Li(html.A('Login', className='nav-link', href=f"{url_for('users.login')}"), className='nav-item'),
                            html.Li(html.A('Register', className='nav-link', href=f"{url_for('users.register')}"), className='nav-item')])
    if current_user:
        if current_user.fname and current_user.surname:
            display_in_user = f'{current_user.fname} {current_user.surname}'
        if current_user.is_authenticated:
            authenticated_html = html.Div([
                                    html.Li(html.A('Favoruties', href='#', className='nav-link'), className='nav-item'),
                                    # Utilise Dash components for dropdown items
                                    html.Li([
                                        html.A(display_in_user, href='#', className='nav-link dropdown-toggle', role='button', **{'data-toggle': 'dropdown',
                                                                                                                                'aria-haspopup': 'true',
                                                                                                                                'aria-expanded': 'false'}),
                                        html.Div([
                                            html.A('Account', className='dropdown-item', href=f"{url_for('users.profile')}"),
                                            html.A('Settings', className='dropdown-item', href=f"{url_for('users.settingd')}"),
                                            html.Div(className='dropdown-divider'),
                                            html.A('Logout', className='dropdown-item', href=f"{url_for('users.logout')}")],
                                        className='dropdown-menu  dropdown-menu-right', **{'aria-labelledby': 'navbarDropdown'})],
                                    className='nav-item dropdown')])
    return html.Div([
        html.Div([
            html.Div('Super Practicals', className='sidebar-heading'),
            html.Div([
                html.A('Dashboard', href=f"{url_for('main.home')}", className='btn btn-primary list-group-item list-group-item-action bg-light'),
                html.A('Biology', href='#biooptions', className='list-group-item list-group-item-action bg-light', **{'data-toggle': 'collapse', 'data-target': '#biooptions'}),
                html.Div([
                    html.H6('Degree of Study', className='collapse-header'),
                    html.A('GCSE', href=f"{url_for('practicals.gcse_biology')}", className='collapse-item'),
                    html.A('A Level', href=f"{url_for('practicals.alevel_biology')}", className='collapse-item')] ,id='biooptions', className='bg-white py-2 collapse-inner rounded'),
                html.A('Chemistry', href='#chemoptions', className='list-group-item list-group-item-action bg-light', **{'data-toggle': 'collapse', 'data-target': '#chemoptions'}),
                html.Div([
                    html.H6('Degree of Study', className='collapse-header'),
                    html.A('GCSE', href=f"{url_for('practicals.gcse_chemistry')}", className='collapse-item'),
                    html.A('A Level', href=f"{url_for('practicals.alevel_chemistry')}", className='collapse-item')] ,id='chemoptions', className='bg-white py-2 collapse-inner rounded'),
                html.A('Physics', href='#physoptions', className='list-group-item list-group-item-action bg-light', **{'data-toggle': 'collapse', 'data-target': '#physoptions'}),
                html.Div([
                    html.H6('Degree of Study', className='collapse-header'),
                    html.A('GCSE', href=f"{url_for('practicals.gcse_physics')}", className='collapse-item'),
                    html.A('A Level', href=f"{url_for('practicals.alevel_physics')}", className='collapse-item')] ,id='physoptions', className='bg-white py-2 collapse-inner rounded')
            ], className='list-group list-group-flush')
        ], id='sidebar-wrapper', className='bg-light border-right'),
        html.Div([
            html.Nav([
                html.Button('Toggle Menu', id='menu-toggle', className='btn btn-primary'),
                html.Button(html.Span(className='navbar-toggler-icon'), className='navbar-toggler', type='button', **{
                                                                                                                        'data-toggle': 'collapse',
                                                                                                                        'data-target': 'navbarSupportedContent',
                                                                                                                        'aria-controls': 'navbarSupportedContent',
                                                                                                                        'aria-expanded': 'false',
                                                                                                                        'aria-label': 'Toggle navigation'}),
                html.Div([
                    html.Ul([
                        html.Li(
                            html.A(['Dashboard', html.Span('(current)', className='sr-only')], className='nav-link', href=f"{url_for('main.home')}"),
                        className='nav-item active'),
                        authenticated_html],
                    className='navbar-nav ml-auto mt-2 mt-lg-0')],
                id='navbarSupportedContent', className='collapse navbar-collapse')],
            className='navbar navbar-expand-lg navbar-light bg-light border-bottom'),
            html.Div([
                html.H2(f'{title}', className='mt-4'),
                content], className='container-fluid')],
        id='page-content-wrapper')],
    id='wrapper', className='d-flex')



def list_practical(practical):

    return html.Div(
            html.Article([
                html.Div([
                    html.Div(
                        html.A(f'{practical.author.fname} {practical.author.surname}', href='#', className='mr-2'),
                    className='article-metadata'),
                    html.H2(html.A(f'{practical.title}', href=f"{url_for('practicals.practical', practical_id=practical.id, practical_title=practical.title)}", className='article-title')),
                    html.P(html.Small(f'Degree of Study: {practical.degStudy}')),
                    html.P(html.Small(f'Subject: {practical.subject}')),
                    html.P(f'{practical.method}', className='article-content')],
                className='media-body')],
            className='media content-section'))

