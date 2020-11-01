#
# Testing of plotnine in PyCharm
#
from plotnine import *
import pandas as pd
import matplotlib.pyplot as plt
gapminder = pd.read_csv("gapminder-FiveYearData.csv")
print(gapminder.head())
#   Plot without legends
#
g = (ggplot(gapminder, aes(x='lifeExp', y='gdpPercap')) +
     geom_point() + ggtitle('Plot 1 - No legends'))
g.draw()
plt.show()
#   Plot with legends
#
g = (ggplot(gapminder, aes(x='gdpPercap', y='lifeExp', size='pop')) +
     geom_point(aes(color='continent'), alpha = 0.5) +
     geom_smooth(se=False, method="loess", color="grey") +
     ggtitle('Plot 2 - With legends'))
g.draw()
plt.show()

