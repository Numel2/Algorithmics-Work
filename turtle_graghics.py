from turtle import *
from time import sleep
speed(0)

def tanisha_shape():
    x = 200
    for i in range(20):
        forward(x)
        right(130)
        x = x-10

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
    goto(-40,110)
    pendown()
    circle(10)



if __name__ == '__main__':
    oliver_shape()