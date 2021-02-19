import dash
from dash.dependencies import Input, Output
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
def practical_view(server):
    dash_app_practical= dash.Dash(__name__, server=server, routes_pathname_prefix='/dashapp/practical/')
    params = [f'Trial {x+1}' for x in range(3)]
    intervals = ['10', '20', '30', '40', '50']

    dash_app_practical.layout = html.Div([
        html.Label('Independent Variable'),
         dcc.Input(id='independent_variable',
                placeholder='Independent Variable',
                value=''
        ),

        html.Label('Dependent Variable'),
        dcc.Input(
            id='dependent_variable',
            placeholder='Dependent Variable',
            value=''
        ),

        dash_table.DataTable(
            id='table-editing-simple',
            columns=(
                [{'id': 'DV', 'name': 'DV'}] +
                [{'id': p, 'name': p} for p in params]
            ),
            data=[
                dict(DV=interval, **{param: 0 for param in params})
                for interval in intervals
            ],
            editable=True
        ),
        html.Button('Mark Anomalous', id='anomalous-button', n_clicks=0),
        dcc.Graph(id='table-editing-simple-output')
    ])

    @dash_app_practical.callback(
        Output('table-editing-simple', 'columns'),
        Input('table-editing-simple', 'columns'),
        Input('dependent_variable', 'value'))
    def display_DV_in_table(columns, dv='Dependent Variable'):
        columns[0]['id'] = columns[0]['name'] = dv
        return columns

    @dash_app_practical.callback(
        Output('table-editing-simple-output', 'figure'),
        Input('table-editing-simple', 'data'),
        Input('table-editing-simple', 'columns'))
    def display_output(rows, columns):
        df = pd.DataFrame(rows, columns=[c['name'] for c in columns])
        return {
            'data': [{
                'type': 'line',
                'x': intervals,
                'y': [row['Trial 1'] for row in rows]
                }]
        }
    # @dash_app_practical.callback(
    #     Output('table-editing-simple', 'selected_cells'),
    #     Input('anomalous-button', 'n_clicks'),
    #     Input('table-editing-simple', 'selected_cells'))
    # def mark_anomalous(anomalous_button, anomalous_cells):
    #     print(anomalous_cells)

    return dash_app_practical.server


