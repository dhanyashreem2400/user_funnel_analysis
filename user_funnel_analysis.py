import plotly.graph_objects as go
import plotly.io as pio
import pandas

# Read csv file
df = pandas.read_csv('/content/user_data.csv')
ds = pandas.DataFrame(df)
print(df)

#define the funnel stages
stages = ['homepage', 'product_page', 'cart', 'checkout', 'purchase']

#calculate the number of users and conversions for each stage
users = []
conversions = []

for i in stages:
    curr_user = df[df['stage'] == i] # It creates a new DataFrame curr_users that only contains rows where the value in the 'stage' column matches the current stage in the loop
    users.append(len(curr_user))
    conversions.append(curr_user['conversion'].sum()) #sum() gives the the count of only True values in conversion,hence no of conversions can be calculated

print("No of users",users)
print("No of Conversions",conversions)

#create a funnel chart
fig = go.Figure(go.Funnel(
    y=stages,
    x=users,
    textposition='inside',
    name='Users',
    marker = {"color": ["pink", "lightgreen", "violet", "teal", "black"]}
))

#Customize the appearance of each trace using any relevant arguments
fig.add_trace(go.Funnel(
    y=stages,
    x=conversions,
    textposition='inside',
    textinfo='value',
    name='Conversions',
    marker = {"color": ["turquoise", "yellow", "green", "blue", "orange"]}
))

fig.update_layout(
    title_text='User Funnel Analysis',
    title_x=0.5,
    template='plotly_white',
    height=800,
    width=1200,
    funnelmode='stack'
)

fig.show()