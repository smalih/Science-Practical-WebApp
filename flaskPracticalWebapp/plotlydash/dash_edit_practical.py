import dash
from dash.dependencies import Input, Output
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

app = dash.Dash(__name__)

params = [f'Trial {x+1}' for x in range(3)]
intervals = ['10', '20', '30', '40', '50']

app.layout = html.Div([
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
    dcc.Graph(id='table-editing-simple-output')
])


@app.callback(
    Output('table-editing-simple-output', 'figure'),
    Input('table-editing-simple', 'data'),
    Input('table-editing-simple', 'columns'))
def display_output(rows, columns):
    print(rows)
    df = pd.DataFrame(rows, columns=[c['name'] for c in columns])
    return {
        'data': [{
            'type': 'line',
            'x': intervals,
            'y': [row['Trial 1'] for row in rows]
            }]
    }


if __name__ == '__main__':
    app.run_server(debug=True)

