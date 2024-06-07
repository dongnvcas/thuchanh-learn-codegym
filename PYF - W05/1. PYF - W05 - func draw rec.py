import turtle
import random

t = turtle.Turtle()
t.hideturtle()

def draw_rec(width = 100, lenght = 200, color = "red"):
    t.fillcolor(color)
    t.begin_fill()
    for i in range(2):
        t.fd(width)
        t.lt(90)
        t.fd(lenght)
        t.lt(90)
    t.end_fill()
def go_to(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()


draw_rec(50,100,"blue")

go_to(-50,0)
draw_rec(50,100,"yellow")

go_to(0,-100)
draw_rec(50,100,"red")

go_to(-50,-100)
draw_rec(50,100,"green")

go_to(50,-100)
draw_rec(100,100,"orange")
# vẽ cửa sổ
go_to(20,30)
draw_rec(10,30,"white")

go_to(-30,30)
draw_rec(10,30,"white")

go_to(-30,-60)
draw_rec(10,30,"white")

go_to(20,-60)
draw_rec(10,30,"white")

go_to(70,-100)
draw_rec(20,60,"grey")

go_to(90,-100)
draw_rec(20,60,"black")

turtle.done()
