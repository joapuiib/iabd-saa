#!/usr/bin/env python

from plotnine import *
import pandas as pd
from pandas.api.types import CategoricalDtype
import numpy

df = pd.read_csv('../athlete_events.csv')
print(numpy.sort(df['Year'].unique()))


"""
# Exercici 3.a
Crea un gràfic de línies que mostre com ha evolucionat la quantitat de
participants als Jocs Olímpics al llarg dels anys similar al següent:
"""
plot = (
    ggplot(df)
    + aes(x='Year')
    + geom_point(stat='count', color='blue')
    + geom_line(stat='count', color='red')
    + scale_x_continuous(breaks=df['Year'].unique())
    + theme(axis_text_x=element_text(rotation=45, hjust=1))

)

plot.show()
