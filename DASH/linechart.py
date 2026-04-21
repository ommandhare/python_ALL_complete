import pandas as pd
import plotly.express as px

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

# Fix column name
df = df.rename(columns={'turnover_₹_cr': 'turnover'})

# Convert date
df['date'] = pd.to_datetime(df['date'])

# Filter one stock
dff = df[df['symbol'] == 'RELIANCE']

# Line chart
fig = px.line(dff, x='date', y='close', title='RELIANCE Price Trend')

fig.show()