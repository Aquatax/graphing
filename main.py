from turtle import Turtle, Screen
import math
from formula import Math

# formulaa = input("Equation:")
screen = Screen()
painter = Turtle()

# ------------------------
# Screen Properties
# screenscale = 2 # 2 is reccommended
screenxscale = 2
screenyscale = 2
screen.bgcolor("black")

# Grid Properties
height = 20
width = 20
axis_color = "gray"
grid_color = "dark gray"
gridplacementx = 5
gridplacementy = 5

# Integers Only
axis_Width = 5
grid_Width = 1

# Settings
# 0 for Medium Speed, High accuracy, not fun to watch   (Average 7 Seconds)
# 1 for Instant, Very Low accuracy, fun to watch (Not Recommended)
# 2 for High Speed, Low accuracy, fun viewing experience (Recommended)
# 3 for manual settings (options under settings. Having 1 or 2 will override these settings)
setting = 2
screen.tracer(n=100) #Reccommended 100
speed = 1 #Reccommended 0.025  Lower number, higher accuracy (eg. 0.0000025 is more accurate than 0.025)
painter.pensize(10) #reccommended 10

table_size = 0.25


painter.pencolor("light blue")
painter.pensize(1)  # Integer Only
# ------------------------


scalex = screenxscale * 10 + 10
scaley = screenyscale * 10 + 10

gridmaker = Turtle()
gridmaker.speed(0)
gridmaker.pensize(axis_Width)
gridmaker.hideturtle()
gridmaker.pencolor(axis_color)
gridmaker.goto(-width / 2 * scalex, 0)
gridmaker.goto(width / 2 * scalex, 0)
gridmaker.penup()
gridmaker.goto(0, height / 2 * scaley)
gridmaker.pendown()
gridmaker.goto(0, -height / 2 * scaley)

gridmaker.pensize(grid_Width)
gridmaker.pencolor(grid_color)
gridmaker.penup()
gridx = 0
while gridx < width / 2:
    gridx += gridplacementx
    gridmaker.penup()
    gridmaker.goto(gridx * scalex, 0)
    gridmaker.goto(gridmaker.xcor(), height / 2 * scaley)
    gridmaker.pendown()
    gridmaker.goto(gridmaker.xcor(), -height / 2 * scaley)
    gridmaker.penup()
gridx = 0
while gridx > -width / 2:
    gridx -= gridplacementx
    gridmaker.penup()
    gridmaker.goto(gridx * scalex, 0)
    gridmaker.goto(gridmaker.xcor(), height / 2 * scaley)
    gridmaker.pendown()
    gridmaker.goto(gridmaker.xcor(), -height / 2 * scaley)
    gridmaker.penup()

gridy = 0
while gridy < height / 2:
    gridy += gridplacementy
    gridmaker.penup()
    gridmaker.goto(0, gridy * scaley)
    gridmaker.goto(width / 2 * scalex, gridmaker.ycor())
    gridmaker.pendown()
    gridmaker.goto(-width / 2 * scalex, gridmaker.ycor())
    gridmaker.penup()

gridy = 0
while gridy > -height / 2:
    gridy -= gridplacementy
    gridmaker.penup()
    gridmaker.goto(0, gridy * scaley)
    gridmaker.goto(width / 2 * scalex, gridmaker.ycor())
    gridmaker.pendown()
    gridmaker.goto(-width / 2 * scalex, gridmaker.ycor())
    gridmaker.penup()

    gridmaker.pendown()

screen.setup(width * 15 * screenxscale, height * 15 * screenyscale)





def forumla(x):

    functiona = Math(formulaa, x)
    newy = functiona.answer
    if newy == "NaN":
        return 42424242
    elif isinstance(newy, complex):
        return 32323232
    else:
        try:
            value = float(newy)
            return newy
        except:
            return 22222222
# formulaa = input("Equation:")
listofpens = []
startx = -width / 2

# for x in range(0, 20):
#     myturtle = Turtle()
#     myturtle.penup()
#     myturtle.pencolor(pencolor)
#     myturtle.pensize(pensize)
#     starty = forumla(startx)
#     myturtle.speed(0)
#     myturtle.goto(startx * scalex, starty * scaley)
#     startx += width / 20
#     myturtle.hideturtle()
# screen.update()

if setting == 0:
    screen.tracer(n=10000)
    speed = 0.00025
    painter.pensize(1)

elif setting == 1:
    speed = 0.01
    painter.pensize(10)

elif setting == 2:
    speed = 0.0025
    painter.pensize(10)



while True:
    formulaa = input("Equation:")
    if formulaa == "exit":
        screen.exitonclick()
    elif formulaa == "clear":
        painter.clear()
    else:
        startx = -width / 2
        x = startx
        painter.penup()
        painter.penup()
        painter.speed(0)
        print(f"DEBUG FOrmula={formulaa}")
        starty = forumla(startx)
        painter.goto(x * scalex, starty * scaley)
        # painter.clear()
        while x <= abs(startx):
            x += speed
            y = forumla(x)

            if round(x % table_size, 3) == 0:

                if y == 32323232:
                    print(f"{round(x, 5)}, Imaginary")
                elif y == 42424242:
                    print(f"{round(x, 5)}, NaN")
                else:
                    print(f"{round(x, 5)}, {round(y, 5)}")

            if y > height / 2 + 5 or y < -height / 2 - 5:
                painter.penup()
                painter.speed(0)
            else:
                painter.goto(x * scalex, y * scaley)
                painter.pendown()
        painter.penup()
        # screen.update()
# screen.exitonclick()
