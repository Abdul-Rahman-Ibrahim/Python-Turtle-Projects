import turtle
import time

# Set up the turtle
t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# Define the colors
colors = ["#F25022", "#7FBA00", "#00A4EF", "#FFB900"]

# Draw the squares
start_time = time.time()
for i in range(4):
    t.penup()
    t.goto((i % 2) * 100 - 50, (i // 2) * -100 + 50)
    t.pendown()
    t.color(colors[i])
    t.begin_fill()
    for j in range(4):
        t.forward(90)
        t.right(90)
    t.end_fill()
    time.sleep((5 - (time.time() - start_time)) / (4 - i))

# Keep the window open
turtle.mainloop()
