from dash import Dash, html, dcc, Input, Output, State
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import mysql.connector
from styles import (
    THEMES, CUSTOM_CSS, 
    get_header_style, get_title_style, get_subtitle_style, get_theme_toggle_style,
    get_content_area_style, get_wrapper_style, get_label_style,
    get_filter_card_style, get_kpi_card_style, get_chart_card_style,
    get_kpi_row_style, get_chart_row_style, get_summary_section_style,
    get_summary_card_style, get_summary_title_style, get_summary_text_style,
    get_last_summary_text_style, get_app_container_style, get_main_container_style
)

# ======================== SQL QUERIES (EASY TO MODIFY) ========================
# Query to get distinct connections
QUERY_DISTINCT_CONNECTIONS = """
SELECT Email_Address, First_Name, Last_Name, 
       COALESCE(Updated_Company, Company) as Company_Final,
       Seniority as Level, Owner
FROM linkedin_connections
GROUP BY Email_Address
ORDER BY Email_Address
"""

# Query to get all owners
QUERY_GET_OWNERS = """
SELECT DISTINCT Owner
FROM linkedin_connections
WHERE Owner IS NOT NULL AND Owner != ''
ORDER BY Owner
"""

# Query to get total connections by owner (or all)
QUERY_TOTAL_CONNECTIONS = """
SELECT COUNT(DISTINCT URL) as total_connections
FROM linkedin_connections
WHERE Owner = %s
"""

QUERY_TOTAL_CONNECTIONS_ALL = """
SELECT COUNT(DISTINCT URL) as total_connections
FROM linkedin_connections
"""

# Query to get total companies by owner (or all)
QUERY_TOTAL_COMPANIES = """
SELECT COUNT(DISTINCT COALESCE(Updated_Company, Company)) as total_companies
FROM linkedin_connections
WHERE Owner = %s
"""

QUERY_TOTAL_COMPANIES_ALL = """
SELECT COUNT(DISTINCT COALESCE(Updated_Company, Company)) as total_companies
FROM linkedin_connections
"""

# Query to get company-wise distribution (top 15)
QUERY_COMPANY_DISTRIBUTION = """
SELECT COALESCE(Updated_Company, Company) as Company, COUNT(DISTINCT URL) as Count
FROM linkedin_connections
WHERE Owner = %s
GROUP BY COALESCE(Updated_Company, Company)
ORDER BY Count DESC
LIMIT 15
"""

QUERY_COMPANY_DISTRIBUTION_ALL = """
SELECT COALESCE(Updated_Company, Company) as Company, COUNT(DISTINCT URL) as Count
FROM linkedin_connections
GROUP BY COALESCE(Updated_Company, Company)
ORDER BY Count DESC
LIMIT 15
"""

# Query to get level-wise distribution
QUERY_LEVEL_DISTRIBUTION = """
SELECT Seniority as Level, COUNT(DISTINCT URL) as Count
FROM linkedin_connections
WHERE Owner = %s AND Seniority IS NOT NULL AND Seniority != ''
GROUP BY Seniority
ORDER BY Count DESC
LIMIT 10
"""

QUERY_LEVEL_DISTRIBUTION_ALL = """
SELECT Seniority as Level, COUNT(DISTINCT URL) as Count
FROM linkedin_connections
WHERE Seniority IS NOT NULL AND Seniority != ''
GROUP BY Seniority
ORDER BY Count DESC
LIMIT 10
"""

# Query to get industry distribution
QUERY_INDUSTRY_DISTRIBUTION = """
SELECT industry, COUNT(*) as Count
FROM linkedin_comapanies_extented
WHERE owner = %s
GROUP BY industry
ORDER BY Count DESC
LIMIT 15
"""

QUERY_INDUSTRY_DISTRIBUTION_ALL = """
SELECT industry, COUNT(*) as Count
FROM linkedin_comapanies_extented
GROUP BY industry
ORDER BY Count DESC
LIMIT 15
"""

# Query to get country distribution
QUERY_COUNTRY_DISTRIBUTION = """
SELECT country, COUNT(*) as Count
FROM linkedin_comapanies_extented
WHERE owner = %s
GROUP BY country
ORDER BY Count DESC
"""

QUERY_COUNTRY_DISTRIBUTION_ALL = """
SELECT country, COUNT(*) as Count
FROM linkedin_comapanies_extented
GROUP BY country
ORDER BY Count DESC
"""

# Query to get connections over time by year and month
QUERY_CONNECTIONS_TIMELINE = """
SELECT YEAR(Connected_on_clean) as Year, MONTHNAME(Connected_on_clean) as Month, MONTH(Connected_on_clean) as MonthNum, COUNT(*) AS Connected
FROM linkedin_comapanies_extented
WHERE owner = %s
GROUP BY YEAR(Connected_on_clean), MONTH(Connected_on_clean), MONTHNAME(Connected_on_clean)
ORDER BY YEAR(Connected_on_clean), MONTH(Connected_on_clean)
"""

