#!/usr/bin/env python

from plotnine import *
from plotnine.data import mtcars

print("Dades `mtcars`:")
print(mtcars)

def regular_plot():
    plot = (
        ggplot(mtcars)
        + aes("wt", "mpg", color="factor(gear)")
        + geom_point()
        + labs(title="Consum (wt) vs Pes (mpg)",
               x="Pes en lliures",
               y="Consum en milles per galó",
               color="Nombre de marxes"
        )
        + theme_dark()
    )

    plot.show()

def line_plot():
    line_plot = (
        ggplot(mtcars)
        + aes(x='wt', y='mpg', color='factor(gear)')
        + geom_line()
    )

    line_plot.show()

def bar_plot():
    bar_plot = (
        ggplot(mtcars)
        + aes(x='factor(cyl)', fill='factor(gear)')
        + geom_bar()
    )

    bar_plot.show()

def facet_wrap_plot():
    facet_plot = (
        ggplot(mtcars)
        + aes("wt", "mpg", color="factor(gear)")
        + geom_point()
        + facet_wrap("gear")
        + labs(title="Consum (wt) vs Pes (mpg)",
               x="Pes en lliures",
               y="Consum en milles per galó",
               color="Nombre de marxes"
        )
    )

    facet_plot.show()

def facet_grid_plot():
    facet_grid_plot = (
        ggplot(mtcars)
        + aes("wt", "mpg", color="factor(gear)")
        + geom_point()
        + facet_grid("gear", "cyl", labeller="label_both")
        + labs(title="Consum (wt) vs Pes (mpg)",
               x="Pes en lliures",
               y="Consum en milles per galó",
               color="Nombre de marxes"
        )
    )

    facet_grid_plot.show()

# simple_plot()
# line_plot()
# bar_plot()
# facet_wrap_plot()
facet_grid_plot()
