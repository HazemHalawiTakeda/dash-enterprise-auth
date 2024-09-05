from dash import Dash, dcc, html, Input, Output
import dash_design_kit as ddk
import dash_enterprise_auth
import plotly.express as px
import json

app = Dash(__name__)
server = app.server

df = px.data.iris()

app.layout = ddk.App([
    ddk.Header([
        ddk.Logo(src=app.get_asset_url('logo.svg'), style={
            'maxHeight': '100px',
            'width': 'auto'
        }),
        ddk.Title('Weekly Analytics'),
        ddk.Menu([
            html.Div(id='auth-username', style={'lineHeight': '60px'}),
        ])
    ]),
    ddk.Card([
        ddk.CardHeader(dcc.Dropdown(
            options=[{'label': i, 'value': i} for i in df.columns],
            value=df.columns[0],
        id='auth-dropdown')),
        html.Div(id='auth-output')
    ], width=50),
    ddk.Card(width=50, children=html.Pre(id='auth-userdata'))
])

print(1)

@app.callback([
    Output('auth-username', 'children'),
    Output('auth-userdata', 'children'),
    Output('auth-output', 'children')],
    [Input('auth-dropdown', 'value')])
def display_output(value):
    username = dash_enterprise_auth.get_username()
    userdata = dash_enterprise_auth.get_user_data()
    return [username, json.dumps(userdata, indent=2), html.Div([
        'Chart created by {}'.format(username),
        ddk.Graph(figure=px.scatter(df, x=df.index, y=value))
    ])]


if __name__ == '__main__':
    app.run(debug=True)