QUERY_CONNECTIONS_TIMELINE_ALL = """
SELECT YEAR(Connected_on_clean) as Year, MONTHNAME(Connected_on_clean) as Month, MONTH(Connected_on_clean) as MonthNum, COUNT(*) AS Connected
FROM linkedin_comapanies_extented
GROUP BY YEAR(Connected_on_clean), MONTH(Connected_on_clean), MONTHNAME(Connected_on_clean)
ORDER BY YEAR(Connected_on_clean), MONTH(Connected_on_clean)
"""

# Query to get connections by year only
QUERY_CONNECTIONS_BY_YEAR = """
SELECT YEAR(Connected_on_clean) as Year, COUNT(*) AS Connected
FROM linkedin_comapanies_extented
WHERE owner = %s
GROUP BY YEAR(Connected_on_clean)
ORDER BY YEAR(Connected_on_clean)
"""

QUERY_CONNECTIONS_BY_YEAR_ALL = """
SELECT YEAR(Connected_on_clean) as Year, COUNT(*) AS Connected
FROM linkedin_comapanies_extented
GROUP BY YEAR(Connected_on_clean)
ORDER BY YEAR(Connected_on_clean)
"""

# Query to get connections by month for a specific year
QUERY_CONNECTIONS_BY_MONTH = """
SELECT MONTHNAME(Connected_on_clean) as Month, MONTH(Connected_on_clean) as MonthNum, COUNT(*) AS Connected
FROM linkedin_comapanies_extented
WHERE owner = %s AND YEAR(Connected_on_clean) = %s
GROUP BY YEAR(Connected_on_clean), MONTH(Connected_on_clean), MONTHNAME(Connected_on_clean)
ORDER BY MONTH(Connected_on_clean)
"""

QUERY_CONNECTIONS_BY_MONTH_ALL = """
SELECT MONTHNAME(Connected_on_clean) as Month, MONTH(Connected_on_clean) as MonthNum, COUNT(*) AS Connected
FROM linkedin_comapanies_extented
WHERE YEAR(Connected_on_clean) = %s
GROUP BY YEAR(Connected_on_clean), MONTH(Connected_on_clean), MONTHNAME(Connected_on_clean)
ORDER BY MONTH(Connected_on_clean)
"""

# ======================== DATABASE CONNECTION FUNCTION ========================
def get_db_connection():
    """Create and return database connection"""
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='0777',
        database='connect_project'
    )

# ======================== FUNCTION TO FETCH DATA FROM DATABASE ========================
def fetch_query(query, params=None):
    """Execute query and return dataframe"""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        
        results = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description] if cursor.description else []
        cursor.close()
        conn.close()
        
        return pd.DataFrame(results, columns=columns)
    except Exception as e:
        print(f"Database Error: {str(e)}")
        return pd.DataFrame()

# ======================== COUNTRY NAME TO ISO-3 CODE MAPPING ========================
COUNTRY_MAPPING = {
    'india': 'IND',
    'united kingdom': 'GBR',
    'united states': 'USA',
    'germany': 'DEU',
    'france': 'FRA',
    'switzerland': 'CHE',
    'australia': 'AUS',
    'japan': 'JPN',
    'finland': 'FIN',
    'singapore': 'SGP',
    'united arab emirates': 'ARE',
    'canada': 'CAN',
    'uruguay': 'URY',
    'bahrain': 'BHR',
    'italy': 'ITA',
    'spain': 'ESP',
    'south africa': 'ZAF',
    'poland': 'POL',
    'israel': 'ISR',
    'estonia': 'EST',
    'netherlands': 'NLD',
    'sweden': 'SWE',
    'norway': 'NOR',
    'denmark': 'DNK',
    'belgium': 'BEL',
    'austria': 'AUT',
    'portugal': 'PRT',
    'brazil': 'BRA',
    'mexico': 'MEX',
    'argentina': 'ARG',
    'china': 'CHN',
    'hong kong': 'HKG',
    'south korea': 'KOR',
    'indonesia': 'IDN',
    'malaysia': 'MYS',
    'thailand': 'THA',
    'philippines': 'PHL',
    'vietnam': 'VNM',
    'new zealand': 'NZL',
    'egypt': 'EGY',
    'nigeria': 'NGA',
    'kenya': 'KEN',
    'saudi arabia': 'SAU',
    'qatar': 'QAT',
    'kuwait': 'KWT',
    'turkey': 'TUR',
    'russia': 'RUS',
    'ukraine': 'UKR',
    'czech republic': 'CZE',
    'hungary': 'HUN',
    'romania': 'ROU',
    'greece': 'GRC',
    'ireland': 'IRL',
    'luxembourg': 'LUX',
    'pakistan': 'PAK',
    'bangladesh': 'BGD',
    'sri lanka': 'LKA',
    'nepal': 'NPL',
}

