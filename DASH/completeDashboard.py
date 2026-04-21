import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from dash import Dash, dcc, html, Input, Output
from config import Cfg

# Load and Clean the Data
df = pd.read_csv(Cfg["DATA_PATH"])

df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
    .str.replace("(", "")
    .str.replace(")", "")
)

if 'turnover_₹_cr' in df.columns:
    df = df.rename(columns={'turnover_₹_cr': 'turnover'})

df[Cfg["DATE_COLUMN"]] = pd.to_datetime(df[Cfg["DATE_COLUMN"]])
df = df.sort_values(by=Cfg["DATE_COLUMN"])



# calculating Kpis
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

def volatility_gauge(volatility):

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=volatility,
        title={'text': "Volatility"},
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': "black"},
            'steps': [
                {'range': [0, 20], 'color': "green"},
                {'range': [20, 40], 'color': "yellow"},
                {'range': [40, 100], 'color': "red"}
            ]
        }
    ))

    return fig




# Main dash app
app = Dash(__name__)

app.layout = html.Div([

    html.H2(Cfg["APP"]["title"]),

    dcc.Dropdown(
        options=[{'label': s, 'value': s} for s in df[Cfg["SYMBOL_COLUMN"]].unique()],
        id='symbol',
        placeholder="Select Stock"
    ),

    html.Div([
        html.Div(id='return', style={'width': '25%', 'display': 'inline-block'}),
        html.Div(id='volatility', style={'width': '25%', 'display': 'inline-block'}),
        html.Div(id='sharpe', style={'width': '25%', 'display': 'inline-block'}),
        html.Div(id='drawdown', style={'width': '25%', 'display': 'inline-block'}),
    ]),

    dcc.Graph(id='chart')

])



# callback
@app.callback(
    [Output('chart', 'figure'),
     Output('return', 'children'),
     Output('volatility', 'children'),
     Output('sharpe', 'children'),
     Output('drawdown', 'children')],
    Input('symbol', 'value'),
)
def update_dashboard(symbol):

    if symbol is None:
        return go.Figure(), "", "", "", ""

    dff = df[df[Cfg["SYMBOL_COLUMN"]] == symbol]

    # KPIs
    total_return, volatility, sharpe, max_dd = calculate_kpis(dff)


    # Chart
    fig = go.Figure()

    if Cfg["CHART_TYPE"] == "candlestick":
        fig.add_trace(go.Candlestick(
            x=dff['date'],
            open=dff['open'],
            high=dff['high'],
            low=dff['low'],
            close=dff['close'],
            name='Price'
        ))
    else:
        fig.add_trace(go.Scatter(
            x=dff['date'],
            y=dff['close'],
            mode='lines',
            name='Price'
        ))

    # Add Moving Averages
    for ma in Cfg["INDICATORS"]["moving_average"]:
        if ma in dff.columns:
            fig.add_trace(go.Scatter(
                x=dff['date'],
                y=dff[ma],
                mode='lines',
                name=ma.upper(),
                line=dict(width=3)
            ))


    fig.update_layout(
        title=f"{symbol} Price Chart",
        height=Cfg["APP"]["height"]
    )

    return (
        fig,
        f"Return: {total_return}%" if Cfg["KPIS"]["return"] else "",
        f"Volatility: {volatility}%" if Cfg["KPIS"]["volatility"] else "",
        f"Sharpe: {sharpe}" if Cfg["KPIS"]["sharpe"] else "",
        f"Max Drawdown: {max_dd}%" if Cfg["KPIS"]["drawdown"] else ""
    )


# =========================
# RUN APP
# =========================
if __name__ == '__main__':
    app.run(debug=Cfg["APP"]["debug"])