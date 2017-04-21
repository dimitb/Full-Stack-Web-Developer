import turtle

def draw_shapes():
    window = turtle.Screen()
    window.bgcolor("white")

    brad = turtle.Turtle()
    brad.shape("square")
    brad.color("blue")
    i = 0

    while (i < 4):
        brad.forward(100)
        brad.right(90)
        i = i + 1

    # sally = turtle.Turtle()
    # sally.shape("circle")
    # sally.color("red")
    # x = 0

    # while (x < 3):
        # sally.right(120)
        # sally.forward(110)
        # x = x + 1

    # angie = turtle.Turtle()
    # angie.circle(75)
    # angie.shape("arrow")
    # angie.color("brown")

    window.exitonclick()

draw_shapes()