def get_country_iso_code(country_name):
    """Convert country name to ISO-3 code for Plotly choropleth"""
    if pd.isna(country_name):
        return None
    country_lower = str(country_name).strip().lower()
    return COUNTRY_MAPPING.get(country_lower, None)

# ======================== GET OWNERS LIST ========================
try:
    owners_df = fetch_query(QUERY_GET_OWNERS)
    if len(owners_df) > 0 and 'Owner' in owners_df.columns:
        owners_list = owners_df['Owner'].tolist()
        owners_list.insert(0, 'All Owners')
    else:
        owners_list = ['All Owners']
except Exception as e:
    print(f"Error loading owners: {str(e)}")
    owners_list = ['All Owners']

print(f"Available Owners: {owners_list}")

# ======================== FUNCTION TO CREATE VISUALIZATIONS ========================
def create_visualizations(selected_owner, theme='light', drill_level='year_month', selected_year=None):
    """Create all visualizations based on SQL queries
    
    Args:
        selected_owner: The selected owner filter
        theme: 'light' or 'dark'
        drill_level: 'year_month' (full), 'year' (by year), or 'month' (by month of a year)
        selected_year: The selected year for month drill-down
    """
    
    try:
        theme_config = THEMES[theme]
        
        # Determine if filtering by owner or all
        filter_by_owner = selected_owner != 'All Owners' and selected_owner is not None
        
        # Get Total Connections
        if filter_by_owner:
            conn_df = fetch_query(QUERY_TOTAL_CONNECTIONS, (selected_owner,))
        else:
            conn_df = fetch_query(QUERY_TOTAL_CONNECTIONS_ALL)
        total_connections = conn_df['total_connections'].values[0] if len(conn_df) > 0 else 0
        
        # Get Total Companies
        if filter_by_owner:
            comp_df = fetch_query(QUERY_TOTAL_COMPANIES, (selected_owner,))
        else:
            comp_df = fetch_query(QUERY_TOTAL_COMPANIES_ALL)
        total_companies = comp_df['total_companies'].values[0] if len(comp_df) > 0 else 0
    
        # Get Company Distribution
        if filter_by_owner:
            company_dist = fetch_query(QUERY_COMPANY_DISTRIBUTION, (selected_owner,))
        else:
            company_dist = fetch_query(QUERY_COMPANY_DISTRIBUTION_ALL)
        
        # Get Level Distribution
        if filter_by_owner:
            level_dist = fetch_query(QUERY_LEVEL_DISTRIBUTION, (selected_owner,))
        else:
            level_dist = fetch_query(QUERY_LEVEL_DISTRIBUTION_ALL)
    
        # ======================== CREATE VISUALIZATIONS ========================
        # 1. Total Connections KPI Card
        fig_connections = go.Figure(go.Indicator(
            mode="number",
            value=int(total_connections),
            title={"text": "Total Connections", "font": {"size": 16}},
            domain={'x': [0, 1], 'y': [0, 1]},
            number={'font': {'size': 54, 'color': theme_config['accent_blue']}, 'suffix': ''},
        ))
        
        fig_connections.update_layout(
            height=280,
            margin=dict(l=20, r=20, t=50, b=20),
            paper_bgcolor=theme_config['bg_secondary'],
            plot_bgcolor=theme_config['bg_secondary'],
            font=dict(family='Inter, -apple-system, sans-serif', size=14, color=theme_config['text_primary']),
            showlegend=False,
        )
        
        # 2. Total Companies KPI Card
        fig_companies = go.Figure(go.Indicator(
            mode="number",
            value=int(total_companies),
            title={"text": "Total Companies", "font": {"size": 16}},
            domain={'x': [0, 1], 'y': [0, 1]},
            number={'font': {'size': 54, 'color': theme_config['accent_orange']}, 'suffix': ''},
        ))
        
        fig_companies.update_layout(
            height=280,
            margin=dict(l=20, r=20, t=50, b=20),
            paper_bgcolor=theme_config['bg_secondary'],
            plot_bgcolor=theme_config['bg_secondary'],
            font=dict(family='Inter, -apple-system, sans-serif', size=14, color=theme_config['text_primary']),
            showlegend=False,
        )
    
        # 3. Pie Chart - People by Company
        if len(company_dist) > 0:
            fig_company_pie = px.pie(
                company_dist,
                values='Count',
                names='Company',
                title='People by Company',
                hole=0.3,
                color_discrete_sequence=px.colors.qualitative.Set1
            )
            fig_company_pie.update_traces(
                textposition='inside',
                textinfo='percent+label',
                textfont=dict(size=11, color=theme_config['text_primary'])
            )
        else:
            fig_company_pie = go.Figure().add_annotation(text="No data available")
        
        fig_company_pie.update_layout(
            height=500,
            title={'font': {'size': 18, 'color': theme_config['text_primary']}},
            font=dict(family='Inter, -apple-system, sans-serif', size=12, color=theme_config['text_secondary']),
            paper_bgcolor=theme_config['bg_secondary'],
            plot_bgcolor=theme_config['bg_secondary'],
            showlegend=True,
            legend=dict(x=0.98, y=0.95, bgcolor='rgba(0,0,0,0)', bordercolor='rgba(0,0,0,0)'),
            margin=dict(l=20, r=20, t=40, b=20),
        )
    
        # 4. Horizontal Bar Chart - People by Level/Seniority
        if len(level_dist) > 0:
            level_dist_sorted = level_dist.sort_values('Count', ascending=True)
            fig_level_bar = px.bar(
                level_dist_sorted,
                x='Count',
                y='Level',
                title='Distribution by Seniority Level',
                labels={'Count': 'Number of People', 'Level': 'Level'},
                color='Count',
                color_continuous_scale='Viridis',
            )
            fig_level_bar.update_traces(
                text=level_dist_sorted['Count'],
                textposition='outside',
                textfont=dict(size=11),
                hovertemplate='<b>%{y}</b><br>Count: %{x}<extra></extra>'
            )
        else:
            fig_level_bar = go.Figure().add_annotation(text="No data available")
        
        fig_level_bar.update_layout(
            height=500,
            title={'font': {'size': 18, 'color': theme_config['text_primary']}},
            font=dict(family='Inter, -apple-system, sans-serif', size=12, color=theme_config['text_secondary']),
            paper_bgcolor=theme_config['bg_secondary'],
            plot_bgcolor=theme_config['bg_secondary'],
            showlegend=False,
            xaxis_title='Number of People',
            xaxis_title_font=dict(size=12, color=theme_config['text_primary']),
            yaxis_title='Seniority Level',
            yaxis_title_font=dict(size=12, color=theme_config['text_primary']),
            margin=dict(l=120, r=20, t=40, b=20),
            xaxis=dict(gridcolor=theme_config['border_color']),
            yaxis=dict(gridcolor=theme_config['border_color']),
        )
        
        # 5. Vertical Bar Chart - Industry Distribution
        if filter_by_owner:
            industry_dist = fetch_query(QUERY_INDUSTRY_DISTRIBUTION, (selected_owner,))
        else:
            industry_dist = fetch_query(QUERY_INDUSTRY_DISTRIBUTION_ALL)
        
        if len(industry_dist) > 0:
            fig_industry_bar = px.bar(
                industry_dist,
                x='industry',
                y='Count',
                title='Companies by Industry',
                labels={'Count': 'Number of Companies', 'industry': 'Industry'},
                color='Count',
                color_continuous_scale='Blues',
            )
            fig_industry_bar.update_traces(
                text=industry_dist['Count'],
                textposition='outside',
                textfont=dict(size=10),
                hovertemplate='<b>%{x}</b><br>Count: %{y}<extra></extra>'
            )
        else:
            fig_industry_bar = go.Figure().add_annotation(text="No data available")
        
        fig_industry_bar.update_layout(
            height=450,
            title={'font': {'size': 16, 'color': theme_config['text_primary']}},
            font=dict(family='Inter, -apple-system, sans-serif', size=11, color=theme_config['text_secondary']),
            paper_bgcolor=theme_config['bg_secondary'],
            plot_bgcolor=theme_config['bg_secondary'],
            showlegend=False,
            xaxis_title='Industry',
            yaxis_title='Count',
            margin=dict(l=50, r=20, t=40, b=60),
            xaxis=dict(tickangle=45, gridcolor=theme_config['border_color']),
            yaxis=dict(gridcolor=theme_config['border_color']),
        )
        
        # ======================== 6. GLOBAL PRESENCE BY COUNTRY (CHOROPLETH MAP) ========================
        if filter_by_owner:
            country_dist = fetch_query(QUERY_COUNTRY_DISTRIBUTION, (selected_owner,))
        else:
            country_dist = fetch_query(QUERY_COUNTRY_DISTRIBUTION_ALL)

        # Theme-aware land/ocean colors
        if theme == 'dark':
            land_color = "#ffffff"
            ocean_color = "#c5f1f9"
        else:
            land_color = '#f0ece4'
            ocean_color = "#c5f1f9"

        fig_country_map = go.Figure()  # always initialize first

        if len(country_dist) > 0 and country_dist['country'].notna().any():
            country_dist = country_dist.dropna(subset=['country'])
            country_dist['iso_alpha'] = country_dist['country'].apply(get_country_iso_code)
            country_dist_mapped = country_dist.dropna(subset=['iso_alpha'])

            # DEBUG - remove after confirming map works
            # print("=== RAW COUNTRY VALUES FROM DB ===")
            # for val in country_dist['country'].tolist():
                # print(repr(val))
            # print("=== UNMAPPED COUNTRIES ===")
            # unmapped = country_dist[country_dist['iso_alpha'].isna()]['country'].tolist()
            # print(unmapped)

            if len(country_dist_mapped) > 0:
                fig_country_map.add_trace(go.Choropleth(
                    locations=country_dist_mapped['iso_alpha'],
                    z=country_dist_mapped['Count'].astype(float),
                    text=country_dist_mapped['country'],
                    colorscale='Turbo',
                    autocolorscale=False,
                    reversescale=False,
                    marker_line_color='white',
                    marker_line_width=0.5,
                    colorbar_title='Connections',
                    hovertemplate='<b>%{text}</b><br>Connections: %{z}<extra></extra>',
                ))
            else:
                fig_country_map.add_annotation(
                    text="No mappable country data — check terminal for unmapped values",
                    xref="paper", yref="paper", x=0.5, y=0.5,
                    showarrow=False,
                    font=dict(size=13, color=theme_config['text_secondary'])
                )
        else:
            fig_country_map.add_annotation(
                text="No country data available",
                xref="paper", yref="paper", x=0.5, y=0.5,
                showarrow=False,
                font=dict(size=13, color=theme_config['text_secondary'])
            )

        fig_country_map.update_layout(
            height=450,
            title={
                'text': 'Global Presence by Country',
                'font': {'size': 16, 'color': theme_config['text_primary']}
            },
            font=dict(
                family='Inter, -apple-system, sans-serif',
                size=11,
                color=theme_config['text_secondary']
            ),
            paper_bgcolor=theme_config['bg_secondary'],
            margin=dict(l=0, r=0, t=40, b=0),
            geo=dict(
                showframe=False,
                showcoastlines=True,
                coastlinecolor='Gray',
                showland=True,
                landcolor=land_color,
                showocean=True,
                oceancolor=ocean_color,
                showlakes=False,
                showcountries=True,
                countrycolor='Gray',
                projection_type='natural earth',
                bgcolor=theme_config['bg_secondary'],
            ),
        )
        # ======================== END CHOROPLETH MAP ========================

        # 7. Connections Timeline - Line Chart with Drill-down
        available_years = []
        
        if drill_level == 'year':
            # View by Year only
            if filter_by_owner:
                timeline_dist = fetch_query(QUERY_CONNECTIONS_BY_YEAR, (selected_owner,))
            else:
                timeline_dist = fetch_query(QUERY_CONNECTIONS_BY_YEAR_ALL)
            
            if len(timeline_dist) > 0:
                available_years = timeline_dist['Year'].astype(int).tolist()
                fig_timeline = px.line(
                    timeline_dist,
                    x='Year',
                    y='Connected',
                    title='Connections by Year',
                    labels={'Connected': 'Number of Connections', 'Year': 'Year'},
                    markers=True,
                )
                fig_timeline.update_traces(
                    line=dict(color=theme_config['accent_blue'], width=3),
                    marker=dict(size=10, color=theme_config['accent_blue']),
                    hovertemplate='<b>Year: %{x}</b><br>Connections: %{y}<extra></extra>'
                )
            else:
                fig_timeline = go.Figure().add_annotation(text="No data available")
            
            chart_title = 'Connections by Year'
            
        elif drill_level == 'month' and selected_year:
            # View by Month for a specific year
            if filter_by_owner:
                timeline_dist = fetch_query(QUERY_CONNECTIONS_BY_MONTH, (selected_owner, selected_year))
            else:
                timeline_dist = fetch_query(QUERY_CONNECTIONS_BY_MONTH_ALL, (selected_year,))
            
            if len(timeline_dist) > 0:
                fig_timeline = px.line(
                    timeline_dist,
                    x='Month',
                    y='Connected',
                    title=f'Connections by Month ({selected_year})',
                    labels={'Connected': 'Number of Connections', 'Month': 'Month'},
                    markers=True,
                )
                fig_timeline.update_traces(
                    line=dict(color=theme_config['accent_orange'], width=3),
                    marker=dict(size=10, color=theme_config['accent_orange']),
                    hovertemplate='<b>%{x}</b><br>Connections: %{y}<extra></extra>'
                )
            else:
                fig_timeline = go.Figure().add_annotation(text="No data available")
            
            chart_title = f'Connections by Month ({selected_year})'
            
        else:
            # Default: View by Year-Month
            if filter_by_owner:
                timeline_dist = fetch_query(QUERY_CONNECTIONS_TIMELINE, (selected_owner,))
            else:
                timeline_dist = fetch_query(QUERY_CONNECTIONS_TIMELINE_ALL)
            
            if len(timeline_dist) > 0:
                available_years = timeline_dist['Year'].astype(int).unique().tolist()
                available_years.sort()
                # Create a proper date column for sorting
                timeline_dist['YearMonth'] = timeline_dist['Year'].astype(str) + '-' + timeline_dist['Month']
                
                fig_timeline = px.line(
                    timeline_dist,
                    x='YearMonth',
                    y='Connected',
                    title='Connections Timeline (Year-Month)',
                    labels={'Connected': 'Number of Connections', 'YearMonth': 'Year-Month'},
                    markers=True,
                )
                fig_timeline.update_traces(
                    line=dict(color=theme_config['accent_blue'], width=3),
                    marker=dict(size=8, color=theme_config['accent_blue']),
                    hovertemplate='<b>%{x}</b><br>Connections: %{y}<extra></extra>'
                )
            else:
                fig_timeline = go.Figure().add_annotation(text="No data available")
            
            chart_title = 'Connections Timeline (Year-Month)'
        
        fig_timeline.update_layout(
            height=500,
            title={'text': chart_title, 'font': {'size': 18, 'color': theme_config['text_primary']}},
            font=dict(family='Inter, -apple-system, sans-serif', size=11, color=theme_config['text_secondary']),
            paper_bgcolor=theme_config['bg_secondary'],
            plot_bgcolor=theme_config['bg_secondary'],
            showlegend=False,
            xaxis_title='Period',
            yaxis_title='Number of Connections',
            xaxis_title_font=dict(size=12, color=theme_config['text_primary']),
            yaxis_title_font=dict(size=12, color=theme_config['text_primary']),
            margin=dict(l=50, r=20, t=40, b=60),
            xaxis=dict(tickangle=45, gridcolor=theme_config['border_color']),
            yaxis=dict(gridcolor=theme_config['border_color']),
        )
        
        return fig_connections, fig_companies, fig_company_pie, fig_level_bar, fig_industry_bar, fig_country_map, fig_timeline, available_years, total_connections, total_companies
    
    except Exception as e:
        print(f"Error in create_visualizations: {str(e)}")
        empty_fig = go.Figure()
        return empty_fig, empty_fig, empty_fig, empty_fig, empty_fig, empty_fig, empty_fig, [], 0, 0

