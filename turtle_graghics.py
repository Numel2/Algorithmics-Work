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


if __name__ == '__main__':
    long_shape()
