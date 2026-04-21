import pandas as pd
import numpy as np
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output

# =========================
# LOAD & CLEAN DATA
# =========================
df = pd.read_csv("historical_stock_data.csv")

# Clean column names
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
    .str.replace("(", "")
    .str.replace(")", "")
)

# Rename problematic column
if 'turnover_₹_cr' in df.columns:
    df = df.rename(columns={'turnover_₹_cr': 'turnover'})

# Convert date
df['date'] = pd.to_datetime(df['date'])

# Sort data
df = df.sort_values(by='date')


# =========================
# KPI FUNCTIONS
# =========================
def calculate_kpis(dff):
    returns = dff['close'].pct_change().dropna()

    total_return = (dff['close'].iloc[-1] / dff['close'].iloc[0] - 1) * 100

    volatility = returns.std() * np.sqrt(252) * 100

    sharpe = (returns.mean() / returns.std()) * np.sqrt(252) if returns.std() != 0 else 0

    cumulative = (1 + returns).cumprod()
    peak = cumulative.cummax()
    drawdown = (cumulative - peak) / peak
    max_dd = drawdown.min() * 100

    return round(total_return, 2), round(volatility, 2), round(sharpe, 2), round(max_dd, 2)


# DASH APP
app = Dash(__name__)

app.layout = html.Div([

    html.H2("MULTI ASSET TRADING DASHBOARD"),

    # Dropdown
    dcc.Dropdown(
        options=[{'label': s, 'value': s} for s in df['symbol'].unique()],
        id='symbol',
        placeholder="Select Stock"
    ),

    # KPI Section
    html.Div([
        html.Div(id='return', style={'width': '25%', 'display': 'inline-block'}),
        html.Div(id='volatility', style={'width': '25%', 'display': 'inline-block'}),
        html.Div(id='sharpe', style={'width': '25%', 'display': 'inline-block'}),
        html.Div(id='drawdown', style={'width': '25%', 'display': 'inline-block'}),
    ]),

    # Chart
    dcc.Graph(id='chart')

])


# =========================
# CALLBACK
# =========================
@app.callback(
    [Output('chart', 'figure'),
     Output('return', 'children'),
     Output('volatility', 'children'),
     Output('sharpe', 'children'),
     Output('drawdown', 'children')],
    Input('symbol', 'value')
)
def update_dashboard(symbol):
    if symbol is None:
        return go.Figure(), "", "", "", ""

    dff = df[df['symbol'] == symbol]

    # KPIs
    total_return, volatility, sharpe, max_dd = calculate_kpis(dff)

    # Moving Average
    dff['ema20'] = dff['close'].ewm(span=20).mean()

    # Chart
    fig = go.Figure()

    fig.add_trace(go.Candlestick(
        x=dff['date'],
        open=dff['open'],
        high=dff['high'],
        low=dff['low'],
        close=dff['close'],
        name='Price'
    ))

    # fig.add_trace(go.Scatter(
    #     x=dff['date'],
    #     y=dff['ema20'],
    #     mode='lines',
    #     name='EMA 20'
    # ))

    fig.update_layout(title=f"{symbol} Price Chart", height=600)

    return (
        fig,
        f"Return: {total_return}%",
        f"Volatility: {volatility}%",
        f"Sharpe: {sharpe}",
        f"Max Drawdown: {max_dd}%"
    )


# =========================
# RUN APP
# =========================
if __name__ == '__main__':
    app.run(debug=True)