# ======================== CREATE DASH APP ========================
app = Dash(__name__)
app.index_string = CUSTOM_CSS

app.layout = html.Div([
    # Theme Store
    dcc.Store(id='theme-store', data='light'),
    # Drill-down State Store
    dcc.Store(id='drill-state-store', data={'drill_level': 'year_month', 'selected_year': None}),
    
    # Main Container with ID for callbacks
    html.Div(id='main-container', children=[
        # Navigation Header
        html.Div([
            html.Div([
                html.H1('Sahastra Arjun', style=get_title_style()),
                html.P('Analytics Dashboard', style=get_subtitle_style()),
            ], style={'flex': '1'}),
            
            # Theme Toggle Button
            html.Button(
                '🌙',
                id='theme-toggle-btn',
                n_clicks=0,
                style=get_theme_toggle_style(),
            ),
        ], style=get_header_style()),
        
        # Content Area
        html.Div([
            html.Div([
                # Filter Card
                html.Div([
                    html.Div([
                        html.Label('Select Owner', style=get_label_style()),
                        dcc.Dropdown(
                            id='owner-dropdown',
                            options=[{'label': owner, 'value': owner} for owner in owners_list],
                            value='All Owners',
                            clearable=False,
                            style={'width': '100%'}
                        )
                    ], style={'width': '100%'})
                ], id='filter-card'),
                
                # KPI Cards Row
                html.Div([
                    html.Div([
                        dcc.Graph(id='kpi-connections', config={'displayModeBar': False})
                    ], id='kpi-card-1'),
                    
                    html.Div([
                        dcc.Graph(id='kpi-companies', config={'displayModeBar': False})
                    ], id='kpi-card-2'),
                ], style=get_kpi_row_style()),
                
                # Charts Row
                html.Div([
                    html.Div([
                        dcc.Graph(id='company-pie-chart', config={'displayModeBar': True, 'displaylogo': False})
                    ], id='pie-card'),
                    
                    html.Div([
                        dcc.Graph(id='level-bar-chart', config={'displayModeBar': True, 'displaylogo': False})
                    ], id='bar-card'),
                ], style=get_chart_row_style()),
                
                # Industry & Country Row
                html.Div([
                    html.Div([
                        dcc.Graph(id='industry-bar-chart', config={'displayModeBar': True, 'displaylogo': False})
                    ], id='industry-card', style={'flex': '1', 'minWidth': '400px', 'borderRadius': '8px', 'overflow': 'hidden', 'boxShadow': '0 2px 6px rgba(0,0,0,0.1)', 'transition': 'all 0.3s ease', 'marginRight': '15px'}),
                    
                    html.Div([
                        dcc.Graph(id='country-map-chart', config={'displayModeBar': True, 'displaylogo': False})
                    ], id='country-card', style={'flex': '1', 'minWidth': '400px', 'borderRadius': '8px', 'overflow': 'hidden', 'boxShadow': '0 2px 6px rgba(0,0,0,0.1)', 'transition': 'all 0.3s ease'}),
                ], style=get_chart_row_style()),
                
                # Timeline Line Chart Row (Full Width) with Drill-down Controls
                html.Div([
                    html.Div([
                        html.Div([
                            html.Button('← Back', id='drill-back-btn', n_clicks=0, style={
                                'padding': '10px 15px', 'marginRight': '10px', 'borderRadius': '4px',
                                'border': '1px solid #ccc', 'backgroundColor': '#f5f5f5', 'cursor': 'pointer',
                                'fontWeight': '500', 'display': 'none'
                            }),
                            html.Button('Drill by Year', id='drill-year-btn', n_clicks=0, style={
                                'padding': '10px 15px', 'marginRight': '10px', 'borderRadius': '4px',
                                'border': '1px solid #007bff', 'backgroundColor': '#e7f1ff', 'cursor': 'pointer',
                                'fontWeight': '500', 'color': "#00ff51"
                            }),
                            html.Button('View Year-Month', id='drill-full-btn', n_clicks=0, style={
                                'padding': '10px 15px', 'marginRight': '10px', 'borderRadius': '4px',
                                'border': '1px solid #ccc', 'backgroundColor': '#f5f5f5', 'cursor': 'pointer',
                                'fontWeight': '500'
                            }),
                            dcc.Dropdown(
                                id='drill-year-dropdown',
                                options=[],
                                value=None,
                                placeholder='Select Year for Month Drill',
                                style={'width': '200px', 'display': 'none'}
                            ),
                        ], style={'display': 'flex', 'alignItems': 'center', 'marginBottom': '15px', 'gap': '10px'}),
                        dcc.Graph(id='timeline-line-chart', config={'displayModeBar': True, 'displaylogo': False})
                    ], id='timeline-card', style={'width': '100%', 'borderRadius': '8px', 'overflow': 'hidden', 'boxShadow': '0 2px 6px rgba(0,0,0,0.1)', 'transition': 'all 0.3s ease', 'padding': '15px'}),
                ], style=dict(display='flex', flexWrap='wrap', gap='15px', width='100%', marginBottom='15px')),
                
            ], style=get_wrapper_style()),
        ], id='content-area', style=get_content_area_style()),
    ]),
], id='app-wrapper', style=get_app_container_style())

