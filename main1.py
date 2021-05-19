from random import randint
import plotly.figure_factory as pff

dice = []

for i in range(0,100):
     dice1 = randint(1,6)
     dice2 = randint(1,6)
     dice.append(dice1 + dice2)

fig = pff.create_distplot([dice], ['result'])
fig.show()
