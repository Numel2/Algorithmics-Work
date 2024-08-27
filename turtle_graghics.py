from turtle import *
from time import sleep

speed(0)


def tanisha_shape():
    x = 200
    for i in range(20):
        forward(x)
        right(130)
        x = x - 10


def oliver_shape():
    penup()
    goto(0, 0)
    pendown()
    circle(100)
    penup()
    goto(40, 110)
    pendown()
    circle(10)
    penup()
    goto(-40, 110)
    pendown()
    circle(10)


def laila():
    y = 150
    for i in range(100):
        forward(y)
        left(170)
        y -= 2


def long_shape():
    goto(-300, -300)
    for i in range(20):
        triangle()
        square()
        forward(240)
        left(30)


def triangle():
    for i in range(3):
        forward(100)
        left(120)


def square():
    for i in range(4):
        forward(150)
        left(90)


def tiffany_shape():
    x = 144
    for i in range(20):
        forward(100)
        left(x)
        right(1)
        forward(10)


def keyanna_shape():
    x = 150
    penup()
    goto(0, -250)
    pendown()
    for i in range(150):
        forward(x)
        left(40)
        x -= 1


def david_shape():
    for i in range(3):
        circle(90, 180)
        right(60)
    sleep(4)


def rokhans_maze():
    right(90)
    forward(60)
    left(90)
    forward(40)
    right(90)
    forward(40)
    right(90)
    forward(40)
    left(90)
    forward(80)
    right(90)
    forward(40)
    left(90)
    forward(30)
    left(90)
    forward(30)


if __name__ == '__main__':
    rokhans_maze()
