import turtle

screen = turtle.Screen()
screen.bgcolor("lightblue")

artist = turtle.Turtle()

for i in range(3):
    artist.forward(100)
    artist.left(120)

artist.penup()
artist.right(150)
artist.forward(60)
artist.pendown()
artist.color("yellow")

for i in range(2):
    artist.forward(150)
    artist.left(90)
    artist.forward(100)
    artist.left(90)

artist.penup()
artist.right(150)
artist.forward(50)
artist.pendown()
artist.color("orange")

for i in range(6):
    artist.forward(100)
    artist.left(60)

