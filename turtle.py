import turtle

turtle.goto(150, 150)


def move(side_length):
    turtle.left(90)
    turtle.forward(side_length)


def drawSquare(side_length):
    move(side_length)
    move(side_length)
    move(side_length)
    move(side_length)


def drawSquareColored(color, side_length):
    turtle.color(color)
    turtle.begin_fill()
    move(side_length)
    move(side_length)
    move(side_length)
    move(side_length)
    turtle.end_fill()


drawSquareColored("red", 100)
