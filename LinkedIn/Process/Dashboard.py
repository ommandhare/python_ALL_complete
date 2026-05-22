from dash import Dash, html, dcc
import pandas as pd

import mysql.connector

conn= mysql.connector.connect(
    host='localhost',
    user='root',
    password='0777',
    database='connect_project'
)

connnection = conn.cursor()

query = "SELECT * FROM linkedin_connections"
connnection.execute(query)

results = connnection.fetchall()

# print(results)

df= pd.DataFrame(results, columns=['First_Name', 'Last_Name', 'URL', 'Email_Address', 'Company', 'Updated_Company', 'Position', 'Base_Role', 'Seniority', 'Connected_On', 'Owner'])


print(df)








app = Dash(__name__)

app.layout = html.Div([
    html.H1('Dash App'),
    dcc.Graph(id='graph')
])

if __name__ == '__main__':
    app.run(debug=True, port=8050)