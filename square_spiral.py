import turtle

if __name__ == '__main__':
    turtle.setup(width=800, height=800)

    bob = turtle.Turtle(shape='turtle')
    bob.color('orange')

    # Drawing a square spiral
    bob.speed(2000)
    for i in range(500):

        bob.forward(i)
        bob.left(91)

    turtle.exitonclick()
