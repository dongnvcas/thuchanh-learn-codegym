import turtle
import random

t = turtle.Turtle()
t.speed(0)
# method to draw ellipse
def draw(rad):
    i = 1
    # rad --> radius of arc
    while i < 3:
        
        # two arcs
        t.circle(rad,90)
        t.circle(rad//2,90)
        i += 1

# Main section
# tilt the shape to negative 45
t.seth(-45)
draw(100)


a = 0
while a < 37:
    t.pencolor(random.choice(["red", "yellow", "blue", "green", "purple", "grey"]))
    draw(100)
    a += 1
    t.seth(-45 - a*10)