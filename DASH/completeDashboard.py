import pandas as pd
import numpy as np
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output
from config import Cfg


# LOAD & CLEAN DATA
df = pd.read_csv(Cfg["DATA_PATH"])

df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
    .str.replace("(", "")
    .str.replace(")", "")
)

# if 'turnover_₹_cr' in df.columns:
#     df = df.rename(columns={'turnover_₹_cr': 'turnover'})

df[Cfg["DATE_COLUMN"]] = pd.to_datetime(df[Cfg["DATE_COLUMN"]])
df = df.sort_values(by=Cfg["DATE_COLUMN"])



# KPI FUNCTION
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


# GAUGE FUNCTION
def create_gauge(value, title, min_val=0, max_val=60):

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=value,
        title={'text': title},
        gauge={
            'axis': {'range': [min_val, max_val]},
            'bar': {'color': "black"},
            'steps': [
                {'range': [min_val, max_val*0.3], 'color': "green"},
                {'range': [max_val*0.3, max_val*0.6], 'color': "yellow"},
                {'range': [max_val*0.6, max_val], 'color': "red"}
            ]
        }
    ))

    fig.update_layout(height=200,margin=dict(l=10, r=10, t=40, b=10))

    return fig


# line chart
def mini_line_chart(dff):
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=dff['date'],
        y=dff['close'],
        mode='lines'
    ))

    fig.update_layout(
        height=120,
        margin=dict(l=5, r=5, t=5, b=5),
        xaxis_visible=False,
        yaxis_visible=False
    )
    return fig



def box_style():
    return {
        'Height': '25px',
        'width': '25%',
        'border': '2px solid black',
        'padding': '5px'
    }


def drawdown_chart(dff):

    returns = dff['close'].pct_change().fillna(0)

    cumulative = (1 + returns).cumprod()
    peak = cumulative.cummax()
    drawdown = (cumulative - peak) / peak

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=dff['date'],
        y=drawdown,
        fill='tozeroy',
        fillcolor='rgba(255,0,0,0.3)',
        mode='lines',
        name='Drawdown'
    ))

    fig.update_layout(
        title="Drawdown",
        height=400
    )

    return fig


def volume_bar_chart(dff):

    # Try to detect volume column safely
    volume_col = None
    for col in dff.columns:
        if "volume" in col :
            volume_col = col
            break

    if volume_col is None:
        return go.Figure()  # fallback if no column

    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=dff['date'],
        y=dff[volume_col],
        marker_color='rgba(0, 123, 255, 0.6)'  # soft blue
    ))

    fig.update_layout(
        title="Volume",
        height=200,   # 👈 NARROW HEIGHT (important)
        margin=dict(l=10, r=10, t=25, b=10),
        xaxis_title=None,
        yaxis_title=None,
        xaxis_showgrid=False,
        yaxis_showgrid=False
    )

    return fig

# DASH APP
app = Dash(__name__)

app.layout = html.Div([

    html.H2(Cfg["APP"]["title"]),

    dcc.Dropdown(
        options=[{'label': s, 'value': s} for s in df[Cfg["SYMBOL_COLUMN"]].unique()],
        id='symbol',
        placeholder="Select Stock"
    ),

    # KPI TEXT (Top Row)
    html.Div([
        html.Div(id='return', style={'width': '30%', 'display': 'inline-block'}),
        html.Div(id='sharpe', style={'width': '30%', 'display': 'inline-block'}),
        html.Div(id='drawdown', style={'width': '30%', 'display': 'inline-block'}),
    ]),


    #MAIN CHART
    dcc.Graph(id='chart'),

    #Volume Bar
    html.Div([
        dcc.Graph(id='volume_chart')
    ], style={
        'border': '2px solid black',
        'width': '100%',
        'height': '160px',
        'marginTop': '15px'

    }),


    # LOWER DASHBOARD (4 BOXES)
    html.Div([

        html.Div([dcc.Graph(id='volatility_gauge')], style=box_style()),

        html.Div([dcc.Graph(id='drawdown_chart')], style={
            'width': '100%',
            'height': '400',          # 👈 NARROW HEIGHT
            'border': '2px solid black',
            'borderRadius': '10px',
            'marginTop': '20px',
            'padding': '10px'
        }),

        html.Div([dcc.Graph(id='return_gauge')], style=box_style()),
    ], style={
        'display': 'flex',
        'alignItems': 'stretch',
        'alignItems': 'center',
        'justifyContent': 'center',
        'gap':'50px',
        'marginTop': '20px'
    })



])


@app.callback(
    [
        Output('chart', 'figure'),
        Output('return', 'children'),
        Output('sharpe', 'children'),
        Output('volume_chart', 'figure'),
        Output('volatility_gauge', 'figure'),
        Output('return_gauge', 'figure'),
        Output('drawdown_chart', 'figure')
    ],
    Input('symbol', 'value')
)
def update_dashboard(symbol):

    if symbol is None:
        symbol = Cfg["DEFAULT_SYMBOL"]

    dff = df[df[Cfg["SYMBOL_COLUMN"]] == symbol].copy()

    # KPIs
    total_return, volatility, sharpe, max_dd = calculate_kpis(dff)

    # MAIN CHART
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

        # Moving Averages
        for ma in Cfg["INDICATORS"]["moving_average"]:
            if ma in dff.columns:
                fig.add_trace(go.Scatter(
                    x=dff['date'],
                    y=dff[ma],
                    mode='lines',
                    name=ma.upper(),
                    line=dict(width=2)
                ))

    fig.update_layout(
        title={
            'text': f"{symbol}",
            'x': 0.5,
            'xanchor': 'center',
            'font': {
            'size': 22,
            'color': '#F02A02',
            'family': 'Segoe UI',
            'weight': 'bold'}
        },
        height=Cfg["APP"]["height"],
        xaxis_rangeslider_visible=Cfg["RANGE_SLIDER"]

    )


    return (
        fig,
        f"Return: {total_return}%",
        f"Sharpe: {sharpe}",
        volume_bar_chart(dff),
        create_gauge(volatility, "Volatility", max_val=100),
        create_gauge(total_return, "Returns", max_val=300),
        drawdown_chart(dff)
    )


# RUN APP

if __name__ == '__main__':
    app.run(debug=Cfg["APP"]["debug"])