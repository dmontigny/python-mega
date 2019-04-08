# https://www.udemy.com/the-python-mega-course/learn/lecture/4775808#content
"""This module plots the time of motion detected"""

from vid_cap import df
from bokeh.plotting import figure, show, output_file

p = figure(x_axis_type='datetime', height=100, width=500, sizing_mode='scale_width',
           title="Motion Graph")

q = p.quad(left=df["Start"], right=df["End"], bottom=0, top=1)

output_file("motion.html")
show(p)
