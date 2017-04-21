import turtle

window = turtle.Screen()
window.bgcolor("white")

def draw_tri(some_turtle, length, angle):
    for i in range(1, 4):
        some_turtle.forward(length)
        some_turtle.right(angle)

def draw_flower(length, angle):
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("blue")
    brad.speed(100)
    brad.right(-90)
    brad.forward(300)
    for i in range(1, 25):
        draw_tri(brad, length, angle)
        brad.right(15)

draw_flower(100, 200)
draw_flower(50, 120)
draw_flower(150, 120)

window.exitonclick()
