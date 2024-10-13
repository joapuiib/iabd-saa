#!/usr/bin/env python

from plotnine import ggplot, geom_point, aes
from plotnine.data import mtcars

print("Dades `mtcars`:")
print(mtcars)

plot = (
    ggplot(mtcars)
    + aes("wt", "mpg", color="factor(gear)")
    + geom_point()
)

plot.show()
