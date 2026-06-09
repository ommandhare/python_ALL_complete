# ======================== THEME CONFIGURATION ========================
THEMES = {
    'light': {
        'bg_primary': '#f5f7fa',
        'bg_secondary': '#ffffff',
        'text_primary': '#1a1a1a',
        'text_secondary': '#555555',
        'border_color': '#e0e0e0',
        'accent_blue': '#1f77b4',
        'accent_orange': '#ff7f0e',
        'accent_green': '#2ca02c',
        'card_shadow': '0 4px 12px rgba(0, 0, 0, 0.08)',
        'header_gradient': 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
    },
    'dark': {
        'bg_primary': '#0f1419',
        'bg_secondary': '#1a1f2e',
        'text_primary': '#e8eef5',
        'text_secondary': '#a8adb5',
        'border_color': '#2d3139',
        'accent_blue': '#4a90e2',
        'accent_orange': '#f5a623',
        'accent_green': '#7ed321',
        'card_shadow': '0 4px 12px rgba(0, 0, 0, 0.3)',
        'header_gradient': 'linear-gradient(135deg, #1e3c72 0%, #2a5298 100%)',
    }
}

# ======================== CUSTOM CSS (MINIMAL) ========================
CUSTOM_CSS = '''
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>LinkedIn Connections Dashboard</title>
        {%favicon%}
        {%css%}
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
            
            body {
                font-family: 'Inter', -apple-system, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                transition: background 0.3s ease;
            }
            
            body.dark-mode {
                background: linear-gradient(135deg, #0f1419 0%, #1a1f2e 100%);
            }
        </style>
    </head>
    <body>
        {%app_entry%}
        <footer>{%config%}{%scripts%}{%renderer%}</footer>
    </body>
</html>
'''

# ======================== COMPONENT STYLES (MINIMAL) ========================
def get_header_style():
    return {
        'display': 'flex',
        'alignItems': 'center',
        'justifyContent': 'space-between',
        'padding': '20px 40px',
        'background': 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
        'boxShadow': '0 2px 8px rgba(0,0,0,0.1)',
    }

def get_title_style():
    return {'fontSize': '24px', 'fontWeight': '600', 'color': '#ffffff', 'margin': '0', 'textTransform': 'uppercase'}

def get_subtitle_style():
    return {'fontSize': '12px', 'color': 'rgba(255,255,255,0.8)', 'margin': '2px 0 0 0'}

def get_theme_toggle_style():
    return {
        'width': '40px',
        'height': '40px',
        'borderRadius': '50%',
        'border': 'none',
        'backgroundColor': 'rgba(255,255,255,0.15)',
        'color': '#ffffff',
        'fontSize': '20px',
        'cursor': 'pointer',
        'transition': 'all 0.3s ease',
    }

def get_content_area_style():
    return {'minHeight': 'calc(100vh - 100px)', 'transition': 'background 0.3s ease'}

def get_wrapper_style():
    return {'maxWidth': '1600px', 'margin': '0 auto', 'padding': '25px 40px 40px'}

def get_label_style():
    return {'fontSize': '12px', 'fontWeight': '600', 'marginBottom': '8px', 'display': 'block', 'textTransform': 'uppercase', 'letterSpacing': '0.3px'}

def get_filter_card_style(theme_config):
    return {
        'padding': '15px',
        'borderRadius': '8px',
        'backgroundColor': theme_config['bg_secondary'],
        'marginBottom': '25px',
        'boxShadow': theme_config['card_shadow'],
        'transition': 'all 0.3s ease',
    }

def get_kpi_card_style(theme_config, is_last=False):
    style = {'flex': '1', 'minWidth': '200px', 'borderRadius': '8px', 'overflow': 'hidden', 'backgroundColor': theme_config['bg_secondary'], 'boxShadow': theme_config['card_shadow'], 'transition': 'all 0.3s ease'}
    if not is_last:
        style['marginRight'] = '15px'
    return style

def get_chart_card_style(theme_config, is_last=False):
    style = {'flex': '1', 'minWidth': '400px', 'borderRadius': '8px', 'overflow': 'hidden', 'backgroundColor': theme_config['bg_secondary'], 'boxShadow': theme_config['card_shadow'], 'transition': 'all 0.3s ease'}
    if not is_last:
        style['marginRight'] = '15px'
    return style

def get_kpi_row_style():
    return {'display': 'flex', 'flexWrap': 'wrap', 'marginBottom': '25px', 'gap': '15px'}

def get_chart_row_style():
    return {'display': 'flex', 'flexWrap': 'wrap', 'gap': '15px', 'marginBottom': '25px'}

def get_summary_section_style():
    return {'marginBottom': '25px'}

def get_summary_card_style(theme_config):
    return {'padding': '20px', 'borderRadius': '8px', 'backgroundColor': theme_config['bg_secondary'], 'boxShadow': theme_config['card_shadow'], 'maxWidth': '350px', 'transition': 'all 0.3s ease'}

def get_summary_title_style():
    return {'fontSize': '14px', 'fontWeight': '600', 'marginBottom': '15px'}

def get_summary_text_style():
    return {'marginBottom': '10px', 'fontSize': '13px'}

def get_last_summary_text_style():
    return {'fontSize': '13px'}

def get_app_container_style():
    return {'display': 'flex', 'flexDirection': 'column', 'minHeight': '100vh', 'transition': 'all 0.3s ease'}

def get_main_container_style(theme_config):
    return {'display': 'flex', 'flexDirection': 'column', 'minHeight': '100vh', 'backgroundColor': theme_config['bg_primary'], 'transition': 'all 0.3s ease'}
