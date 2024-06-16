import pandas as pd
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px

spaceX_df =  pd.read_csv(r"C:\Users\Mustafa yassin\Downloads\spacex_launch_geo (1).csv")

app = dash.Dash(__name__)

app.layout = html.Div(children=[html.H1('SpaceX Launch Records Dashboard',style={'textAlign': 'center', 'color': '#503D36', 'font-size': 40}),
                                html.Br(),
                                html.Br(),
                                dcc.Dropdown(id='site-dropdown',
                                options=[
                                      {'label': 'All Sites',   'value': 'ALL'},
                                      {'label': 'CCAFS LC-40', 'value': 'CCAFS LC-40'},
                                      {'label': 'VAFB SLC-4E', 'value': 'VAFB SLC-4E'},
                                      {'label': 'KSC LC-39A',  'value':'KSC LC-39A'},
                                      {'label': 'CCAFS SLC-40','value': 'CCAFS SLC-40'},
                                        ],
                                
                value='ALL',
                placeholder="place holder here",
                searchable=True
                ),
                                html.Br(),
                                html.Br(),
                                
                                
                                html.Div([

                                        html.Div(dcc.Graph(id='success-pie-chart'),style={'height':'45px', 'font-size': 50})
                                        
                                         ]),
                                
                                html.Br(),html.Br(),
                                html.Br(),html.Br(),
                                html.Br(),html.Br(),
                                html.Br(),html.Br(),
                                html.Br(),html.Br(),
                                html.Br(),html.Br(),
                                html.Br(),html.Br(),
                                html.Br(),html.Br(),
                                html.Br(),html.Br(),
                                html.Br(),html.Br(),
                                
                                
                                html.Div ([
                                    
                                        html.Div(dcc.RangeSlider(id ='payload-slider', min = 0, max = 10000,step =2500, value= [0,10000]))
                                
                                          ]),
                                 
                                html.Div([

                                        html.Div(dcc.Graph(id='success-payload-scatter-chart'),style={'height':'45px', 'font-size': 50})
                                        
                                         ])
])

@app.callback(Output(component_id='success-pie-chart', component_property='figure'),
              Input(component_id='site-dropdown', component_property='value'))



def get_pie_chart(entered_site):
    new_data = spaceX_df
    if entered_site == 'ALL':
        fig = px.pie(spaceX_df, values='class',
                     names='Launch Site', title='Total Success Launches By All Site')
        return fig
    else :
        if entered_site =="CCAFS LC-40":
            new_data = spaceX_df[spaceX_df['Launch Site'] =='CCAFS LC-40' ]
            gb_data = new_data.groupby(['Launch Site'])['class'].value_counts().reset_index()
            fig1 = px.pie(gb_data, values='count',
                          names='class',labels=['success','faild'],title=f'Total Success Launches By {entered_site} Site')
            return fig1
        elif entered_site =="VAFB SLC-4E":
            new_data = spaceX_df[spaceX_df['Launch Site'] =='VAFB SLC-4E' ]
            gb_data2 = new_data.groupby(['Launch Site'])['class'].value_counts().reset_index()
            fig2 = px.pie(gb_data2, values='count', 
                          names='class', title=f'Total Success Launches By {entered_site} Site')
            return fig2
        
        elif entered_site =="KSC LC-39A":
            new_data = spaceX_df[spaceX_df['Launch Site'] =='KSC LC-39A' ]
            gb_data3 = new_data.groupby(['Launch Site'])['class'].value_counts().reset_index()
            fig3 = px.pie(gb_data3, values='count', 
                          names='class', title=f'Total Success Launches By {entered_site} Site')
            return fig3
        
        
        elif entered_site =="CCAFS SLC-40":
            new_data = spaceX_df[spaceX_df['Launch Site'] =='CCAFS SLC-40' ]
            gb_data4 = new_data.groupby(['Launch Site'])['class'].value_counts().reset_index()
            fig4 = px.pie(gb_data4, values='count', 
                          names='class', title=f'Total Success Launches By {entered_site} Site')
            return fig4



@app.callback(Output(component_id='success-payload-scatter-chart', component_property='figure'),
              Input(component_id='site-dropdown', component_property='value'),
              Input(component_id='payload-slider', component_property='value'))
       
     
def get_scatter_chart(entered_site,eneterd_range):

    new_data = spaceX_df
    if entered_site == 'ALL':
        new_data = spaceX_df[spaceX_df['Payload Mass (kg)'].between(eneterd_range[0],eneterd_range[1])]
        scatter = px.scatter(new_data,x = 'Payload Mass (kg)', y = 'class',color='Booster Version',title=f"Correlation Between Payload And Success For All Sites")
        return scatter
    else :
        if entered_site =="CCAFS LC-40" :
            new_data =spaceX_df[(spaceX_df['Launch Site'] =='CCAFS LC-40') & (spaceX_df['Payload Mass (kg)'].between(eneterd_range[0],eneterd_range[1]))]
            scatter1 = px.scatter(new_data,x = 'Payload Mass (kg)', y = 'class',color='Booster Version',title=f"Correlation Between Payload And Success For {entered_site} Site ")
            return scatter1
        elif entered_site =="VAFB SLC-4E":
            new_data = spaceX_df[(spaceX_df['Launch Site'] =='VAFB SLC-4E') & (spaceX_df['Payload Mass (kg)'].between(eneterd_range[0],eneterd_range[1]))]
            scatter2 = px.scatter(new_data,x = 'Payload Mass (kg)', y = 'class',color='Booster Version',title=f"Correlation Between Payload And Success For {entered_site} Site")
            return scatter2
        
        elif entered_site =="KSC LC-39A":
            new_data = spaceX_df[(spaceX_df['Launch Site'] =='KSC LC-39A') & (spaceX_df['Payload Mass (kg)'].between(eneterd_range[0],eneterd_range[1]))]
            scatter3 = px.scatter(new_data,x = 'Payload Mass (kg)', y = 'class',color='Booster Version',title=f"Correlation Between Payload And Success For {entered_site} Site ")
            return scatter3
         
        elif entered_site =="CCAFS SLC-40":
            new_data = spaceX_df[(spaceX_df['Launch Site'] =='CCAFS SLC-40') & (spaceX_df['Payload Mass (kg)'].between(eneterd_range[0],eneterd_range[1]))]
            scatter4 = px.scatter(new_data,x = 'Payload Mass (kg)', y = 'class',color='Booster Version', title=f"Correlation Between Payload And Success For {entered_site} Site ")
            return scatter4
       
    

if __name__ == '__main__':
    app.run_server(port = 2226)