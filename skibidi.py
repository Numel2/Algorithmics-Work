from turtle import *
from time import sleep


def nonagon():
    for i in range(9):
        forward(100)
        right(40)


def triangle():
    for i in range(3):
        forward(100)
        left(120)


def pentagon():
    for i in range(5):
        forward(100)
        right(72)


def heptagon():
    left()
    for i in range(7):
        forward(100)
        left(51.43)


pentagon()
triangle()
sleep(3)
heptagon()
