# Kimberly Medina Ríos
from turtle import *
from colorsys import *

bgcolor("black")
speed(0)

h = 0
for i in range(100):
    color(hsv_to_rgb(h, 1, 1))
    h += 0.01
    penup()
    forward(i * 5)
    pendown()
    circle(20)
    right(30)

hideturtle()
done()