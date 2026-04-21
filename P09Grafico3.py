# Kimberly Medina Ríos
from turtle import *
from colorsys import *

bgcolor("black")
speed(0)
width(2)

h = 0
for i in range(360):
    color(hsv_to_rgb(h, 1, 1))
    h += 0.002
    circle(100)
    right(10)

hideturtle()
done()