from random import randint
import plotly.express as px

dice = []

count = []

for i in range(0,100):
     dice1 = randint(1,6)
     dice2 = randint(1,6)
     dice.append(dice1 + dice2)
     count.append(i)

fig = px.bar(x=dice, y=count)
fig.show()