# ======================== CALLBACKS FOR THEME AND DATA ========================
@app.callback(
    [Output('main-container', 'style'),
     Output('filter-card', 'style'),
     Output('kpi-card-1', 'style'),
     Output('kpi-card-2', 'style'),
     Output('pie-card', 'style'),
     Output('bar-card', 'style'),
     Output('theme-store', 'data'),
     Output('theme-toggle-btn', 'children')],
    Input('theme-toggle-btn', 'n_clicks'),
    State('theme-store', 'data'),
)
def toggle_theme(n_clicks, current_theme):
    new_theme = 'dark' if current_theme == 'light' else 'light'
    theme_config = THEMES[new_theme]
    
    toggle_emoji = '☀️' if new_theme == 'dark' else '🌙'
    
    return (
        get_main_container_style(theme_config),
        get_filter_card_style(theme_config),
        get_kpi_card_style(theme_config, is_last=False),
        get_kpi_card_style(theme_config, is_last=True),
        get_chart_card_style(theme_config, is_last=False),
        get_chart_card_style(theme_config, is_last=True),
        new_theme,
        toggle_emoji
    )

@app.callback(
    Output('drill-state-store', 'data'),
    [Input('drill-year-btn', 'n_clicks'),
     Input('drill-full-btn', 'n_clicks'),
     Input('drill-back-btn', 'n_clicks')],
    State('drill-state-store', 'data'),
    prevent_initial_call=True
)
def handle_drill_buttons(year_clicks, full_clicks, back_clicks, current_state):
    """Handle drill-down button clicks only"""
    if not current_state:
        current_state = {'drill_level': 'year_month', 'selected_year': None}
    
    # Get which button was clicked using callback_context
    from dash import callback_context
    ctx = callback_context
    if not ctx.triggered:
        return current_state
    
    button_id = ctx.triggered[0]['prop_id'].split('.')[0]
    
    if button_id == 'drill-year-btn':
        return {'drill_level': 'year', 'selected_year': None}
    elif button_id == 'drill-full-btn':
        return {'drill_level': 'year_month', 'selected_year': None}
    elif button_id == 'drill-back-btn':
        return {'drill_level': 'year', 'selected_year': None}
    
    return current_state

