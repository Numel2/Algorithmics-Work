import turtle
import random

t = turtle.Turtle()
t.speed(5)

tw = 52


def skibidi():
    for x in range(-7, 10):
        for y in range(-7, 10):
            tw = 52
            t.penup()
            t.goto(x * tw, y * tw)
            t.setheading(0)
            t.pendown()
            colour1 = random.randint(0, 256)
            colour2 = random.randint(0, 256)
            colour3 = random.randint(0, 256)

            t.fillcolor(colour1, colour2, colour3, 0.5)
            t.begin_fill()
            t.goto((x + 1.2) * tw, y * tw)
            for i in range(6):
                t.left(300)
                t.forward(60)

            t.end_fill()


def toilet():
    sk = 75
    for x in range(-4, 4):
        for y in range(-4, 4):
            t.penup()
            t.goto(x * sk, y * sk)
            t.setheading(0)

            colour1 = random.randint(0, 256)
            colour2 = random.randint(0, 256)
            colour3 = random.randint(0, 256)

            t.fillcolor(colour1, colour2, colour3, 0.25)
            t.begin_fill()
            t.goto((x + 1) * sk, y * sk)
            t.setheading(90)

            t.goto((x + 1) * sk, (y + 1) * sk)
            t.end_fill()


if __name__ == '__main__':
    skibidi()
    toilet()
