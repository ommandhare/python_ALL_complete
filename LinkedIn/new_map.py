import pandas as pd
import plotly.express as px

# =========================
# SAMPLE DATA
# =========================

df = pd.DataFrame({

    "iso_alpha": [
        "IND",
        "USA",
        "DEU",
        "CAN",
        "AUS",
        "GBR"
    ],

    "country": [
        "India",
        "United States",
        "Germany",
        "Canada",
        "Australia",
        "United Kingdom"
    ],

    "connections": [
        250,
        180,
        70,
        50,
        40,
        90
    ]

})


# =========================
# WORLD MAP
# =========================

fig = px.choropleth(

    df,

    locations="iso_alpha",

    color="connections",

    hover_name="country",

    color_continuous_scale="Viridis"

)


# =========================
# LAYOUT
# =========================

fig.update_layout(

    title="LinkedIn Global Connections",

    margin={
        "r":0,
        "t":50,
        "l":0,
        "b":0
    }

)


# =========================
# SHOW
# =========================

fig.show()