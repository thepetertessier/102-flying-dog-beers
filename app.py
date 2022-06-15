# This is Peter's website for the ML Workshop

import dash
from dash import html
from dash import dcc
import plotly.graph_objs as go

########### Define your variables
beers=['Elon Musk', 'Bernard Arnault & family', 'Jeff Bezos', 'Bill']
ibu_values=[219, 177, 158, 129]
abv_values=[211.2, 139.1, 131.5, 121.8]
color1='darkred'
color2='blue'
mytitle='Forbes vs Wikipedia 06/15/2022'
tabtitle='billionaires!'
myheading='Four Richest People according to different sources'
label1='Forbes'
label2='Wikipedia'
githublink='https://github.com/thepetertessier/102-flying-dog-beers'
sourceurl='https://en.wikipedia.org/wiki/The_World%27s_Billionaires'

########### Set up the chart
bitterness = go.Bar(
    x=beers,
    y=ibu_values,
    name=label1,
    marker={'color':color1}
)
alcohol = go.Bar(
    x=beers,
    y=abv_values,
    name=label2,
    marker={'color':color2}
)

beer_data = [bitterness, alcohol]
beer_layout = go.Layout(
    barmode='group',
    title = mytitle
)

beer_fig = go.Figure(data=beer_data, layout=beer_layout)


########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout
app.layout = html.Div(children=[
    html.H1(myheading),
    dcc.Graph(
        id='flyingdog',
        figure=beer_fig
    ),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A('Data Source', href=sourceurl),
    ]
)

if __name__ == '__main__':
    app.run_server()
