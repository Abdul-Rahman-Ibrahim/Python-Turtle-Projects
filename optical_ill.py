import turtle

# Set up the turtle
t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# Define the size of the tiles
tile_size = 20

# Draw the tiles
for row in range(8):
    for col in range(8):
        # Calculate the position of the tile
        x = col * tile_size + (row % 2) * tile_size / 2 - 80
        y = row * tile_size - 80

        # Draw the tile
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.color("black" if (col + row) % 2 == 0 else "white")
        t.begin_fill()
        for i in range(4):
            t.forward(tile_size)
            t.right(90)
        t.end_fill()

    # Draw the mortar line
    t.penup()
    t.goto(-80, (row + 1) * tile_size - 80)
    t.pendown()
    t.color("gray")
    t.pensize(3)
    t.forward(8 * tile_size)

# Keep the window open
turtle.mainloop()
