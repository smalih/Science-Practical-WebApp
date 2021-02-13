import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
import dash_table
import pandas as pd
app = dash.Dash(__name__)

intervals = ['10', '20', '30', '40', '50']

trials = ['5', '6', '8', '7']

app.layout = html.Div([dash_table.DataTable(
        id='results-table',
        columns=(
            [{'id': 'DV', 'name': 'DV'}] +
            [{'id': f'Trial {x+1}', 'name': f'Trial {x+1}'} for x in range(len(trials))]
        ),
        data=[
            dict(DV=interval, **{trial: 0 for trial in trials })
            for interval in intervals
        ],
        editable=True
    ),
    dcc.Graph(id='test-graph')
])
    
@app.callback(
    Output('test-graph', 'figure'),
    Input('results-table', 'data'),
    Input('results-table', 'columns'))
def display_output(rows, columns):
    df = pd.DataFrame(rows, columns=[c['name'] for c in columns[1:]])
    return {
        'data': [{
            'type': 'line',
            'x': intervals,
            'y': df[columns[1]['id']]
        }]
    }


if __name__ == '__main__':
    app.run_server(debug=True)