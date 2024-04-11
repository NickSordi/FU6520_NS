from dash import Dash, html, dash_table
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

# Load the CSV data
data = pd.read_csv('CreditCardData.csv')

# Create the Dash app
app = Dash(__name__)

# Define the layout
app.layout = html.Div([
    html.Div(children = 'My first app with data'),
    dash_table.DataTable(data=data.to_dict('records'), page_size=10)
])


if __name__ == '__main__':
    app.run_server(debug=True)