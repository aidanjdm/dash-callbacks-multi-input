import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State

########### Define your variables ######

myheading1='Multiple Inputs'
tabtitle = 'states'
population_list=['low population', 'high population']
area_list=['small area', 'large area']
sourceurl = 'https://dash.plot.ly/getting-started-part-2'
githublink = 'https://github.com/aidanjdm/dash-callbacks-multi-input'


########## Set up the chart

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout

app.layout = html.Div(children=[
    html.H1(myheading1),
    html.Div([
        html.Div([
            dcc.RadioItems(
                id='pick-a-pop',
                options=[
                        {'label':population_list[0], 'value':population_list[0]},
                        {'label':population_list[1], 'value':population_list[1]},
                        ],
                value='choose',
                ),
        ],className='two columns'),
        html.Div([
            dcc.RadioItems(
                id='pick-an-area',
                options=[
                        {'label':area_list[0], 'value':area_list[0]},
                        {'label':area_list[1], 'value':area_list[1]},
                        ],
                value='one',
                ),
        ],className='two columns'),
        html.Div([
            html.Div(id='your_output_here', children=''),
        ],className='eight columns'),
    ],className='twelve columns'),
    html.Br(),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A("Info on Callbacks", href=sourceurl),
    ]
)

########## Define Callback

@app.callback(Output('your_output_here', 'children'),
              [Input('pick-a-pop', 'value'),
               Input('pick-an-area', 'value')])
def radio_results(pop_selection, area_selection):
    image_you_chose=f'{pop_selection}-{area_selection}.jpg'
    return html.Img(src=app.get_asset_url(image_you_chose), style={'width': 'auto', 'height': 'auto'}),

############ Deploy
if __name__ == '__main__':
    app.run_server()
