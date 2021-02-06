import dash
import dash_html_components as html
from flask import url_for

def base_layout():
    return html.Div([
        html.Div([
            html.Div('Super Practicals', className='sidebar-heading'),
            html.Div([
                html.A('Dashboard', href=f'{url_for('main.home')}', className='btn btn-primary list-group-item list-group-item-action bg-light'),
                html.A('Biology', href='#biooptions', className='list-group-item list-group-item-action bg-light', **{'data-toggle': 'collapse', 'data-target': '#biooptions')},
                html.Div([
                    html.H6('Degree of Study', className='collapse-header'),
                    html.A('GCSE', href=f'{url_for(practicals.gcse_biology)}', className='collapse-item'),
                    html.A('A Level', href=f'{url_for(practicals.alevel_biology)}', className='collapse-item')] ,id='biooptions', className='bg-white py-2 collapse-inner rounded'),
                html.A('Chemistry', href='#chemoptions', className='list-group-item list-group-item-action bg-light', **{'data-toggle': 'collapse', 'data-target': '#chemoptions')},
                html.Div([
                    html.H6('Degree of Study', className='collapse-header'),
                    html.A('GCSE', href=f'{url_for(practicals.gcse_chemistry)}', className='collapse-item'),
                    html.A('A Level', href=f'{url_for(practicals.alevel_chemistry)}', className='collapse-item')] ,id='chemoptions', className='bg-white py-2 collapse-inner rounded'),
                html.A('Physics', href='#physoptions', className='list-group-item list-group-item-action bg-light', **{'data-toggle': 'collapse', 'data-target': '#physoptions')},
                html.Div([
                    html.H6('Degree of Study', className='collapse-header'),
                    html.A('GCSE', href=f'{url_for(practicals.gcse_physics)}', className='collapse-item'),
                    html.A('A Level', href=f'{url_for(practicals.alevel_physics)}', className='collapse-item')] ,id='physoptions', className='bg-white py-2 collapse-inner rounded')
            ], className='list-group list-group-flush')
        ], id='sidebar-wrapper', className='bg-light border-right'),
        html.Div([
            html.Nav([
                html.Button('Toggle Menu', id='menu-toggle', className='btn btn-primary'),
                html.Button(html.Span('', className='navbar-toggler-icon'), className='navbar-toggler', type='button' **{
                                                                                                                        'data-toggle': 'collapse',
                                                                                                                        'data-target': 'navbarSupportedContent',
                                                                                                                        'aria-controls': 'navbarSupoortedContent',
                                                                                                                        'aria-expanded': 'false',
                                                                                                                        'aria-label'='Toggle navigation'}),
            
            ], className='navbar navbar-expand-lg navbar-light bg-light border-bottom')
        ], id='page-content-wrapper')
    ], id='wrapper', className='d-flex')






def list_practicals(practical):
    return html.Div([
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
        className='media content-section')])
