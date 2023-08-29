import pandas
import plotly.graph_objects as go
import plotly.io as pio
import plotly.express as px

# Read csv file
df = pandas.read_csv('/content/user_data.csv')
ds = pandas.DataFrame(df)
print(df)

#define the funnel stages
Funnel_Stages = ['homepage', 'product_page', 'cart', 'checkout', 'purchase']

#calculate the number of users and conversions for each stage
no_of_users = []
no_of_conversions = []

for stages in Funnel_Stages:
    stage_users = df[df['stage'] == stages ]  # It creates a new DataFrame stage_users that only contains rows where the value in the 'stage' column matches the current stage in the loop
    no_of_users.append(len(stage_users))
    no_of_conversions.append(stage_users['conversion'].sum()) # sum() gives the the count of only True values in conversion,hence no of conversions can be calculated

print("Number of Users : ",no_of_users)
print("Number of Conversions : ",no_of_conversions)

#create a funnel chart
fig = go.Figure(go.Funnel(
    y=Funnel_Stages,
    x=no_of_users,
    textposition='inside',
    name='Users',
    marker={'color':'lightblue'}))

pio.templates.default = "plotly_white"

#Adding the trace using any relevant arguments
fig.add_trace(go.Funnel(
    y=Funnel_Stages,
    x=no_of_conversions,
    textposition='inside',
    textinfo='value',
    name='Conversions',
    marker={'color':'blue'}))

#Customize the appearance of the chart
fig.update_layout(
    title_text='User Funnel Analysis',
    title_x=0.5,
    height=800,
    width=1300,
    funnelmode='stack',
    legend=dict(orientation='h',y=0.001,x=0.43))

fig.show()
