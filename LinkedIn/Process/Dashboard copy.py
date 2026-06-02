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
def create_visualizations(selected_owner, theme='light'):
    """Create all visualizations based on SQL queries"""
    
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
            height=400,
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
        
        # 6. World Map - Country Distribution
        if filter_by_owner:
            country_dist = fetch_query(QUERY_COUNTRY_DISTRIBUTION, (selected_owner,))
        else:
            country_dist = fetch_query(QUERY_COUNTRY_DISTRIBUTION_ALL)
        
        if len(country_dist) > 0:
            # Convert country names to ISO-3 codes
            country_dist['iso_code'] = country_dist['country'].apply(get_country_iso_code)
            country_dist = country_dist.dropna(subset=['iso_code'])
            
            if len(country_dist) > 0:
                fig_country_map = px.choropleth(
                    country_dist,
                    locations='iso_code',
                    locationmode='ISO-3',
                    color='Count',
                    hover_name='country',
                    hover_data={'iso_code': False, 'Count': True},
                    title='Global Presence by Country',
                    color_continuous_scale='Viridis',
                )
            else:
                fig_country_map = go.Figure().add_annotation(text="No data available")
        else:
            fig_country_map = go.Figure().add_annotation(text="No data available")
        
        fig_country_map.update_layout(
            height=450,
            title={'font': {'size': 16, 'color': theme_config['text_primary']}},
            font=dict(family='Inter, -apple-system, sans-serif', size=11, color=theme_config['text_secondary']),
            paper_bgcolor=theme_config['bg_secondary'],
            plot_bgcolor=theme_config['bg_secondary'],
            geo=dict(showframe=False, projection_type='natural earth'),
            margin=dict(l=0, r=0, t=40, b=0),
        )
        
        return fig_connections, fig_companies, fig_company_pie, fig_level_bar, fig_industry_bar, fig_country_map, total_connections, total_companies
    
    except Exception as e:
        print(f"Error in create_visualizations: {str(e)}")
        empty_fig = go.Figure()
        return empty_fig, empty_fig, empty_fig, empty_fig, empty_fig, empty_fig, 0, 0

# ======================== CREATE DASH APP ========================
app = Dash(__name__)
app.index_string = CUSTOM_CSS

app.layout = html.Div([
    # Theme Store
    dcc.Store(id='theme-store', data='light'),
    
    # Main Container with ID for callbacks
    html.Div(id='main-container', children=[
        # Navigation Header
        html.Div([
            html.Div([
                html.H1('LinkedIn Connections', style=get_title_style()),
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
                
                # Summary Section
                html.Div([
                    html.Div([
                        html.H3('Summary Statistics', style=get_summary_title_style()),
                        html.Div([
                            html.P(id='summary-connections', style=get_summary_text_style()),
                            html.P(id='summary-companies', style=get_summary_text_style()),
                            html.P(id='summary-average', style=get_last_summary_text_style()),
                        ])
                    ], id='summary-card')
                ], style=get_summary_section_style()),
                
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
     Output('summary-card', 'style'),
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
        get_summary_card_style(theme_config),
        new_theme,
        toggle_emoji
    )

@app.callback(
    [Output('kpi-connections', 'figure'),
     Output('kpi-companies', 'figure'),
     Output('company-pie-chart', 'figure'),
     Output('level-bar-chart', 'figure'),
     Output('industry-bar-chart', 'figure'),
     Output('country-map-chart', 'figure'),
     Output('summary-connections', 'children'),
     Output('summary-companies', 'children'),
     Output('summary-average', 'children')],
    [Input('owner-dropdown', 'value'),
     Input('theme-store', 'data')]
)
def update_dashboard(selected_owner, theme):
    try:
        fig_conn, fig_comp, fig_pie, fig_bar, fig_industry, fig_country, total_conn, total_comp = create_visualizations(selected_owner, theme)
        
        avg_connections = float(total_conn) / float(total_comp) if total_comp > 0 else 0
        
        summary_conn = f'✓ Distinct Connections: {int(total_conn)}'
        summary_comp = f'✓ Total Companies: {int(total_comp)}'
        summary_avg = f'✓ Avg per Company: {avg_connections:.1f}'
        
        return fig_conn, fig_comp, fig_pie, fig_bar, fig_industry, fig_country, summary_conn, summary_comp, summary_avg
    except Exception as e:
        print(f"Error in update_dashboard callback: {str(e)}")
        empty_fig = go.Figure()
        return empty_fig, empty_fig, empty_fig, empty_fig, empty_fig, empty_fig, 'Error', 'Error', 'Error'

# ======================== RUN APP ========================
if __name__ == '__main__':
    app.run(debug=True, port=8050)
