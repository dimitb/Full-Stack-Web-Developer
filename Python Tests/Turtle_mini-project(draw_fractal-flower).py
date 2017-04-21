import turtle

def draw_fractal():
    window = turtle.Screen()
    window.bgcolor("white")

    moriarty = turtle.Turtle()
    moriarty.shape("arrow")
    moriarty.color("red")
    moriarty.speed(50)
    for i in range (1, 74):
        moriarty.left(5)
        moriarty.circle(100)
        
    window.exitonclick()

draw_fractal()
