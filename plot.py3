# Emma Akbari
import plotly.express as px # graphing library
import pandas as pd # geospatial data
import dash # framework for building analytical web apps
import dash_core_components as dcc
import dash_html_components as html
# data from https://www.gapminder.org/data/
df = pd.read_csv('co2_intensity_economic.csv')
fig = px.line(df, x="year", y="co2", color="country", title="CO2 Intensity of Economic Output (kg CO2 per 2011 PPP $ of GDP)")

styles = { 'title': {'textAlign': 'center',
        'font-family': 'tahoma',
        'background-color': 'rgb(255,255,255)',
        'color': 'rgb(0,0,31)'} }

app = dash.Dash()
app.layout = html.Div([
    html.H1("Comparing Economic CO2 Emissions: USA and China", style = styles['title'] ),
    #line graph
    dcc.Graph(figure = fig),
])

app.run_server(debug=True, use_reloader=True)  # Turn off reloader if inside Jupyter