@app.callback(
    Output('drill-state-store', 'data', allow_duplicate=True),
    Input('drill-year-dropdown', 'value'),
    State('drill-state-store', 'data'),
    prevent_initial_call=True
)
def handle_year_selection(selected_year, current_state):
    """Handle year dropdown selection - only when a year is selected"""
    if not current_state:
        current_state = {'drill_level': 'year_month', 'selected_year': None}
    
    # Only update if we're in year view and a year is selected
    if current_state.get('drill_level') == 'year' and selected_year:
        return {'drill_level': 'month', 'selected_year': selected_year}
    
    return current_state

@app.callback(
    [Output('kpi-connections', 'figure'),
     Output('kpi-companies', 'figure'),
     Output('company-pie-chart', 'figure'),
     Output('level-bar-chart', 'figure'),
     Output('industry-bar-chart', 'figure'),
     Output('country-map-chart', 'figure'),
     Output('timeline-line-chart', 'figure'),
     Output('drill-year-dropdown', 'options'),
     Output('drill-year-dropdown', 'style'),
     Output('drill-back-btn', 'style'),
     Output('drill-year-btn', 'style'),
     Output('drill-full-btn', 'style')],
    [Input('owner-dropdown', 'value'),
     Input('theme-store', 'data'),
     Input('drill-state-store', 'data'),
     Input('drill-year-dropdown', 'value')]
)
def update_dashboard(selected_owner, theme, drill_state, dropdown_value):
    try:
        if not drill_state:
            drill_state = {'drill_level': 'year_month', 'selected_year': None}
        
        fig_conn, fig_comp, fig_pie, fig_bar, fig_industry, fig_country, fig_timeline, available_years, total_conn, total_comp = create_visualizations(
            selected_owner, theme, drill_state['drill_level'], drill_state['selected_year']
        )
        
        # Prepare year dropdown options
        year_options = [{'label': str(year), 'value': year} for year in available_years]
        
        # Dropdown styling based on drill level
        dropdown_style = {
            'width': '200px',
            'display': 'block' if drill_state['drill_level'] == 'year' else 'none'
        }
        
        # Button styling based on drill level
        active_style = {'padding': '10px 15px', 'marginRight': '10px', 'borderRadius': '4px',
                       'border': '1px solid #007bff', 'backgroundColor': '#e7f1ff', 'cursor': 'pointer',
                       'fontWeight': '500', 'color': '#007bff'}
        inactive_style = {'padding': '10px 15px', 'marginRight': '10px', 'borderRadius': '4px',
                         'border': '1px solid #ccc', 'backgroundColor': '#f5f5f5', 'cursor': 'pointer',
                         'fontWeight': '500'}
        
        back_btn_style = inactive_style.copy()
        back_btn_style['display'] = 'block' if drill_state['drill_level'] in ['year', 'month'] else 'none'
        
        year_btn_style = active_style if drill_state['drill_level'] == 'year' else inactive_style
        full_btn_style = active_style if drill_state['drill_level'] == 'year_month' else inactive_style
        
        return (
            fig_conn, fig_comp, fig_pie, fig_bar, fig_industry, fig_country, fig_timeline,
            year_options, dropdown_style, back_btn_style, year_btn_style, full_btn_style
        )
    except Exception as e:
        print(f"Error in update_dashboard callback: {str(e)}")
        empty_fig = go.Figure()
        empty_style = {}
        return (
            empty_fig, empty_fig, empty_fig, empty_fig, empty_fig, empty_fig, empty_fig,
            [], {}, {}, {}, {}
        )

# Sync dropdown value with drill_state selected_year
@app.callback(
    Output('drill-year-dropdown', 'value'),
    Input('drill-state-store', 'data')
)
def sync_dropdown_with_drill_state(drill_state):
    """Keep dropdown value in sync with selected_year in drill_state"""
    if not drill_state or drill_state.get('drill_level') != 'month':
        return None
    return drill_state.get('selected_year', None)

# ======================== RUN APP ========================
if __name__ == '__main__':
    app.run(debug=True, port=8000)