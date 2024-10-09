import turtle

screen = turtle.Screen()
screen.title("Turtle Drowing")
screen.bgcolor("lightblue")

screen.bgpic("img.png")
t=turtle.Turtle()

t.penup()
t.goto(0,-100)
t.pendown()
t.fillcolor("white")
t.begin_fill()
t.circle(100)
t.end_fill()

t.hideturtle()
turtle.done()