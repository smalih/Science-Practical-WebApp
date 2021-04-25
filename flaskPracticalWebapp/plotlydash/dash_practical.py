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
            id='results-table',
            columns=(
                [{'id': 'DV', 'name': 'DV'}] +
                [{'id': p, 'name': p} for p in params]
            ),
            data=[
                dict(DV=interval, **{param: 0 for param in params}, type='numeric')
                for interval in intervals
            ],
            editable=True
        ),
        html.Button('Mark Anomalous', id='anomalous-button', n_clicks=0),
        dcc.Graph(id='results-table-output')
    ])

    @dash_app_practical.callback(
        Output('results-table', 'columns'),
        Input('results-table', 'columns'),
        Input('independent_variable', 'value'))
    def display_IV_in_table(columns, iv='Independent Variable'):
        columns[0]['id'] = columns[0]['name'] = iv
        return columns
        
    # Write function to display the DV in the table
    # @dash_app_practical.callback(
    #     Output('results-table', 'rows'),
    #     Input('results-table', 'rows'),
    #     Input('dependent_variable', 'value'))
    # def display_DV_in_table(rows, dv='Dependent Variable'):
    #     rows[0]['id'] = rows[0]['name'] = dv
    #     return rows

    @dash_app_practical.callback(
        Output('results-table-output', 'figure'),
        Input('results-table', 'data'),
        Input('results-table', 'columns'))
    def display_output(rows, columns):
        df = pd.DataFrame(rows, columns=[c['name'] for c in columns])
        return {
            'data': [{
                'type': 'line',
                'x': intervals,
                # need to find a way to convert values into int implicitly
                # why are they of type str to begin with?
                'y': [(int(row['Trial 1']) + int(row['Trial 2']) + int(row['Trial 3']))/3 for row in rows]
                }]
        }
    # @dash_app_practical.callback(
    #     Output('results-table', 'selected_cells'),
    #     Input('anomalous-button', 'n_clicks'),
    #     Input('results-table', 'selected_cells'))
    # def mark_anomalous(anomalous_button, anomalous_cells):
    #     print(anomalous_cells)

    return dash_app_practical.server


