from dash import Dash, html, dcc

app = Dash(__name__)

app.layout = html.Div([
    html.H1('Dash App'),
    dcc.Graph(id='graph')
])

if __name__ == '__main__':
    app.run(debug=True)