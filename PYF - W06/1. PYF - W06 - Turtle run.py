import turtle as t
import random
import datetime

# Set up the screen
screen = t.Screen()
screen.setup(height=500, width=600)

# Create a pen turtle to draw the track
pen = t.Turtle(visible=False)
pen.penup()
pen.speed(0)
pen.goto(-250, 200)

# Draw left side milestones
for i in range(21):
    pen.write(i)
    pen.forward(25)

# Draw dashed lines and right side milestones
x = -250
pen.goto(-250, 200)
pen.right(90)
for i in range(21):
    for j in range(10):
        pen.pendown()
        pen.forward(20)
        pen.penup()
        pen.forward(10)
    pen.penup()
    pen.forward(5)
    pen.write(i)
    pen.goto(x + (i + 1) * 25, 200)

# Create turtles for the race
all_turtles = []
y_position = [160, 100, 40, -20]
colors = ['red', 'green', 'blue', 'black']
for turtle in range(4):
    turtles = t.Turtle(shape="turtle")
    turtles.penup()
    turtles.goto(x=-250, y=y_position[turtle])
    turtles.color(colors[turtle])
    all_turtles.append(turtles)

# Function to move turtles randomly
def random_walk(turtles):
    global run, start_time, winning_color, best_time
    for turtle in turtles:
        turtle.forward(random.randint(1, 10))
        if turtle.xcor() > 250:
            run = False
            winning_color = turtle.pencolor()
            end_time = datetime.datetime.now()
            elapsed_time = (end_time - start_time).total_seconds()
            best_time = min(best_time, elapsed_time)

# Initialize race parameters
run = True
winning_color = None
best_time = float('inf')
start_time = datetime.datetime.now()

# Run the race
while run:
    random_walk(all_turtles)

# Display the winner and time
pen.goto(0, 0)
pen.hideturtle()
pen.penup()
pen.goto(-150, -5)
pen.pendown()
pen.lt(90)
pen.fillcolor('white')
pen.begin_fill()
for _ in range(2):
    pen.forward(300)
    pen.lt(90)
    pen.forward(60)
    pen.lt(90)
pen.end_fill()
pen.penup()
pen.goto(0, 0)
pen.write(f"Winner: {winning_color}\nBest Time: {best_time:.2f} seconds", align="center", font=("Arial", 16, "normal"))

# Exit on click
screen.exitonclick()
