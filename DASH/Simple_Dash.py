import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

# Load data
df = pd.read_csv("historical_stock_data.csv")

# Clean columns
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
    .str.replace("(", "")
    .str.replace(")", "")
)

df = df.rename(columns={'turnover_₹_cr': 'turnover'})
df['date'] = pd.to_datetime(df['date'])

# App
app = Dash(__name__)

app.layout = html.Div([
    html.H3("Stock Asset Line Chart"),

    dcc.Dropdown(
        options=[{'label': s, 'value': s} for s in df['symbol'].unique()],
        id='symbol',
        value=df['symbol'].unique()[0]
    ),

    dcc.Graph(id='line-chart')
])

@app.callback(
    Output('line-chart', 'figure'),
    Input('symbol', 'value')
)
def update_chart(symbol):
    dff = df[df['symbol'] == symbol]

    fig = px.line(dff, x='date', y='close', title=f"{symbol} Price")

    return fig

if __name__ == '__main__':
    app.run(debug=True)