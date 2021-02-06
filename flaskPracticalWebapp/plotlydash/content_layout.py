import dash
import dash_html_components as html
from flask import url_for

# def base_layout():
#

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
