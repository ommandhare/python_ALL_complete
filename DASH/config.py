Cfg = {
    "DATA_PATH": "3yrs_data_100sym.csv",

    "DATE_COLUMN": "date",
    "SYMBOL_COLUMN": "symbol",

    "CHART_TYPE": "candlestick",# candlestick / line
     # "RANGE_SLIDER" : True,

    "EMA": {
        "enabled": True,
        "span": 20
    },

    "KPIS": {
        "return": True,
        "volatility": True,
        "sharpe": True,
        "drawdown": True
    },

    "INDICATORS": {
    "moving_average": ["ma_7", "ma_14", "ma_21", "ma_28"]  # choose what to show
    },

    "APP": {
        "title": "MULTI ASSET TRADING DASHBOARD",
        "height": 600,
        "debug": True
    }
}