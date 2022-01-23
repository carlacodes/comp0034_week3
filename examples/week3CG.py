import plotly.express as px
import plotly.graph_objects as go
import plotly
import pandas as pd

df = pd.DataFrame({'a': [1, 2, 3, 4],
                   'b': [6, 7, 8, 9]})


#take example dataframe and let's plot it using plotly express
df = px.data.iris()
df3=df
fig2 = px.scatter(df, x="sepal_width", y="sepal_length", color="species", title='Iris Length Over Species'  , labels={
                     "sepal_length": "Sepal Length (cm)",
                     "sepal_width": "Sepal Width (cm)",
                     "species": "Species of Iris"})
fig2.show()

##now how about a pie chart?

df2 = px.data.gapminder().query("year == 2007").query("continent == 'Europe'")
df2.loc[df2['pop'] < 2.e6, 'country'] = 'Other countries' # Represent only large countries
fig = px.pie(df2, values='pop', names='country', title='Population of European continent')
fig.show()
plotly.offline.plot(fig, filename='file.html')


figTreeMap = go.Figure(go.Treemap(
    labels = ["Eve","Cain", "Seth", "Enos", "Noam", "Abel", "Awan", "Enoch", "Azura"],
    parents = ["", "Eve", "Eve", "Seth", "Seth", "Eve", "Eve", "Awan", "Eve"],
    root_color="lightgrey"
))

figTreeMap.update_layout(margin = dict(t=50, l=25, r=25, b=25))
figTreeMap.show()