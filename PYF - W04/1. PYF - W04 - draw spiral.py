import turtle

t = turtle.Turtle()
n = int(input("Please input the distance you want to draw: "))
i = 0

while i <= n:
 t.circle(i,20)
 i += 1